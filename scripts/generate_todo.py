#!/usr/bin/env python3
"""Generate the root TODO.md from open Markdown task list items."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "TODO.md"

TASK_RE = re.compile(r"^\s*[-*]\s+\[ \]\s+(.+?)\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HTML_COMMENT_RE = re.compile(r"\s*<!--.*?-->\s*")


@dataclass(frozen=True)
class Task:
    path: Path
    line: int
    document: str
    text: str


def clean_label(text: str) -> str:
    """Keep a readable task label without nesting links in the generated link."""
    text = INLINE_LINK_RE.sub(r"\1", text)
    text = HTML_COMMENT_RE.sub("", text)
    return text.strip()


def collect_tasks() -> list[Task]:
    tasks: list[Task] = []

    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if relative == Path("TODO.md") or any(part.startswith(".") for part in relative.parts):
            continue

        document = path.stem
        in_fence = False

        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.lstrip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue

            if in_fence:
                continue

            heading = HEADING_RE.match(line)
            if heading and len(heading.group(1)) == 1:
                document = clean_label(heading.group(2))
                continue

            task = TASK_RE.match(line)
            if task:
                tasks.append(
                    Task(
                        path=relative,
                        line=line_number,
                        document=document,
                        text=clean_label(task.group(1)),
                    )
                )

    return tasks


def render(tasks: list[Task]) -> str:
    grouped: dict[str, dict[str, list[Task]]] = defaultdict(lambda: defaultdict(list))

    for task in tasks:
        parent = task.path.parent
        group = " / ".join(parent.parts) if parent.parts else "Repozitář"
        grouped[group][task.document].append(task)

    lines = [
        "# TODO",
        "",
        "> Tento soubor je automaticky generovaný přehled. Úkol upravuj nebo označ jako",
        "> hotový v odkazovaném původním dokumentu; `TODO.md` se potom obnoví automaticky.",
        "",
    ]

    if not tasks:
        lines.extend(["Aktuálně nejsou evidované žádné otevřené úkoly.", ""])
        return "\n".join(lines)

    for group in sorted(grouped):
        lines.extend([f"## {group}", ""])

        for document in sorted(grouped[group]):
            lines.extend([f"### {document}", ""])

            for task in sorted(grouped[group][document], key=lambda item: (item.path.as_posix(), item.line)):
                target = quote(task.path.as_posix(), safe="/-._~")
                lines.append(f"- [ ] [{task.text}]({target}?plain=1#L{task.line})")

            lines.append("")

    return "\n".join(lines)


def main() -> None:
    OUTPUT.write_text(render(collect_tasks()), encoding="utf-8")


if __name__ == "__main__":
    main()
