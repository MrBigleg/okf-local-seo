# Consuming an OKF bundle

An OKF bundle is just files, so anything that reads markdown can consume it — no SDK, no parser. This guide covers how to do it *well*, especially from an LLM agent.

## Progressive disclosure (don't load everything)

Start at the root `index.md`, then open only what you need:

1. Read `bundles/<name>/index.md` — the top-level map (sections + descriptions).
2. Follow into a folder's `index.md` to see that group's concepts and one-line descriptions.
3. Load individual concept files only when a description matches the task.

This keeps an agent's context small. A 200-concept bundle costs a few hundred tokens to *navigate*; you pull full bodies on demand.

## Filter on frontmatter

The frontmatter is the queryable surface. Parse it to route or scope retrieval:

- `type` — route by kind (e.g. only `Playbook` for "how do I…", only `Reference` for sources).
- `tags` — scope to a sub-topic (`gbp`, `reviews`, `schema`).
- `resource` — when present, the canonical external asset the concept describes.
- `status` — skip `deprecated`, treat `draft` as provisional (absent means `stable`).
- `verified` — derive a trust tier before you rely on a claim (see below).

```python
import re, yaml
from pathlib import Path
def concepts(bundle):
    FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
    for p in Path(bundle).rglob("*.md"):
        if p.name in ("index.md","log.md"): continue
        m = FM.match(p.read_text(encoding="utf-8"))
        fm = yaml.safe_load(m.group(1)) if m else {}
        yield p, (fm or {})
# e.g. playbooks = [p for p,fm in concepts("bundles/local-seo") if fm.get("type")=="Playbook"]
```

## Surface citations

Provenance lives in the `sources` frontmatter list, not the body. Each entry has a `resource` (a URL, a bundle-relative path, or a scope descriptor) and usually an `id` and `title`. When an agent answers from a concept, surface those sources alongside the answer — it makes the response auditable.

When the body attributes a specific claim, it does so with a markdown footnote whose label is the `sources[].id`:

```markdown
The primary category is the strongest single setting.[^whitespark-2026]
```

Resolve attribution through the matching `sources` entry rather than by parsing the footnote prose. Older v0.1 bundles instead end each concept with a `# Citations` list; a tolerant consumer should read both.

## Weigh trust before you rely on a claim

Derive a tier from `verified` — absent means **unverified**, non-`human:` actors only means **machine-confirmed**, and any `human:<id>` actor means **human-reviewed**:

```python
def tier(fm):
    v = fm.get("verified") or []
    v = v if isinstance(v, list) else [v]          # a bare mapping is a one-element list
    if any(str(e.get("by","")).startswith("human:") for e in v): return "human-reviewed"
    return "machine-confirmed" if v else "unverified"
```

These are advisory signals, not access control: never reject a concept for being unverified. In this bundle, the absence of `verified` is deliberate and meaningful — it marks knowledge that no dated verification pass has covered yet.

## Track freshness

- `generated.at` per concept = when that knowledge last meaningfully changed (v0.1 bundles use `timestamp`).
- `stale_after` per concept = the date it goes stale; a concept is stale when `today >= stale_after`.
- The latest `verified[].at` = when it was last confirmed, which is independent of when it was written.
- `bundles/<name>/log.md` = a dated changelog for the whole bundle.

Use these as change signals — e.g. re-check anything past `stale_after`, or diff the log since your last sync.

## Read it as a graph

Cross-links (`[text](/folder/concept.md)`) form a concept graph richer than the folder tree. A `sources[].resource` pointing at another concept is an edge too — a derivation edge — so you can recurse into a source's own `sources` and let credibility propagate. Open `bundles/<name>/viz.html` for an interactive force-directed view (search, type filter, layouts, sources, trust tier, "cited by" backlinks) — a self-contained file, no backend.

## Use it in existing tools

- **Obsidian / Notion** — open the bundle as a vault/import; bundle-relative links resolve.
- **MkDocs / Hugo / Docusaurus** — point a static-site generator at the bundle; markdown + frontmatter render natively.
- **An LLM/agent** — mount the folder and follow the progressive-disclosure flow above.
