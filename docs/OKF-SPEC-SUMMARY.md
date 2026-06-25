# OKF v0.1 — condensed reference

A practical summary of the **Open Knowledge Format** for contributors to this repo.

- Authoritative spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf (`SPEC.md`)
- Community tooling: https://github.com/xSAVIKx/okf-skills

OKF is an open, vendor-neutral format for knowledge: a directory of Markdown files with YAML frontmatter. No schema registry, no required tooling. If you can `cat` a file you can read it; if you can `git clone` it you can ship it.

## Terms

- **Bundle** — a self-contained directory tree of concept docs. The unit of distribution (here: `bundles/local-seo/`).
- **Concept** — one markdown document = one unit of knowledge.
- **Concept ID** — the file path within the bundle minus `.md` (e.g. `maps/geo-grid-tracking.md` → `maps/geo-grid-tracking`).

## Concept document

YAML frontmatter (`---` delimited) + markdown body.

Frontmatter keys:

- `type` — **REQUIRED**, non-empty string. Not centrally registered; pick descriptive values (this repo uses `Ranking Dimension`, `Maps Analysis`, `Detection Method`, `Playbook`, `Reference`, `Concept`). Consumers must tolerate unknown types.
- `title` — recommended display name.
- `description` — recommended one-line summary (used in index snippets / search).
- `resource` — optional canonical URI of the underlying asset (omit for abstract concepts).
- `tags` — optional list.
- `timestamp` — optional ISO-8601 last-modified.
- Producers MAY add any extra keys; consumers MUST preserve unknown keys and MUST NOT reject unknown ones.

Conventional body headings (use when applicable): `# Schema`, `# Examples`, `# Citations`.

## Cross-linking

- Standard markdown links. **Absolute (bundle-relative)** preferred: begin with `/`, e.g. `[reviews](/local-seo/reviews-reputation.md)`.
- A link asserts an untyped relationship; the prose conveys the kind.
- Consumers MUST tolerate broken links (they may be not-yet-written knowledge).

## Reserved filenames (any level)

- `index.md` — directory listing for progressive disclosure. **No frontmatter**, EXCEPT the bundle-root `index.md` MAY carry an `okf_version` key. Body is sections of `* [Title](url) - description` bullets.
- `log.md` — optional chronological update history, newest first, ISO date headings.

These two names MUST NOT be used for concept documents.

## Conformance (v0.1)

A bundle is conformant if:

1. Every non-reserved `.md` has a parseable YAML frontmatter block.
2. Every frontmatter block has a non-empty `type`.
3. `index.md` / `log.md` follow their structures when present.

Consumers treat everything else as soft guidance and MUST NOT reject a bundle for: missing optional fields, unknown `type` values, unknown extra keys, broken cross-links, or missing `index.md`.

The bundle root `index.md` MAY declare `okf_version: "0.1"`.

## Validate

The canonical validator in this repo is `tool/okf_build.py` — it checks conformance, prints a concept-type breakdown and any broken links, and regenerates `viz.html`:

```bash
python3 tool/okf_build.py bundles/local-seo --name "Local SEO OKF"
```

For a quick, dependency-free check of any bundle, this standalone snippet prints `CONFORMANT v0.1: True/False` (point `B` at the bundle):

```python
import re, yaml
from pathlib import Path
B = Path("bundles/local-seo")
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RES = {"index.md", "log.md"}
ids = {str(p.relative_to(B).with_suffix("")).replace("\\","/")
       for p in B.rglob("*.md") if p.name not in RES}
LINK = re.compile(r"\]\((/[^)]+\.md)\)")
fail_fm=[]; fail_type=[]; idx_fm=[]; root_ok=True; broken=0
for p in sorted(B.rglob("*.md")):
    rel = str(p.relative_to(B)).replace("\\","/"); txt = p.read_text(encoding="utf-8")
    if p.name == "index.md":
        m = FM.match(txt)
        if m and rel != "index.md": idx_fm.append(rel)   # only root index may carry frontmatter
        continue
    if p.name == "log.md": continue
    m = FM.match(txt)
    if not m: fail_fm.append(rel); continue
    try: fm = yaml.safe_load(m.group(1)) or {}
    except Exception: fail_fm.append(rel); continue
    if not str(fm.get("type","")).strip(): fail_type.append(rel)
    for mm in LINK.finditer(txt):
        if mm.group(1).lstrip("/")[:-3] not in ids: broken += 1
ok = not fail_fm and not fail_type
print("fm_parse_fail:", fail_fm[:3], "| missing_type:", fail_type[:3])
print("broken_in_bundle_links:", broken, "(allowed, informational)")
print("CONFORMANT v0.1:", ok)
```

Requires Python 3 + PyYAML (`pip install pyyaml`). Broken in-bundle links are allowed by the spec — they flag not-yet-written knowledge, not a conformance failure.
