# OKF v0.2 — condensed reference

A practical summary of the **Open Knowledge Format** for contributors to this repo.

- Authoritative spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf (`SPEC.md`)
- Community tooling: https://github.com/xSAVIKx/okf-skills

OKF is an open, vendor-neutral format for knowledge: a directory of Markdown files with YAML frontmatter. No schema registry, no required tooling. If you can `cat` a file you can read it; if you can `git clone` it you can ship it.

## What changed in v0.2

v0.2 is a minor version bump with **two deliberate breaking changes** (spec §13.1). Both applied to this bundle:

| v0.1 | v0.2 | Note |
|---|---|---|
| `timestamp: <ISO>` | `generated: { by, at }` | The last content change now records *who* as well as *when*. |
| body `# Citations` list | `sources:` frontmatter | Provenance moves out of the body and becomes queryable. |

A v0.2 consumer MAY still fall back to a legacy `timestamp`, and SHOULD still parse a legacy `# Citations` list when it meets a v0.1 bundle. This repo's verifier rejects both, because the migration here is complete.

Everything else in v0.2 is additive: the `sources` / `generated` / `verified` / `status` / `stale_after` families, the `Attested Computation` type with its computation keys, the `# Computation` heading, and the actor convention.

## Terms

- **Bundle** — a self-contained directory tree of concept docs. The unit of distribution (here: `bundles/local-seo/`).
- **Concept** — one markdown document = one unit of knowledge.
- **Concept ID** — the file path within the bundle minus `.md` (e.g. `maps/geo-grid-tracking.md` → `maps/geo-grid-tracking`).

## Concept document

YAML frontmatter (`---` delimited) + markdown body.

Core frontmatter keys:

- `type` — **REQUIRED**, non-empty string. Not centrally registered by OKF; consumers must tolerate unknown types. This repo uses a **controlled vocabulary** (see "Type vocabulary" below) and the verifier warns on values outside it.
- `title` — recommended display name.
- `description` — recommended one-line summary (used in index snippets / search).
- `resource` — optional canonical URI of the underlying asset (omit for abstract concepts).
- `tags` — optional list.
- Producers MAY add any extra keys; consumers MUST preserve unknown keys and MUST NOT reject unknown ones.

Conventional body headings (use when applicable): `# Schema`, `# Examples`, `# Computation`.

## Provenance: `sources` (§5.1)

Every knowledge doc in this repo carries `sources`; the verifier enforces it (governance `Policy` and `Report` docs are exempt).

```yaml
sources:
  - id: whitespark-2026                       # SHOULD be present when the body cites it
    resource: /references/whitespark-2026.md  # REQUIRED: URL, /bundle-path, or scope descriptor
    title: Whitespark Local Search Ranking Factors
```

`id` values must be unique within a document. To attribute one specific claim, use a markdown footnote whose label **is** the `id`:

```markdown
The primary category is the strongest single setting.[^whitespark-2026]
```

The label is the join key into `sources` — keyed, not positional, so reordering the list can't silently misattribute a claim. The verifier fails any `[^label]` with no matching `sources[].id`.

Optional per-source credibility signals are `author`, `usage_count` (framed by a sibling `usage_window`), and `last_modified`. **`last_modified` means when the source itself last changed** — it is not the same as this repo's `accessed`, so don't write one as the other.

Note that OKF deliberately stores no credibility *score*, on the grounds that a score is subjective and goes stale. This repo's `confidence` field on `Reference` docs (below) predates v0.2 and is kept as a producer extension, not an OKF field.

## Trust: `generated` and `verified` (§5.2)

```yaml
generated: { by: human:craigburton, at: 2026-06-25T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-06T00:00:00Z }
```

- `generated` — how the current content was produced. `by` is REQUIRED; `at` marks the last meaningful content change.
- `verified` — a list of confirmation events, each `{ by, at }`. A single verifier MAY be written as a bare mapping; consumers MUST treat it as a one-element list. Multiple entries capture independent checks.
- The two are independent: content can change without re-confirmation, and facts can be re-confirmed without regeneration.

**Actor convention (§7)** — `human:<id>` for a person, `process:<id>` for an automated process, `<producer>/<version>` for an agent or tool. The `human:` prefix is what drives the top trust tier, so it MUST be used for hand-authored or human-confirmed content.

**Trust tiers (§5.3)**, derived from `verified` alone:

| `verified` | Tier |
|---|---|
| absent | unverified |
| non-`human:` actors only | machine-confirmed |
| includes a `human:<id>` actor | human-reviewed |

Only claim `verified` where a documented pass exists. In this bundle that means a dated [verification report](/bundles/local-seo/references/) or, for a `Reference`, its own recorded `accessed` date. Concepts with no documented pass carry no `verified` key and read as unverified — that absence is a real signal, not an omission to be filled in.

## Lifecycle: `status` and `stale_after` (§5.4–5.5)

```yaml
status: stable        # draft | stable | deprecated; absent means stable
stale_after: 2026-10-06
```

`stale_after` is an absolute `YYYY-MM-DD` date, never a relative TTL, so staleness stays a plain date comparison. In this repo it is derived from the freshness tier in [`maintenance.md`](/bundles/local-seo/maintenance.md): volatile monthly, semi-stable quarterly, durable semi-annually, counted from the last verification. `okf_verify.py` reports past-due docs but does not fail the build on them.

