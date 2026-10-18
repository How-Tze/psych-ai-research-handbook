from __future__ import annotations

import json
import mimetypes
import secrets
import sqlite3
from pathlib import Path
import threading
import time

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse, Response

from . import __version__
from .projects import Catalog
from .render import Renderer
from .source import blocks
from .store import Store, Conflict
from .util import inside
from .preview_security import NONCE_MARKER, preview_policy


class Runtime:
    def __init__(self, directory: Path, config: dict, frontend: Path, app_port: int, preview_port: int):
        self.directory, self.frontend = directory, frontend
        self.catalog, self.store = Catalog(config), Store(directory)
        self.renderer = Renderer(directory, self.catalog, self.store)
        self.master, self.instance, self.preview_key = secrets.token_urlsafe(32), secrets.token_hex(16), secrets.token_urlsafe(24)
        self.origin = f"http://127.0.0.1:{app_port}"
        self.preview_origin = f"http://127.0.0.1:{preview_port}"
        self.sessions, self.boots = {}, {}
        self.boot_lock = threading.Lock()
        self.shutdown = None

    def launch(self, target=None):
        token = secrets.token_urlsafe(32)
        with self.boot_lock:
            self.boots[token] = (time.time() + 60, target or {})
        return self.origin + "/#boot=" + token

    def exchange(self, token):
        with self.boot_lock:
            entry = self.boots.pop(token, None)
        if not entry or entry[0] < time.time():
            raise ValueError("启动链接已使用或过期。请从桌面入口重新打开。")
        session = secrets.token_urlsafe(32)
        self.sessions[session] = time.time() + 7 * 86400
        return {"session": session, "target": entry[1]}

    def authorized(self, request):
        token = request.headers.get("authorization", "").removeprefix("Bearer ")
        return token in self.sessions and self.sessions[token] > time.time()


