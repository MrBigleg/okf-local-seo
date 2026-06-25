# okf-local-seo

A portable, agent-readable **local SEO & maps intelligence** knowledge base in [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) — plain markdown with YAML frontmatter, organised as a hierarchy of cross-linked concepts.

No database, no SDK, no lock-in. If you can `cat` a file you can read it; if you can `git clone` it you can ship it. Humans, agents, and static-site tools all read the same files.

> **Status:** private review → public. Human-review the content (see *Provenance* below) before flipping the repo public.

## What's inside

```
okf-local-seo/
├── bundle/                     # the OKF bundle (the actual knowledge)
│   ├── index.md                # root listing (declares okf_version: 0.1)
│   ├── log.md                  # dated changelog
│   ├── local-seo/              # ranking dimensions + detection + AI-search
│   ├── maps/                   # geo-grid, GBP audit, reviews, NAP, schema, tiers
│   ├── references/             # primary sources (each claim is cited)
│   └── playbooks/              # repeatable procedures
├── okf_build.py                # validator + viz.html generator (no dependencies)
├── LICENSE                     # MIT — Copyright (c) 2026 Craig Burton
└── README.md
```

25 concepts, fully conformant to OKF v0.1.

## Use it

**As an agent context source.** Point any LLM/agent at `bundle/`. The frontmatter (`type`, `tags`, `resource`) gives agents fields to filter on; the per-folder `index.md` files allow progressive disclosure — an agent can see what's available before loading everything into context.

**As a docs site.** MkDocs / Hugo / Docusaurus read markdown + frontmatter natively — point one at `bundle/`.

**As an interactive graph.** Open `bundle/viz.html` in any browser — a self-contained, force-directed graph of every concept and cross-link. No backend.

**In Obsidian / Notion.** Open `bundle/` as a vault; the `/absolute/path.md` cross-links work as-is.

## Validate & regenerate the viewer

```bash
python3 okf_build.py bundle --name "Local SEO OKF"
```

Prints a conformance check (OKF v0.1), a concept-type breakdown, and any broken links (allowed — they may be not-yet-written knowledge), then rewrites `bundle/viz.html`. Re-run it whenever the bundle grows.

## Grow it

1. Add a `.md` file under the right folder in `bundle/`. Minimum frontmatter:

   ```markdown
   ---
   type: Playbook
   title: Review response templates
   description: One-line summary.
   tags: [local-seo, reviews]
   timestamp: 2026-06-25T00:00:00Z
   ---
   # Body…
   ```

   Only `type` is required.
2. Cross-link with bundle-relative links: `[reviews](/local-seo/reviews-reputation.md)`.
3. Update the folder's `index.md` and add a `log.md` line.
4. Re-run `okf_build.py`.

## Agentic-tool integration (notes for the PoC)

Because the bundle is just files, an agent tool can consume it without bespoke parsing:

- **Retrieval:** load `bundle/index.md` first, then fetch only the concept files an agent needs (progressive disclosure keeps context small).
- **Filtering:** parse frontmatter `type`/`tags` to route or scope retrieval.
- **Citation:** each concept ends with a `# Citations` block of primary-source links, so an agent can surface sources with its answer.
- **Freshness:** `timestamp` per concept and `bundle/log.md` give you change signals.

## Provenance & verification

The structure and topic map were *inspired by* the local-SEO and maps skills in the MIT-licensed [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) repo. The concept docs here are **independently rewritten** and every figure has been **checked against its primary source**; unverifiable figures were dropped. Sources include Whitespark, Sterling Sky, BrightLocal, Ahrefs, Seer Interactive, and Google Search Central — see `bundle/references/`.

**Before going public:** sanity-check the content (the source repo carried March 2026-dated stats) and confirm the exact live URL of Google's AI-features documentation, which is flagged in `bundle/references/google-ai-optimization-guide.md`.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Craig Burton.
