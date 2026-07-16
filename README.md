# Local SEO OKF

I have spent years working in Local SEO and Digital Marketing and I', methodical about collaiting information: Google documentation,
research, working methods, things that changed, and things people repeat even
though the evidence does not support them.

The biggest problem is information overload and stale understanding, keeping information
organised, sourced, current, and useful to me as a hands on SEO. 

Recently with AI being able to much better handle long context, research and verification tasks, organising. 
Understanding data became more manageble and my "second brain" has become indespensible.
Sharing is caring and since OKF became a standard that I think will revolutionise A2A and ARD discovery.
I wanted to create a next gen shared space for Local SEOs to share knowledge efficietnlty in the AI age.  

This repository is am attempt to create that. It is a public Local SEO knowledge base written
in [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf):
plain Markdown files, small indexes, links between related ideas, and sources
you can check for yourself.

You can read it. You can give it to an AI agent. Or you can copy the pattern
and build a knowledge base around your own work.



## What this gives you

- Evidence-backed guidance about Local SEO, Google Business Profiles, Maps,
  reviews, local visibility, and emerging agent workflows.
- A working example of a knowledge base that an AI can navigate without
  loading everything at once.
- A repeatable way to turn your own files, website, database, wiki, research,
  or operating procedures into structured knowledge.
- Dependency-free tools for checking the structure, sources, links, and
  generated knowledge graph.

This is not a magic database and OKF is not another platform you have to buy.
The source of truth is a folder of readable files. Git records what changed,
who changed it, and when.

## How it works

```text
Your sources
    ↓
Small Markdown knowledge pages
    ↓
Indexes, links, citations, and Git history
    ↓
Validation and human review
    ↓
People, websites, AI workspaces, or MCP connectors
```

Each meaningful subject becomes one concept page. The frontmatter says what
the page is; the body explains it; links connect it to related knowledge; and
citations show where factual claims came from.

An AI starts at `index.md`, follows the section that matches the task, and
opens only the pages it needs. This is called progressive disclosure. In plain
English: give the agent a map first, not the entire library.

## Choose how you want to use it

| Path | Best for | What you manage |
|---|---|---|
| Read or clone this bundle | Learning, research, and public Local SEO workflows | Nothing beyond keeping your copy updated |
| Build your own OKF bundle | Your own knowledge, your own rules, full control | Sources, review, updates, and where the files live |
| Connect the files to your agent | Private local workflows without a managed service | Agent access, permissions, and any MCP or search layer you add |
| Use the official RankinMaps connector | A supported connection to RankinMaps knowledge and private workflows | Your account, the agent you connect, and the actions you approve |

The open route is genuinely open. You do not need RankinMaps to use this
format or recreate the approach.

If you want the supported route, the
[official RankinMaps MCP connector](https://www.rank-in-maps.com/tools/learn/rank-in-maps-mcp)
connects compatible AI clients to the knowledge and tools available to your
RankinMaps account. A paid option is available for private workflows. Access
depends on your account and the tools currently enabled; your MCP client's
tool list is the source of truth.

MCP and OKF are not the same thing. **OKF organises the knowledge. MCP is one
way to let an AI use it.** You can replace the connector and keep the files.
That portability is the point.

## Recreate this with your own knowledge

You do not need to start with hundreds of documents. Start with ten useful
ones.

1. **Choose the source.** It might be a folder, website, database, wiki,
   spreadsheet, set of client-safe procedures, or your own notes.
2. **Split it into useful subjects.** Make each subject one Markdown file.
   Keep the title specific and the description short.
3. **Add structure.** Give each page a `type`, useful tags, and links to
   related pages. Put facts and explanation in the body.
4. **Show your evidence.** Link factual claims to the best available source.
   Record dates and limitations when the information can change.
5. **Build the map.** Add an `index.md` at the root and inside larger
   sections. The indexes help people and agents find the right page quickly.
6. **Validate and review.** Let automation find missing fields, broken links,
   and stale material. Let a human decide what is true and what gets merged.
7. **Connect it to your workflow.** Mount the folder in an AI workspace,
   import it into a documentation tool, publish it as a site, or expose
   selected search/read operations through your own MCP server.

The detailed guides are here:

- [Writing an OKF producer](docs/WRITING-A-PRODUCER.md) explains how to turn
  files, APIs, databases, wikis, or spreadsheets into a bundle.
- [Consuming an OKF bundle](docs/CONSUMING-A-BUNDLE.md) explains how an agent
  can navigate, filter, cite, and monitor it.
- [OKF v0.1 condensed reference](docs/OKF-SPEC-SUMMARY.md) covers the format
  and conformance rules.
- [The minimal bundle](bundles/minimal/) is the smallest working example.

RankinMaps uses the same pattern at a larger scale. This public repository is
the canonical Local SEO source. RankinMaps pulls a pinned, validated snapshot
rather than quietly maintaining a different copy. Its product documentation,
private operations, and customer knowledge stay outside this public
repository.

That separation matters. Open knowledge should be inspectable. Private
business knowledge should remain private.

## Read this bundle

Start with [`bundles/local-seo/index.md`](bundles/local-seo/index.md). Choose
a section, read its index, and open only the concepts relevant to your task.

You can also open [`bundles/local-seo/viz.html`](bundles/local-seo/viz.html)
locally for a self-contained interactive view of the knowledge graph. Search
it, filter by type, and follow the links between concepts.

The files can be mounted directly in an agent workspace, imported into a
documentation system, or cloned and used as ordinary Git content. No special
reader is required.

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

## Validate a change

```bash
python tool/okf_verify.py bundles/local-seo
python tool/okf_verify.py bundles/local-seo --check-urls
python tool/okf_build.py bundles/local-seo --name "Local SEO OKF"
git diff --exit-code -- bundles/local-seo/viz.html
```

The first command is the hard structural and provenance gate. URL probing is
a review signal because publishers sometimes block automated requests. The
graph must be regenerated whenever concept content or links change.

## Contribute

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md)
before proposing a change.

Every factual update must identify its source and scope. Fast-changing product
claims need a current primary source. Automation may prepare a weekly draft
maintenance pull request, but it does not decide what is true. A person must
verify and approve every claim before it is merged.

AI is a remarkable collaborator. It is not an accountable editor. Humans stay
in the loop here.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Craig Burton. Third-party
attributions are recorded in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
