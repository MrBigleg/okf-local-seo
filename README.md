# Local SEO OKF

A public, agent-readable Local SEO and maps-intelligence knowledge base in
[Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf).
The canonical knowledge is plain Markdown with YAML frontmatter, maintained in
public so practitioners and agents can inspect sources and propose corrections.

RankinMaps consumes a pinned, validated snapshot of this repository. General
Local SEO knowledge belongs here; RankinMaps product documentation, private
operations, admin material, and customer Second Brains do not.

## Repository layout

```text
okf-local-seo/
├── bundles/local-seo/          # canonical Local SEO OKF bundle
│   ├── index.md                # root map (OKF v0.1)
│   ├── log.md                  # dated editorial changelog
│   ├── maintenance.md          # ownership and freshness policy
│   ├── agentic/                # AI, Maps, and commerce changes
│   ├── gbp/                    # Google Business Profile guidance
│   ├── local-seo/              # ranking and on-page concepts
│   ├── maps/                   # maps analysis and capability tiers
│   ├── playbooks/              # repeatable procedures
│   ├── references/             # evidence and provenance
│   └── viz.html                # generated interactive graph
├── bundles/minimal/            # small teaching bundle
├── docs/                       # producer and consumer documentation
└── tool/                       # dependency-free build and verification tools
```

## Read and use the bundle

Start with [`bundles/local-seo/index.md`](bundles/local-seo/index.md), follow a
section index, then load only the concepts needed for the task. This progressive
disclosure pattern keeps agent context small. Each substantive concept carries
citations, while reference pages record publisher, publication/access dates,
confidence, and scope.

Open [`bundles/local-seo/viz.html`](bundles/local-seo/viz.html) locally for the
self-contained interactive graph. The files can also be mounted directly in an
agent workspace, imported into a documentation system, or cloned as ordinary
Git content.

## Validate a change

```bash
python tool/okf_verify.py bundles/local-seo
python tool/okf_verify.py bundles/local-seo --check-urls
python tool/okf_build.py bundles/local-seo --name "Local SEO OKF"
git diff --exit-code -- bundles/local-seo/viz.html
```

The first command is the hard structural and provenance gate. URL probing is a
review signal because publishers sometimes block automated requests. The graph
must be regenerated whenever concept content or links change.

## Contribute

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md)
before proposing a change. Every factual update must identify its source and
scope; volatile product claims require a current primary source. Automation may
open a weekly draft maintenance PR, but a human must verify and approve claims
before merge.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Craig Burton. Third-party
attributions are recorded in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
