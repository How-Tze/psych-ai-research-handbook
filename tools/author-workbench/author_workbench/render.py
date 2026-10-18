from __future__ import annotations

import json
import copy
import re
import shutil
import threading
import uuid
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from .source import blocks, relocate, insertion_prefix
from .util import atomic_write, digest, inside, run, write_json
from .preview_security import seal_preview


def materialize(text: str, spans: list[dict], replacements: list[dict]) -> tuple[str, list[str]]:
    mapped, conflicts = {}, []
    for entry in replacements:
        state, start, end = relocate(text, entry["block"], entry["body"])
        block = next((b for b in spans if b["start"] == start and b["end"] == end), None)
        if state == "included":
            continue
        if state != "apply" or block is None or block["id"] in mapped:
            conflicts.append(entry["id"])
            continue
        mapped[block["id"]] = entry
    result = text
    for block in reversed(spans):
        entry = mapped.get(block["id"])
        value = entry["body"] if entry else block["original"]
        prefix = insertion_prefix(value)
        marker = f'<span data-aw-id="{block["id"]}"></span>'
        end_marker = f'<span data-aw-end="{block["id"]}"></span>'
        value = value[:prefix] + marker + value[prefix:] + end_marker
        result = result[:block["start"]] + value + result[block["end"]:]
        block["entry_id"] = entry["id"] if entry else None
    return result, conflicts


