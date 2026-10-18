"""Explicit batch integration into a separate worktree, never publication."""
from __future__ import annotations

from pathlib import Path
from .source import relocate
from .util import atomic_write, digest, git, inside


def validate_target(catalog, project: str, target: Path) -> Path:
    original = catalog.get(project)["root"]
    target = target.resolve()
    if target == original or target.is_relative_to(original):
        raise ValueError("请指定独立的整合工作副本，不能向正在阅读的项目写入")
    branch = git(target, "branch", "--show-current")
    if not branch or branch in {"main", "master", "gh-pages"}:
        raise ValueError("整合只能写入专用分支，不能写入 main 或历史标签")
    # A real worktree shares its Git common directory. An independent clone
    # must have the same origin, preventing an accidental write to another repo.
    source_common = Path(git(original, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
    target_common = Path(git(target, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
    if source_common != target_common:
        if git(original, "remote", "get-url", "origin").rstrip("/") != git(target, "remote", "get-url", "origin").rstrip("/"):
            raise ValueError("整合副本不是同一个项目")
    return target


def apply_exact(store, catalog, batch_id: str, target: Path, *, write=False) -> dict:
    batch = store.batch(batch_id)
    target = validate_target(catalog, batch["project"], target)
    files, results = {}, []
    for item in batch["items"]:
        if item["kind"] != "replacement":
            continue
        catalog.page(batch["project"], item["source"])
        path = inside(target, item["source"])
        if item["source"] not in files:
            raw = path.read_bytes()
            files[item["source"]] = {"path": path, "raw": raw, "text": raw.decode("utf-8-sig"), "edits": []}
        file = files[item["source"]]
        receipt = item.get("result") or {}
        if (receipt.get("outcome") in {"applied", "included"}
                and receipt.get("evidence", {}).get("sha256") == digest(file["raw"])):
            state, start, end = "included", -1, -1
        else:
            snapshot = store.get_snapshot(item["snapshot"])
            state, start, end = relocate(file["text"], item["block"], item["body"], digest(snapshot["text"]))
        result = {"entry_id": item["id"], "revision": item["revision"], "source": item["source"], "outcome": state}
        if state == "conflict":
            result.update(original=item["block"]["original"], author=item["body"],
                          current=file["text"][max(0,item["block"]["start"]-200):item["block"]["end"]+200])
        elif state == "apply":
            file["edits"].append((start, end, item["body"], result))
        results.append(result)
    for file in files.values():
        edits = sorted(file["edits"])
        for previous, following in zip(edits, edits[1:]):
            if previous[1] > following[0]:
                previous[3]["outcome"] = following[3]["outcome"] = "conflict"
                previous[3]["reason"] = following[3]["reason"] = "同一范围有多条修改，需要先选择采用哪一稿"
    conflicts = any(r["outcome"] == "conflict" for r in results)
    if write and not conflicts:
        store.set_target(batch_id, str(target))
        changed = []
        try:
            for file in files.values():
                if file["path"].read_bytes() != file["raw"]:
                    raise ValueError("整合期间源码已变化，请重新检查")
            for source, file in files.items():
                text = file["text"]
                for start, end, replacement, _ in sorted(file["edits"], key=lambda e:e[0], reverse=True):
                    text = text[:start] + replacement + text[end:]
                raw = (b"\xef\xbb\xbf" if file["raw"].startswith(b"\xef\xbb\xbf") else b"") + text.encode("utf-8")
                if raw != file["raw"]:
                    atomic_write(file["path"], raw)
                    changed.append(file)
                for result in results:
                    if result["source"] == source:
                        result["outcome"] = "applied" if result["outcome"] == "apply" else "included"
                        result["evidence"] = {"file": source, "sha256": digest(raw), "branch": git(target, "branch", "--show-current")}
        except Exception:
            for file in reversed(changed):
                atomic_write(file["path"], file["raw"])
            raise
        for result in results:
            store.result(batch_id, result["entry_id"], result)
    return {"batch": batch_id, "target": str(target), "written": bool(write and not conflicts), "conflicts": conflicts, "items": results}


def record_result(store, catalog, batch_id, entry_id, outcome, reason, target=None, file=None):
    batch = store.batch(batch_id)
    item = next((e for e in batch["items"] if e["id"] == entry_id), None)
    if not item:
        raise ValueError("记录不属于该批次")
    result = {"outcome": outcome, "reason": reason}
    if outcome in {"applied", "included"}:
        if not target or not file:
            raise ValueError("已整合结果需要候选工作副本和具体文件证据")
        if item["kind"] == "replacement":
            raise ValueError("直接改字请使用 apply-exact 检查并记录，不能跳过逐字核验")
        project = batch["project"]
        if project == "all":
            matches = []
            for key in catalog.projects:
                try:
                    matches.append((key, validate_target(catalog, key, Path(target))))
                except ValueError:
                    continue
            if len(matches) != 1:
                raise ValueError("跨项目意见需要指定可明确识别项目的独立候选副本")
            project, target = matches[0]
        else:
            target = validate_target(catalog, project, Path(target))
        catalog.page(project, file)
        path = inside(target, file)
        # Require an actual candidate change or committed change since baseline.
        original = inside(catalog.get(project)["root"], file).read_bytes()
        if path.read_text(encoding="utf-8-sig") == original.decode("utf-8-sig").replace("\r\n", "\n"):
            raise ValueError("指定文件与当前正式来源一致，尚无候选修改证据")
        if not reason.strip():
            raise ValueError("请说明该文件如何回应这条意见")
        if batch["project"] != "all":
            store.set_target(batch_id, str(target))
        result["evidence"] = {"project": project, "target": str(target), "file": file, "sha256": digest(path.read_bytes()), "branch": git(target,"branch","--show-current")}
    store.result(batch_id, entry_id, result)
    return result
