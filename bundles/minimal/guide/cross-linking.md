---
type: Reference
title: Cross-linking
description: Concepts link to each other with bundle-relative markdown links, forming a graph.
tags: [okf, tutorial]
timestamp: 2026-06-25T00:00:00Z
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