## Type vocabulary (this repo)

OKF leaves `type` open, but this bundle commits to a closed, documented set so the graph stays legible and the viz colour-codes meaningfully. The verifier warns on any value outside it.

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

OKF v0.2 also defines `Attested Computation` for concepts that carry a runnable, verifiable computation (`runtime`, `parameters`, `computation`, `executor`, `attester`). This bundle has no such concepts yet, so the type is not in the vocabulary above.

## Reference provenance (producer extension)

`Reference` docs carry extra frontmatter so a claim can be traced and re-checked. These are this repo's own keys, not OKF fields:

- `resource` — the **canonical URL** of the source.
- `publisher` — who published it.
- `published` — publication/edition date (`n.d.` / `living document` when undated).
- `accessed` — ISO date the maintainer last opened the source. This is also the evidence behind the doc's `verified` entry.
- `confidence` — `high` / `medium` / `low` (qualitative reliability of the claim).
- `scope` — one line on what the source does and does **not** establish.

The verifier warns when a `Reference` is missing any of these.

## Cross-linking

- Standard markdown links. **Absolute (bundle-relative)** preferred: begin with `/`, e.g. `[reviews](/local-seo/reviews-reputation.md)`.
- A link asserts an untyped relationship; the prose conveys the kind.
- A `sources[].resource` pointing at another concept is a derivation edge — OKF has no separate lineage field.
- Consumers MUST tolerate broken links (they may be not-yet-written knowledge).

## Reserved filenames (any level)

- `index.md` — directory listing for progressive disclosure. **No frontmatter**, EXCEPT the bundle-root `index.md` MAY carry an `okf_version` key. Body is sections of `* [Title](url) - description` bullets.
- `log.md` — optional chronological update history, newest first, ISO date headings.

These two names MUST NOT be used for concept documents.

## Conformance (v0.2)

A bundle is conformant if:

1. Every non-reserved `.md` has a parseable YAML frontmatter block.
2. Every frontmatter block has a non-empty `type`.
3. `index.md` / `log.md` follow their structures when present.

Where the trust, lifecycle, provenance or computation families are present, consumers:

- MUST treat a bare `verified` mapping as a one-element list.
- MUST NOT reject a concept for missing any optional family.
- SHOULD derive trust tiers and staleness only from the specified fields.

Consumers treat everything else as soft guidance and MUST NOT reject a bundle for: missing optional fields, unknown `type` values, unknown extra keys, broken cross-links, or missing `index.md`.

The bundle root `index.md` declares `okf_version: "0.2"`.

## Validate

Two tools in this repo:

- `tool/okf_build.py` — checks conformance, prints a concept-type breakdown and any broken links, and regenerates `viz.html` (which renders `sources` and the trust tier per concept).
- `tool/okf_verify.py` — a stricter, dependency-free quality gate. Hard failures exit non-zero.

```bash
python3 tool/okf_build.py  bundles/local-seo --name "Local SEO OKF"
python3 tool/okf_verify.py bundles/local-seo                     # offline checks
python3 tool/okf_verify.py bundles/local-seo --check-urls        # also probe external links
python3 tool/okf_verify.py bundles/local-seo --show-unverified   # list the unverified tier
```

`okf_verify.py` hard-fails on: unparseable frontmatter, empty `type`, malformed `generated` / `verified` (including actor-convention violations), `status` outside the vocabulary, a non-date `stale_after`, missing `sources`, a `sources` entry with no `resource` or `id`, duplicate source ids, a footnote with no matching source id, broken internal links, stale draft markers, `audience: internal`, and any surviving v0.1 `timestamp` or `# Citations`. It warns on out-of-vocabulary types, incomplete `Reference` provenance, orphans, past-due `stale_after`, and unreachable URLs.

For a quick, dependency-free conformance check of any bundle, this standalone snippet prints `CONFORMANT v0.2: True/False` (point `B` at the bundle):

```python
import re, yaml
from pathlib import Path
B = Path("bundles/local-seo")
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RES = {"index.md", "log.md"}
ids = {str(p.relative_to(B).with_suffix("")).replace("\\","/")
       for p in B.rglob("*.md") if p.name not in RES}
LINK = re.compile(r"\]\((/[^)]+\.md)\)")
fail_fm=[]; fail_type=[]; idx_fm=[]; broken=0; tiers={}
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
    v = fm.get("verified")
    v = v if isinstance(v, list) else ([v] if v else [])
    tier = ("human-reviewed" if any(str(e.get("by","")).startswith("human:") for e in v)
            else "machine-confirmed" if v else "unverified")
    tiers[tier] = tiers.get(tier, 0) + 1
    for mm in LINK.finditer(txt):
        if mm.group(1).lstrip("/")[:-3] not in ids: broken += 1
ok = not fail_fm and not fail_type
print("fm_parse_fail:", fail_fm[:3], "| missing_type:", fail_type[:3])
print("broken_in_bundle_links:", broken, "(allowed, informational)")
print("trust tiers:", tiers)
print("CONFORMANT v0.2:", ok)
```

Requires Python 3 + PyYAML (`pip install pyyaml`). Broken in-bundle links are allowed by the spec — they flag not-yet-written knowledge, not a conformance failure.
