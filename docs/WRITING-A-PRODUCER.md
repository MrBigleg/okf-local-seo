# Writing an OKF producer

A **producer** turns a source — a database, a file tree, an API, a wiki, a spreadsheet — into an OKF bundle. This guide is the on-ramp for adding a new one.

## The pattern (five steps)

1. **Enumerate** the units of knowledge in your source (tables, endpoints, articles, factors…). Each becomes one concept document.
2. **Map** each unit to a concept: choose a descriptive `type`, write a one-line `description`, set `resource` if it points at a real asset.
3. **Write the body** as structured markdown — headings, tables, lists, fenced code. Structure aids both human reading and agent retrieval.
4. **Cross-link** related concepts with bundle-relative links: `[text](/folder/concept.md)`. Links express the graph the directory tree can't.
5. **Generate** the navigation: an `index.md` per directory (root carries `okf_version: "0.1"`) and an optional `log.md`. Then validate.

## Two design rules worth keeping

- **Deterministic extraction.** Re-running a producer on an unchanged source should be a no-op (same bytes out). Keep the mechanical extraction free of an embedded LLM; if you want grounded prose, let an agent enrich the bundle as a separate, reviewable pass.
- **Frontmatter is the queryable surface; the body is for reading.** Put the few fields you'll filter or route on (`type`, `tags`, `resource`, `timestamp`) in frontmatter; put everything humans and agents actually read in the body.

## Minimal producer skeleton (Python)

```python
import datetime as dt, yaml
from pathlib import Path

OUT = Path("bundles/example")

def write_concept(relpath, fm, body):
    p = OUT / relpath
    p.parent.mkdir(parents=True, exist_ok=True)
    y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    p.write_text(f"---\n{y}\n---\n\n{body.strip()}\n", encoding="utf-8")

for item in enumerate_source():            # <- your source here
    write_concept(
        f"{item.group}/{item.slug}.md",
        {"type": item.type, "title": item.title,
         "description": item.one_liner,
         "tags": item.tags,
         "timestamp": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")},
        item.markdown_body,                # include bundle-relative [links](/g/other.md)
    )
# then generate index.md per dir + a root index.md with okf_version: "0.1"
```

## Worked examples

- **Files / DB / Git / BigQuery** — the community connectors at [`xSAVIKx/okf-skills`](https://github.com/xSAVIKx/okf-skills) are single-purpose binaries that `produce` a bundle and `ingest` descriptions back. Study their `produce`/`ingest`/`schema` command surface.
- **Obsidian vault → OKF** — the `wiki-export-okf` skill in Craig's `claude-obsidian` plugin is a working producer: it selects pages by tag, rewrites `[[wikilinks]]` to bundle-relative links, normalises frontmatter, and emits index/log. That's the feeder used to draft content for this repo before hand-curation.

## Validate as you go

```bash
python3 tool/okf_build.py bundles/example --name "Example"
```

See [`OKF-SPEC-SUMMARY.md`](OKF-SPEC-SUMMARY.md) for the conformance rules and a standalone check.
