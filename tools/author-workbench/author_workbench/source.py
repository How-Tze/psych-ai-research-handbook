"""Exact source spans. Markers are inserted only into isolated render copies."""
from __future__ import annotations

import re
from markdown_it import MarkdownIt
from .util import digest


def insertion_prefix(source: str) -> int:
    return len(re.match(r"^(?:[ \t]*>[ \t]*)*(?:[ \t]*(?:[-+*]|\d+[.)])[ \t]+(?:\[[ xX]\][ \t]+)?)?", source).group(0))


def blocks(text: str) -> list[dict]:
    lines = text.splitlines(keepends=True)
    scan = list(lines)
    # Preserve line coordinates while preventing Quarto delimiters from
    # becoming ordinary paragraphs in the CommonMark span parser.
    yaml = bool(lines and lines[0].lstrip("\ufeff").strip() == "---")
    math = False
    fenced = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if yaml:
            scan[i] = "\n"
            if i and stripped in {"---", "..."}:
                yaml = False
            continue
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            fence = match.group(1)
            if fenced is None:
                fenced = fence
            elif fence[0] == fenced[0] and len(fence) >= len(fenced):
                fenced = None
            continue
        if fenced:
            continue
        if stripped.startswith("$$"):
            if stripped == "$$":
                math = not math
            scan[i] = "\n"
        elif math or re.match(r"^:{3,}", stripped):
            scan[i] = "\n"
    offsets, count = [], 0
    for line in lines:
        offsets.append(count)
        count += len(line)
    offsets.append(count)
    tokens = MarkdownIt("commonmark").enable("table").parse("".join(scan))
    result, section = [], ""
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and index + 1 < len(tokens):
            section = tokens[index + 1].content
        if token.type != "paragraph_open" or token.map is None:
            continue
        start_line, end_line = token.map
        start, end = offsets[start_line], offsets[end_line]
        source = text[start:end].rstrip("\r\n")
        end = start + len(source)
        if not source.strip() or source.lstrip().startswith((":::" , "$$", "<", "<!--")):
            continue
        # A block must stay inside one paragraph/list leaf, not consume a table.
        if any(re.match(r"^\s*\|", x) for x in source.splitlines()):
            continue
        inline = tokens[index + 1] if index + 1 < len(tokens) else None
        if inline is None or inline.type != "inline":
            continue
        if any(child.type == "image" for child in (inline.children or [])):
            continue  # Inline markers would turn Quarto figures into plain images.
        prefix = insertion_prefix(source)
        block_id = "b" + digest(f"{start}:{end}:{source}")[:18]
        result.append({"id": block_id, "start": start, "end": end, "line": start_line + 1,
                       "original": source, "hash": digest(source), "section": section,
                       "occurrences": text.count(source),
                       "prefix": text[max(0, start - 180):start], "suffix": text[end:end + 180],
                       "insert": start + prefix, "plain": inline.content})
    # No overlapping editable ranges are accepted.
    previous = -1
    for block in result:
        if block["start"] < previous:
            raise ValueError("段落范围重叠，当前页请使用章节批注")
        previous = block["end"]
    return result


def annotate(text: str, spans: list[dict]) -> str:
    for block in reversed(spans):
        at = block["insert"]
        text = text[:at] + f'<span data-aw-id="{block["id"]}"></span>' + text[at:]
    return text


def relocate(current: str, block: dict, replacement: str, base_hash: str | None = None) -> tuple[str, int, int]:
    original = block["original"]
    if base_hash == digest(current) and current[block["start"]:block["end"]] == original:
        return "apply", block["start"], block["end"]

    def positions(needle):
        if not needle:
            return []
        return [m.start() for m in re.finditer(re.escape(needle), current)]

    def contextual(candidates, needle):
        before, after = block.get("prefix", ""), block.get("suffix", "")
        return [p for p in candidates if
                (not before or current[max(0, p - len(before)):p] == before) and
                (not after or current[p + len(needle):p + len(needle) + len(after)] == after)]

    # Being present somewhere is insufficient to claim an edit was integrated.
    included = contextual(positions(replacement), replacement)
    if len(included) == 1:
        return "included", included[0], included[0] + len(replacement)
    if not replacement and block.get("prefix") and block.get("suffix"):
        joined = block["prefix"] + block["suffix"]
        if current.count(joined) == 1:
            p = current.index(joined) + len(block["prefix"])
            return "included", p, p
    candidates = positions(original)
    if len(candidates) > 1 or block.get("occurrences", 2) > 1:
        candidates = contextual(candidates, original)
    if len(candidates) == 1:
        p = candidates[0]
        return "apply", p, p + len(original)
    return "conflict", -1, -1
