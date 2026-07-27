---
type: Concept
title: Concept anatomy
description: A concept document is YAML frontmatter plus a markdown body; only type is required.
tags: [okf, tutorial]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
    title: Open Knowledge Format specification (v0.2)
---

A **concept** is one markdown file. It has two parts.

# Frontmatter

The block between the `---` fences at the top is YAML. The only required key is `type` (a short, descriptive string). A concept carrying nothing but `type` is already fully conformant.[^okf-spec]

Everything else is optional. The recommended basics are `title`, `description`, `tags` and `resource`:

```yaml
---
type: Concept
title: Concept anatomy
description: One sentence describing this concept.
tags: [okf, tutorial]
resource: https://example.com/the-underlying-asset   # omit for abstract ideas
---
```

On top of those, v0.2 adds three optional families — provenance, trust and lifecycle. They are covered in [trust and freshness](/guide/trust-and-freshness.md).

# Body

Everything after the frontmatter is plain markdown — headings, lists, tables, code. Favour structure over freeform prose; it helps both human readers and agents.

Three headings carry conventional meaning: `# Schema`, `# Examples`, and `# Computation`. No section is required. In v0.1 a `# Citations` list was the convention for provenance; in v0.2 that moves into `sources` frontmatter instead.

# Where to go next

See [cross-linking](/guide/cross-linking.md) for how this concept connects to others, and [trust and freshness](/guide/trust-and-freshness.md) for how a reader judges whether to believe it.