class Renderer:
    def __init__(self, directory, catalog, store):
        self.directory = directory / "cache"
        self.directory.mkdir(parents=True, exist_ok=True)
        self.catalog, self.store = catalog, store
        self.lock = threading.RLock()
        self.jobs = {}
        self.quarto = shutil.which("quarto")
        if not self.quarto:
            import os
            candidate = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/Quarto/bin/quarto.exe"
            if candidate.is_file():
                self.quarto = str(candidate)

    def key(self, project, drafts):
        item = self.catalog.get(project)
        pieces = [inside(item["root"], "_quarto.yml").read_bytes()]
        for page in item["pages"]:
            pieces.append(inside(item["root"], page["source"]).read_bytes())
        css = item["document"].get("format", {}).get("html", {}).get("css", [])
        for name in ([css] if isinstance(css, str) else css):
            pieces.append(inside(item["root"], name).read_bytes())
        if drafts:
            pieces.append(json.dumps([(e["id"], e["revision"], e.get("state")) for e in self.store.entries(project)
                                      if e["kind"] == "replacement"], sort_keys=True).encode())
        return digest(b"renderer-3\0" + b"\0".join(pieces) + str(drafts).encode())[:24]

    def request(self, project, drafts=True, force=False):
        key = self.key(project, drafts)
        job_id = project + "-" + key
        with self.lock:
            if job_id in self.jobs and not force:
                return dict(self.jobs[job_id])
            folder = self.directory / job_id
            if not force:
                complete = [p for p in self.directory.glob(job_id + "*") if (p / "manifest.json").is_file()]
                if complete:
                    folder = max(complete, key=lambda p: (p / "manifest.json").stat().st_mtime)
                    job_id = folder.name
            manifest = folder / "manifest.json"
            if manifest.exists() and not force:
                value = json.loads(manifest.read_text(encoding="utf-8"))
                self.jobs[job_id] = {"id": job_id, "project": project, "status": "ready", "drafts": drafts,
                                     "conflicts": value["conflicts"], "count": len(value["pages"])}
                return dict(self.jobs[job_id])
            if not self.quarto:
                raise ValueError("找不到 Quarto。请安装 Quarto 后重新打开工作台；已保存记录不受影响。")
            # Unique build directory avoids concurrent readers seeing partial output.
            if force:
                job_id += "-" + uuid.uuid4().hex[:6]
                folder = self.directory / job_id
            self.jobs[job_id] = {"id": job_id, "project": project, "status": "building", "drafts": drafts,
                                 "message": "正在准备独立阅读副本…"}
            thread = threading.Thread(target=self._build, args=(job_id, folder, project, drafts), daemon=True)
            thread.start()
            return dict(self.jobs[job_id])

    def status(self, job_id):
        with self.lock:
            if job_id not in self.jobs:
                raise ValueError("预览任务不存在，请重新打开章节")
            return dict(self.jobs[job_id])

    def manifest(self, job_id):
        self.status(job_id)
        path = self.directory / job_id / "manifest.json"
        if not path.exists():
            raise ValueError("预览尚未完成")
        return json.loads(path.read_text(encoding="utf-8"))

    def _build(self, job_id, folder, project, drafts):
        try:
            folder.mkdir(parents=True, exist_ok=True)
            item = self.catalog.get(project)
            root = item["root"]
            config = copy.deepcopy(item["document"])
            entries = [e for e in self.store.entries(project) if e["kind"] == "replacement" and e.get("state") != "withdrawn"] if drafts else []
            manifest = {"project": project, "drafts": drafts, "pages": {}, "conflicts": [],
                        "revisions": {e["id"]: e["revision"] for e in entries}}
            for page in item["pages"]:
                raw, meta = self.catalog.read(project, page["source"])
                text = raw.decode("utf-8-sig")
                spans = blocks(text)
                snapshot = self.store.snapshot(project, page["source"], raw, meta)
                result, conflicts = materialize(text, spans, [e for e in entries if e.get("source") == page["source"]])
                manifest["conflicts"].extend(conflicts)
                manifest["pages"][page["source"]] = {**page, "snapshot": snapshot, "metadata": meta, "blocks": spans}
                atomic_write(folder / page["source"], result)
            resources = set()
            for pattern in config.get("project", {}).get("resources", []):
                pattern = pattern.lstrip("/")
                if ".." in Path(pattern).parts or Path(pattern).is_absolute():
                    raise ValueError("项目资源路径不安全")
                for file in root.glob(pattern):
                    if file.is_file():
                        resources.add(file.relative_to(root).as_posix())
            html = config.get("format", {}).get("html", {})
            css = html.get("css", [])
            resources.update([css] if isinstance(css, str) else css)
            # Include local images and ordinary linked assets, never directories.
            for page in item["pages"]:
                text = inside(root, page["source"]).read_text(encoding="utf-8-sig")
                for match in re.finditer(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
                    link = match[1].split("#")[0]
                    if not link or ":" in link or link.endswith((".qmd", ".html")):
                        continue
                    candidate = (root / Path(page["source"]).parent / link).resolve()
                    if candidate.is_relative_to(root) and candidate.is_file():
                        relative = candidate.relative_to(root).as_posix()
                        if Path(relative).suffix.lower() in {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif", ".csv", ".txt", ".pdf", ".docx", ".zip", ".md"}:
                            resources.add(relative)
            for relative in resources:
                source = inside(root, relative)
                target = folder / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            config["project"]["output-dir"] = "_site"
            for key in ("pre-render", "post-render", "pre-execute", "post-execute"):
                config["project"].pop(key, None)
            config["execute"] = {"enabled": False, "freeze": False}
            config.pop("filters", None)
            config.pop("profile", None)
            html.pop("include-after-body", None)
            html.pop("include-before-body", None)
            html.pop("include-in-header", None)
            # Chromium renders MathML locally. No CDN can receive draft content.
            html["html-math-method"] = "mathml"
            html["embed-resources"] = False
            html["self-contained"] = False
            nav = config.get("book", config.get("website", {}))
            nav.pop("repo-actions", None)
            nav.pop("comments", None)
            atomic_write(folder / "_quarto.yml", yaml.safe_dump(config, allow_unicode=True, sort_keys=False))
            self.jobs[job_id]["message"] = "正在生成章节和目录；首次准备需要稍候…"
            result = run([self.quarto, "render", "--to", "html", "--no-execute"], cwd=folder, timeout=900)
            atomic_write(folder / "render.log", result.stdout + "\n" + result.stderr)
            if result.returncode:
                raise ValueError("Quarto 预览生成失败。记录已保存；可重试或查看本机预览日志。")
            total, missing = 0, []
            for source, page in manifest["pages"].items():
                output = folder / "_site" / page["page"]
                soup = BeautifulSoup(output.read_text(encoding="utf-8"), "html.parser")
                markers = {span.get("data-aw-id") for span in soup.select("[data-aw-id]")}
                for block in page["blocks"]:
                    block["mapped"] = block["id"] in markers
                    if not block["mapped"]:
                        missing.append({"source": source, "id": block["id"]})
                total += len(markers)
                seal_preview(soup)
                atomic_write(output, str(soup))
            manifest["unmapped"] = missing
            write_json(folder / "manifest.json", manifest)
            with self.lock:
                self.jobs[job_id].update(status="ready", message="预览已生成", conflicts=manifest["conflicts"], count=len(manifest["pages"]), mapped=total, unmapped=len(missing))
        except Exception as exc:
            with self.lock:
                self.jobs[job_id].update(status="error", message=str(exc))
