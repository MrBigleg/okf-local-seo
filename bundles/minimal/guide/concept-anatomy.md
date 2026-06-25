---
type: Reference
title: Concept anatomy
description: A concept document is YAML frontmatter plus a markdown body; only type is required.
tags: [okf, tutorial]
timestamp: 2026-06-25T00:00:00Z
---

A **concept** is one markdown file. It has two parts.

# Frontmatter

The block between the `---` fences at the top is YAML. The only required key is `type` (a short, descriptive string). Everything else is optional but recommended: `title`, `description`, `tags`, `resource`, `timestamp`.

# Body

Everything after the frontmatter is plain markdown — headings, lists, tables, code. Favour structure over freeform prose; it helps both human readers and agents.

# Where to go next

See [cross-linking](/guide/cross-linking.md) for how this concept connects to others.
