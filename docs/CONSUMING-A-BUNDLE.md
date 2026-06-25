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

Each concept ends with a `# Citations` block of primary-source links. When an agent answers from a concept, surface those sources alongside the answer — it makes the response auditable.

## Track freshness

- `timestamp` per concept = when that knowledge was last touched.
- `bundles/<name>/log.md` = a dated changelog for the whole bundle.

Use both as change signals — e.g. re-verify concepts older than N months, or diff the log since your last sync.

## Read it as a graph

Cross-links (`[text](/folder/concept.md)`) form a concept graph richer than the folder tree. Open `bundles/<name>/viz.html` for an interactive force-directed view (search, type filter, layouts, "cited by" backlinks) — a self-contained file, no backend.

## Use it in existing tools

- **Obsidian / Notion** — open the bundle as a vault/import; bundle-relative links resolve.
- **MkDocs / Hugo / Docusaurus** — point a static-site generator at the bundle; markdown + frontmatter render natively.
- **An LLM/agent** — mount the folder and follow the progressive-disclosure flow above.
