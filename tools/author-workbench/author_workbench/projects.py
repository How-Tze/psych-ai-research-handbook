from __future__ import annotations

import json
import hashlib
from pathlib import Path
import re
from urllib.parse import parse_qs, unquote, urlsplit
import yaml

from .util import digest, git, inside, write_json


PROJECTS = {
    "handbook": {"name": "心理学研究的 AI 进阶手册", "repo": "psych-ai-research-handbook", "version": "v1.3"},
    "guide": {"name": "心理学研究者的 AI Start Guide", "repo": "psych-ai-start-guide", "version": "v0.12"},
}


def configure(data_dir: Path, handbook: Path, guide: Path) -> dict:
    value = {"schema": 1, "projects": {"handbook": str(handbook.resolve()), "guide": str(guide.resolve())}}
    for root in value["projects"].values():
        if not (Path(root) / "_quarto.yml").is_file():
            raise ValueError("请选择包含 _quarto.yml 的项目目录")
    write_json(data_dir / "config.json", value)
    return value


def discover(data_dir: Path) -> dict:
    path = data_dir / "config.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8-sig"))
    candidates = [Path(__file__).resolve().parents[3], Path.home() / "Documents/Research_Projects/psych-ai-research-handbook"]
    for root in candidates:
        if (root / "_quarto.yml").is_file() and (root.parent / "psych-ai-start-guide/_quarto.yml").is_file():
            return configure(data_dir, root, root.parent / "psych-ai-start-guide")
    raise ValueError("首次使用需要选择主手册和动态指南的本地项目目录。")


def frontmatter(text: str) -> dict:
    found = re.match(r"\ufeff?---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    return (yaml.safe_load(found.group(1)) or {}) if found else {}


def qmd_paths(value):
    if isinstance(value, str) and value.endswith(".qmd"):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from qmd_paths(item)
    elif isinstance(value, dict):
        for key in ("href", "chapters", "contents"):
            yield from qmd_paths(value.get(key))


class Catalog:
    def __init__(self, config: dict):
        self.config = config
        self.projects = {}
        for project_id, location in config["projects"].items():
            if project_id not in PROJECTS:
                raise ValueError("未知项目")
            root = Path(location).resolve()
            document = yaml.safe_load(inside(root, "_quarto.yml").read_text(encoding="utf-8"))
            nav = document.get("book") or document.get("website") or {}
            paths = list(qmd_paths(nav.get("chapters", nav.get("sidebar", []))))
            if not paths:
                for pattern in document.get("project", {}).get("render", []):
                    paths.extend(p.relative_to(root).as_posix() for p in sorted(root.glob(pattern)))
            pages = []
            for source in dict.fromkeys(paths):
                raw = inside(root, source).read_bytes()
                title = frontmatter(raw.decode("utf-8-sig")).get("title", Path(source).stem)
                pages.append({"source": source, "page": str(Path(source).with_suffix(".html")).replace("\\", "/"), "title": str(title)})
            self.projects[project_id] = {**PROJECTS[project_id], "id": project_id, "root": root,
                                          "document": document, "pages": pages,
                                          "url": nav.get("site-url", "").rstrip("/") + "/"}

    def get(self, project: str) -> dict:
        if project not in self.projects:
            raise ValueError("未知项目")
        return self.projects[project]

    def page(self, project: str, source: str) -> dict:
        found = next((p for p in self.get(project)["pages"] if p["source"] == source), None)
        if not found:
            raise ValueError("该页面不在当前出版目录中")
        return found

    def read(self, project: str, source: str):
        self.page(project, source)
        root = self.get(project)["root"]
        raw = inside(root, source).read_bytes()
        try:
            commit = git(root, "rev-parse", "HEAD")
            dirty = bool(git(root, "status", "--porcelain", "--", source))
        except ValueError:
            commit, dirty = None, True
        # Line endings can differ between a Windows checkout and a Linux build.
        public_hash = hashlib.sha1(raw.replace(b"\r\n", b"\n")).hexdigest()
        return raw, {"commit": commit, "dirty": dirty, "hash": digest(raw), "public_build": "sha1:" + public_hash}

    def public(self) -> list[dict]:
        return [{k: v for k, v in p.items() if k not in {"root", "document"}} for p in self.projects.values()]

    def target(self, value: str) -> dict:
        if not value:
            return {}
        if len(value) > 4096:
            raise ValueError("地址过长")
        parsed = urlsplit(value)
        if parsed.scheme == "psychauthor":
            if parsed.netloc != "open" or parsed.path not in {"", "/"}:
                raise ValueError("不支持的作者入口")
            query = parse_qs(parsed.query)
            if set(query) - {"project", "page", "anchor", "build", "quote", "url"}:
                raise ValueError("入口包含未知操作")
            if "url" in query:
                return self.target(query["url"][0])
            project = query.get("project", ["handbook"])[0]
            page = query.get("page", ["index.html"])[0]
            anchor = query.get("anchor", [""])[0]
            build = query.get("build", [""])[0]
            quote = query.get("quote", [""])[0]
        elif parsed.scheme in {"https", "http"}:
            project = None
            for key, item in self.projects.items():
                base = urlsplit(item["url"])
                if parsed.hostname == base.hostname and parsed.path.startswith(base.path):
                    project = key
                    page = unquote(parsed.path[len(base.path):]) or "index.html"
                    break
            if project is None:
                raise ValueError("这不是两站中的页面地址")
            query = parse_qs(parsed.query)
            anchor = unquote(parsed.fragment)
            build = query.get("aw-build", [""])[0]
            quote = query.get("aw-quote", [""])[0]
        else:
            raise ValueError("请粘贴两站的完整页面地址")
        item = self.get(project)
        if any(x in page for x in ("..", "\\", ":")) or page.startswith("/"):
            raise ValueError("无效页面路径")
        aliases = {"chapters/00-usage.html": "chapters/01-introduction.html", "chapters/09-maintenance.html": "chapters/11-safety-recovery.html"}
        if project == "handbook":
            page = aliases.get(page, page)
        found = next((p for p in item["pages"] if p["page"] == page), None)
        if not found:
            raise ValueError("该地址尚未对应当前章节，请在工作台选择章节；原意见仍可记录。")
        return {"project": project, "source": found["source"], "anchor": anchor[:1000], "build": build[:128], "quote": quote[:160], "from_public": True}