def app_for(runtime: Runtime) -> FastAPI:
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @app.middleware("http")
    async def boundary(request: Request, call_next):
        if request.headers.get("host") != runtime.origin.removeprefix("http://"):
            return JSONResponse({"error": "无效的本机地址"}, status_code=403)
        origin = request.headers.get("origin")
        if origin and origin != runtime.origin:
            return JSONResponse({"error": "该请求不来自作者工作台"}, status_code=403)
        if request.url.path.startswith("/api/") and not runtime.authorized(request):
            return JSONResponse({"error": "请从桌面入口重新打开工作台"}, status_code=401)
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Content-Security-Policy"] = f"default-src 'self'; frame-src {runtime.preview_origin}; style-src 'self' 'unsafe-inline'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
        return response

    @app.exception_handler(ValueError)
    async def expected_error(request, exc):
        return JSONResponse({"error": str(exc)}, status_code=409 if isinstance(exc, Conflict) else 400)

    async def body(request):
        raw = await request.body()
        if len(raw) > 600000:
            raise ValueError("请求内容过长")
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("请求格式错误")
        return data

    @app.get("/health")
    def health():
        return {"app": "psych-ai-author-workbench", "version": __version__, "instance": runtime.instance}

    @app.post("/launch")
    async def launch(request: Request):
        if request.headers.get("origin") or not secrets.compare_digest(request.headers.get("authorization", ""), "Bearer " + runtime.master):
            return JSONResponse({"error": "启动请求无效"}, status_code=403)
        data = await body(request)
        target = runtime.catalog.target(data.get("uri", ""))
        return {"url": runtime.launch(target)}

    @app.post("/bootstrap")
    async def bootstrap(request: Request):
        return runtime.exchange((await body(request)).get("token", ""))

    @app.post("/shutdown")
    def shutdown(request: Request):
        if request.headers.get("origin") or not secrets.compare_digest(request.headers.get("authorization", ""), "Bearer " + runtime.master):
            return JSONResponse({"error": "停止请求无效"}, status_code=403)
        if runtime.shutdown:
            threading.Timer(.2, runtime.shutdown).start()
        return {"ok": True}

    @app.get("/api/state")
    def state():
        return {"projects": runtime.catalog.public(), "version": __version__, "last": runtime.store.setting("last"),
                "data_directory": str(runtime.directory), "preview_origin": runtime.preview_origin,
                "entries": runtime.store.entries(), "batches": runtime.store.batches()}

    @app.post("/api/location")
    async def location(request: Request):
        data = await body(request)
        if data.get("project") not in runtime.catalog.projects:
            raise ValueError("未知项目")
        runtime.catalog.page(data["project"], data["source"])
        runtime.store.setting("last", {k: data.get(k) for k in ("project", "source", "anchor")})
        return {"ok": True}

    @app.post("/api/open-url")
    async def open_url(request: Request):
        return runtime.catalog.target((await body(request)).get("url", ""))

    @app.post("/api/render")
    async def render(request: Request):
        data = await body(request)
        return runtime.renderer.request(data.get("project", "handbook"), bool(data.get("drafts", True)), bool(data.get("force", False)))

    @app.get("/api/render/{job_id}")
    def render_status(job_id: str):
        return runtime.renderer.status(job_id)

    @app.get("/api/document/{job_id}")
    def document(job_id: str, source: str):
        manifest = runtime.renderer.manifest(job_id)
        if source not in manifest["pages"]:
            raise ValueError("页面不属于该预览")
        page = manifest["pages"][source]
        return {**page, "build": job_id, "drafts": manifest["drafts"], "revisions": manifest["revisions"],
                "conflicts": manifest["conflicts"],
                "preview": f"{runtime.preview_origin}/p/{runtime.preview_key}/{job_id}/{page['page']}",
                "entries": runtime.store.entries(manifest["project"], source)}

    @app.get("/api/entries")
    def entries():
        return runtime.store.entries()

    @app.get("/api/entries/{entry_id}/history")
    def history(entry_id: str):
        return runtime.store.history(entry_id)

    @app.post("/api/entries")
    async def save(request: Request):
        data = await body(request)
        entry_id = data.get("id")
        if entry_id:
            previous = runtime.store.entry(entry_id)
            payload = {k: v for k, v in previous.items() if k not in {"id", "revision", "updated"}}
            for key in ("body", "intent", "state"):
                if key in data:
                    payload[key] = data[key]
        else:
            kind, project = data.get("kind"), data.get("project")
            if project == "all" and kind == "idea":
                payload = {"kind": kind, "project": project, "source": "", "snapshot": None, "quote": ""}
            else:
                runtime.catalog.page(project, data.get("source", ""))
                snapshot = runtime.store.get_snapshot(data.get("snapshot", ""))
                if snapshot["project"] != project or snapshot["source"] != data["source"]:
                    raise ValueError("原文快照与当前章节不一致")
                payload = {"kind": kind, "project": project, "source": data["source"], "snapshot": snapshot["id"],
                           "quote": str(data.get("quote", ""))[:12000], "section": str(data.get("section", ""))[:1000]}
                if data.get("block_id"):
                    block = next((b for b in blocks(snapshot["text"]) if b["id"] == data["block_id"]), None)
                    if not block:
                        raise ValueError("段落已变化，请重新打开该段")
                    payload.update(block_id=block["id"], block=block)
                elif kind == "replacement":
                    raise ValueError("请选择需要修改的段落")
            payload.update(body=data.get("body", ""), intent=data.get("intent", "next"), state="active")
        result = runtime.store.save(payload, entry_id, int(data.get("expected", 0)))
        # A successful response means the transaction has committed. A backup
        # failure must not falsely report that the edit itself was not saved.
        try:
            runtime.store.backup(automatic=True)
        except (OSError, sqlite3.Error):
            result["backup_warning"] = "修改已保存，自动备份未完成；请稍后重试备份。"
        return result

    @app.post("/api/entries/{entry_id}/undo")
    async def undo(entry_id: str, request: Request):
        data = await body(request)
        old = runtime.store.entry(entry_id, int(data["revision"]))
        current = runtime.store.entry(entry_id)
        payload = {k: v for k, v in current.items() if k not in {"id", "revision", "updated"}}
        payload.update(body=old["body"], state=old.get("state", "active"), intent=old["intent"])
        return runtime.store.save(payload, entry_id, int(data["expected"]))

    @app.get("/api/backups")
    def backups():
        return runtime.store.backups()

    @app.post("/api/backup")
    def backup():
        path = runtime.store.backup()
        return {"name": path.name, "path": str(path)}

    @app.get("/api/backups/{name}")
    def download_backup(name: str):
        if name not in {p["name"] for p in runtime.store.backups()}:
            raise ValueError("备份不存在")
        return FileResponse(runtime.directory / "backups" / name, filename=name)

    @app.post("/api/restore")
    async def restore(request: Request):
        data = await body(request)
        if data.get("confirmation") != "恢复备份":
            raise ValueError("请确认恢复备份；当前记录会先自动备份")
        return runtime.store.restore(data.get("name", ""))

    @app.post("/api/batches")
    async def prepare(request: Request):
        data = await body(request)
        project = data.get("project")
        if project not in {*runtime.catalog.projects, "all"}:
            raise ValueError("未知项目")
        batch = runtime.store.prepare_batch(project, data.get("task", ""), data.get("ids"))
        destination = runtime.store.export_batch(batch["id"])
        return {"batch": batch, "path": str(destination)}

    @app.get("/api/batches/{batch_id}")
    def batch(batch_id: str):
        value = runtime.store.batch(batch_id)
        return {**value, "path": str(runtime.store.export_batch(batch_id))}

    @app.get("/{path:path}")
    def static(path: str):
        if not path:
            path = "index.html"
        try:
            target = inside(runtime.frontend, path)
        except ValueError:
            return Response(status_code=404)
        return FileResponse(target)

    return app


