#!/usr/bin/env python3
"""Check internal Markdown links, fenced blocks, and JSON examples."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)


def check_fences(path: Path, content: str) -> list[str]:
    errors: list[str] = []
    fence_char: str | None = None
    fence_size = 0
    start_line = 0

    for line_number, line in enumerate(content.splitlines(), start=1):
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match and fence_char is None:
            marker = match.group(1)
            fence_char = marker[0]
            fence_size = len(marker)
            start_line = line_number
            continue

        if fence_char is not None:
            close = re.match(r"^\s*([\`~]+)\s*$", line)
            if close:
                marker = close.group(1)
                if marker[0] == fence_char and len(marker) >= fence_size and len(set(marker)) == 1:
                    fence_char = None
                    fence_size = 0

    if fence_char is not None:
        errors.append(f"{path.relative_to(ROOT)}:{start_line}: unclosed Markdown code fence")
    return errors


def check_links(path: Path, content: str) -> tuple[list[str], int]:
    errors: list[str] = []
    count = 0

    for match in LINK_RE.finditer(content):
        target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(target)

        if parsed.scheme or target.startswith("//") or not parsed.path:
            continue

        relative_target = Path(unquote(parsed.path))
        resolved = (path.parent / relative_target).resolve()

        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(
                f"{path.relative_to(ROOT)}: link escapes repository: {target}"
            )
            continue

        count += 1
        if not resolved.exists():
            errors.append(
                f"{path.relative_to(ROOT)}: broken internal link: {target}"
            )

    return errors, count


def main() -> int:
    markdown_files = sorted(
        path for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )
    errors: list[str] = []
    link_count = 0
    json_count = 0

    for path in markdown_files:
        content = path.read_text(encoding="utf-8")
        errors.extend(check_fences(path, content))
        link_errors, links_found = check_links(path, content)
        errors.extend(link_errors)
        link_count += links_found

        for example in JSON_FENCE_RE.findall(content):
            try:
                json.loads(example)
                json_count += 1
            except json.JSONDecodeError as exc:
                errors.append(
                    f"{path.relative_to(ROOT)}: invalid JSON example: {exc}"
                )

    skill = ROOT / "skills/civic-waste-investigator/SKILL.md"
    if skill.exists():
        skill_text = skill.read_text(encoding="utf-8")
        if not skill_text.startswith("---\n") or "\n---\n" not in skill_text[4:]:
            errors.append("skills/civic-waste-investigator/SKILL.md: missing front matter")
        elif "name: civic-waste-investigator" not in skill_text:
            errors.append("skills/civic-waste-investigator/SKILL.md: missing skill name")
    else:
        errors.append("skills/civic-waste-investigator/SKILL.md: file is missing")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(
        f"Documentation checks passed: {len(markdown_files)} Markdown files, "
        f"{link_count} internal links, {json_count} JSON examples."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
