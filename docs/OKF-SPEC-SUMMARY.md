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

- `type` — **REQUIRED**, non-empty string. Not centrally registered by OKF; consumers must tolerate unknown types. This repo uses a **controlled vocabulary** (see "Type vocabulary" below) and the verifier warns on values outside it.
- `title` — recommended display name.
- `description` — recommended one-line summary (used in index snippets / search).
- `resource` — optional canonical URI of the underlying asset (omit for abstract concepts).
- `tags` — optional list.
- `timestamp` — optional ISO-8601 last-modified.
- Producers MAY add any extra keys; consumers MUST preserve unknown keys and MUST NOT reject unknown ones.

Conventional body headings (use when applicable): `# Schema`, `# Examples`, `# Citations`. Every concept doc in this repo carries a `# Citations` block; the verifier enforces it.

## Type vocabulary (this repo)

OKF leaves `type` open, but this bundle commits to a closed, documented set so the graph stays legible and the viz colour-codes meaningfully. The verifier (`tool/okf_verify.py`) warns on any value outside it.

| Tier | Type | Meaning |
|---|---|---|
| Knowledge | `Concept` | Explains an idea, mechanism or practice. |
| Knowledge | `Ranking Dimension` | A category of signal that influences local ranking/visibility. |
| Knowledge | `Maps Analysis` | A repeatable analysis technique over maps/GBP data. |
| Knowledge | `Detection Method` | A heuristic for classifying a site or business. |
| Knowledge | `Playbook` | An ordered, actionable procedure or checklist. |
| Source | `Reference` | A pointer to a single external primary source, with provenance frontmatter. |
| Governance | `Policy` | A maintenance or governance rule for the bundle itself. |
| Governance | `Report` | A dated record of a verification or audit pass. |

## Reference provenance

`Reference` docs carry provenance frontmatter so a claim can be traced and re-checked:

- `resource` — the **canonical URL** of the source.
- `publisher` — who published it.
- `published` — publication/edition date (`n.d.` / `living document` when undated).
- `accessed` — ISO date the maintainer last opened the source.
- `confidence` — `high` / `medium` / `low` (qualitative reliability of the claim).
- `scope` — one line on what the source does and does **not** establish.

The verifier warns when a `Reference` is missing any of these.

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

Two tools in this repo:

- `tool/okf_build.py` — checks v0.1 conformance, prints a concept-type breakdown and any broken links, and regenerates `viz.html`.
- `tool/okf_verify.py` — a stricter, dependency-free quality gate. It checks frontmatter + non-empty type, the type vocabulary above, broken internal links (absolute and relative), `# Citations` presence, sequential citation numbering, reference provenance completeness, stale draft markers, orphaned documents, and (with `--check-urls`) external URL reachability. Hard failures exit non-zero.

```bash
python3 tool/okf_build.py  bundles/local-seo --name "Local SEO OKF"
python3 tool/okf_verify.py bundles/local-seo                 # offline checks
python3 tool/okf_verify.py bundles/local-seo --check-urls    # also probe external links
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