def preview_app(runtime: Runtime, bridge_file: Path):
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @app.middleware("http")
    async def boundary(request: Request, call_next):
        if request.headers.get("host") != runtime.preview_origin.removeprefix("http://") or request.method not in {"GET", "HEAD"}:
            return Response(status_code=403)
        result = await call_next(request)
        result.headers["Cache-Control"] = "no-store"
        result.headers["Referrer-Policy"] = "no-referrer"
        result.headers["X-Content-Type-Options"] = "nosniff"
        # HTML routes supply their own per-response script nonce.
        if "Content-Security-Policy" not in result.headers:
            result.headers["Content-Security-Policy"] = preview_policy(runtime.origin, secrets.token_urlsafe(24))
        return result

    @app.get("/bridge.js")
    def bridge():
        content = "window.awParentOrigin=" + json.dumps(runtime.origin) + ";\n" + bridge_file.read_text(encoding="utf-8")
        return Response(content, media_type="application/javascript")

    @app.get("/p/{key}/{job_id}/{path:path}")
    def page(key: str, job_id: str, path: str):
        if not secrets.compare_digest(key, runtime.preview_key):
            return Response(status_code=403)
        try:
            runtime.renderer.status(job_id)
            if runtime.renderer.status(job_id)["status"] != "ready":
                return Response(status_code=404)
            target = inside(runtime.renderer.directory / job_id / "_site", path or "index.html")
        except ValueError:
            return Response(status_code=404)
        if target.suffix.lower() == ".html":
            nonce = secrets.token_urlsafe(24)
            # Also seals old caches and static demonstration HTML before serving.
            from bs4 import BeautifulSoup
            from .preview_security import seal_preview
            soup = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
            seal_preview(soup)
            content = str(soup).replace(NONCE_MARKER, nonce)
            return Response(content, media_type="text/html", headers={"Content-Security-Policy": preview_policy(runtime.origin, nonce)})
        return FileResponse(target)

    return app
