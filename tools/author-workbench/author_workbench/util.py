from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from datetime import datetime, timezone


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def digest(data: str | bytes) -> str:
    return hashlib.sha256(data.encode("utf-8") if isinstance(data, str) else data).hexdigest()


def home_dir() -> Path:
    return Path(os.environ.get("LOCALAPPDATA", Path.home() / ".local/share")) / "PsychAI" / "AuthorWorkbench"


def atomic_write(path: Path, data: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = data.encode("utf-8") if isinstance(data, str) else data
    fd, temporary = tempfile.mkstemp(prefix=".writing-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(raw)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(path: Path, value) -> None:
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=2))


def inside(root: Path, relative: str, *, must_exist=True) -> Path:
    if not relative or "\\" in relative or ":" in relative:
        raise ValueError("无效的项目路径")
    parts = Path(relative).parts
    if Path(relative).is_absolute() or any(p in {"..", ".git", ".qa", ".env"} for p in parts):
        raise ValueError("路径超出项目范围")
    root = root.resolve()
    target = (root / relative).resolve()
    if not target.is_relative_to(root) or target == root:
        raise ValueError("路径超出项目范围")
    # Also reject links pointing to a different file within the root.
    cursor = root
    for part in parts:
        cursor = cursor / part
        if cursor.is_symlink() or (hasattr(cursor, "is_junction") and cursor.is_junction()):
            raise ValueError("不读取链接目录或文件")
    if must_exist and not target.is_file():
        raise ValueError("找不到对应文件")
    return target


def run(args: list[str], *, cwd: Path | None = None, timeout=30):
    return subprocess.run(args, cwd=cwd, capture_output=True, encoding="utf-8", errors="replace",
                          timeout=timeout, creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)


def git(root: Path, *args: str) -> str:
    result = run(["git", "-C", str(root), *args])
    if result.returncode:
        raise ValueError("Git 检查失败：" + result.stderr.strip()[:300])
    return result.stdout.strip()
