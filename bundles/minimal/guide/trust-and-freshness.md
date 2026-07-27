---
type: Concept
title: Trust and freshness
description: The v0.2 provenance, trust and lifecycle families let a reader judge where a concept came from and whether it is still current.
tags: [okf, tutorial, trust]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
    title: Open Knowledge Format specification (v0.2)
  - id: anatomy
    resource: /guide/concept-anatomy.md
    title: Concept anatomy
---

OKF v0.2 adds three optional frontmatter families that answer three questions: where did this come from, how much should I trust it, and is it still current.[^okf-spec] All of them are optional, and every one of them is absent from a plain v0.1 concept.

# Provenance: `sources`

`sources` lists the material a concept derives from. Only `resource` is required inside an entry, but give each one an `id` when the body cites it:

```yaml
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
    title: Open Knowledge Format specification (v0.2)
```

To attribute one specific claim, use a markdown footnote whose label is the `id`:

```markdown
Only `type` is required.[^okf-spec]
```

The label is the join key. It is keyed rather than positional (`sources[0]`) because agents rewrite these documents constantly, and a positional index misattributes silently the moment the list is reordered.

# Trust: `generated` and `verified`

Who *wrote* a concept need not be who *confirmed* it, so the two are recorded separately:

```yaml
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
verified:  { by: human:someone,    at: 2026-07-27T00:00:00Z }
```

Identities follow one actor convention: `human:<id>` for a person, `process:<id>` for an automated process, and `<producer>/<version>` for an agent or tool.

A consumer derives a **trust tier** from `verified` alone:

| `verified` | Tier |
|---|---|
| absent | unverified |
| non-`human:` actors only | machine-confirmed |
| includes a `human:<id>` actor | human-reviewed |

Note what this document does *not* claim. It carries no `verified` key, so a consumer reads it as **unverified** — the honest signal for a teaching example nobody has fact-checked. Absence carries meaning, and an unverified concept is never rejected for it.

# Lifecycle: `status` and `stale_after`

```yaml
status: stable        # draft | stable | deprecated; absent means stable
stale_after: 2027-01-27
```

`stale_after` is an absolute date, not a relative TTL, so deciding whether a concept is stale stays a plain date comparison that does not depend on when it was read.

# What replaced what

Two v0.1 habits are retired in v0.2. A `timestamp` key becomes `generated.at`, and a `# Citations` body list becomes `sources`. A v0.2 consumer should still read both legacy forms when it meets an older bundle. See [concept anatomy](/guide/concept-anatomy.md) for the rest of the document shape.[^anatomy]
