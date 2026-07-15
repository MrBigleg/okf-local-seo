#!/usr/bin/env python3
"""Create a deterministic weekly freshness report without changing knowledge."""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

FRONTMATTER_END = re.compile(r"^---\s*$", re.MULTILINE)
DATE_VALUE = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    matches = list(FRONTMATTER_END.finditer(text))
    if len(matches) < 2 or matches[0].start() != 0:
        return {}
    values: dict[str, str] = {}
    for line in text[matches[0].end() : matches[1].start()].splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def parsed_date(value: str) -> dt.date | None:
    match = DATE_VALUE.match(value)
    if not match:
        return None
    try:
        return dt.date.fromisoformat(match.group(1))
    except ValueError:
        return None


def cadence_days(relative: Path, kind: str) -> int:
    if relative.parts and relative.parts[0] == "agentic":
        return 31
    if kind == "Reference" or (relative.parts and relative.parts[0] == "references"):
        return 92
    return 183


def build_report(bundle: Path, today: dt.date) -> str:
    rows: list[tuple[Path, dt.date | None, int, int | None]] = []
    for path in sorted(bundle.rglob("*.md")):
        if path.name in {"index.md", "log.md"}:
            continue
        meta = frontmatter(path)
        relative = path.relative_to(bundle)
        last = parsed_date(meta.get("accessed", "")) or parsed_date(meta.get("timestamp", ""))
        cadence = cadence_days(relative, meta.get("type", ""))
        age = (today - last).days if last else None
        if age is None or age >= cadence:
            rows.append((relative, last, cadence, age))

    lines = [
        f"# Weekly Local SEO knowledge review — {today.isoformat()}",
        "",
        "> Automation prepared this review queue. It did not research, edit, approve, or merge factual claims.",
        "",
        "## Human review checklist",
        "",
        "- [ ] Review URL-health output in `weekly-url-check.txt`.",
        "- [ ] Re-open primary sources for every edited volatile claim.",
        "- [ ] Update affected concept/reference dates and `bundles/local-seo/log.md`.",
        "- [ ] Run the verifier and regenerate `viz.html`.",
        "- [ ] Obtain human approval before merge.",
        "",
        "## Pages due for freshness review",
        "",
        "| Page | Last evidence date | Cadence | Age |",
        "|---|---:|---:|---:|",
    ]
    if rows:
        for relative, last, cadence, age in rows:
            lines.append(
                f"| `{relative.as_posix()}` | {last.isoformat() if last else 'missing'} | "
                f"{cadence} days | {age if age is not None else 'unknown'} |"
            )
    else:
        lines.append("| _None_ | — | — | — |")
    lines.extend(["", "## Editorial notes", "", "Add researched findings here before marking the PR ready.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", nargs="?", default="bundles/local-seo")
    parser.add_argument("--date", help="UTC date override for deterministic tests (YYYY-MM-DD)")
    args = parser.parse_args()
    bundle = Path(args.bundle).resolve()
    today = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(dt.timezone.utc).date()
    output = Path("reviews/weekly") / f"{today.isoformat()}.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_report(bundle, today), encoding="utf-8", newline="\n")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
