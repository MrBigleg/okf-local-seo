---
type: Concept
title: Cross-linking
description: Concepts link to each other with bundle-relative markdown links, forming a graph.
tags: [okf, tutorial]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
    title: Open Knowledge Format specification (v0.2)
---

Concepts relate to each other through ordinary markdown links.

# Bundle-relative links (preferred)

Start the path with `/`, relative to the bundle root:

```markdown
See [concept anatomy](/guide/concept-anatomy.md).
```

This renders as: see [concept anatomy](/guide/concept-anatomy.md).

# Why it matters

The directory tree only expresses parent/child. Links express every other relationship — and a consumer can build a graph from them. Broken links are allowed; they simply mark knowledge not yet written.

# Links as lineage

A `sources` entry may point at another concept in the same bundle instead of an external URL:

```yaml
sources:
  - id: anatomy
    resource: /guide/concept-anatomy.md
    title: Concept anatomy
```

That is a derivation edge, so a consumer can walk into that concept's own `sources` and let credibility propagate.[^okf-spec] OKF has no dedicated lineage field; the link *is* the lineage.
