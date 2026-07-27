---
type: Ranking Dimension
title: Local Schema Markup
description: LocalBusiness JSON-LD with the correct industry subtype — not a ranking factor, but it helps search and AI parse the business.
tags: [local-seo, schema, json-ld, ranking-factors]
generated: { by: human:craigburton, at: 2026-06-25T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
stale_after: 2027-01-27
sources:
  - id: whitespark-2026
    resource: /references/whitespark-2026.md
    title: Whitespark Local Search Ranking Factors
  - id: google-search-central-local-business-localbusiness
    resource: /references/google-local-business-structured-data.md
    title: Google Search Central — LocalBusiness structured data
  - id: schema-org-localbusiness
    resource: /references/schema-org-localbusiness.md
    title: Schema.org — LocalBusiness
---

Structured data is **not** a direct ranking factor (Google's own line), but it can earn rich results and, increasingly, it helps AI systems read your business facts cleanly. Worth getting right; not worth over-claiming.

# What to check

* LocalBusiness JSON-LD present (extract the blocks).
* Required: `name`, `address` with `PostalAddress` sub-properties.
* Recommended: `geo` (use real lat/long with several decimal places), `openingHoursSpecification`, `telephone`, `url`, `image`, and `aggregateRating` where genuine.
* **Correct subtype for the industry** (see [industry vertical detection](/local-seo/industry-vertical-detection.md)) — e.g. `Restaurant`, `LegalService`, `Dentist`, `AutoDealer`, rather than a generic `LocalBusiness`.
* Service-area businesses: use `areaServed` with named places instead of a street address.
* Multi-location: each page gets its own LocalBusiness with a unique `@id`, linked via `branchOf` to the Organization on the homepage.

# Scoring guide

| Level | Criteria |
|-------|----------|
| Full | Correct subtype, recommended properties present, valid JSON-LD. |
| Partial | Present but generic type or missing recommended properties. |
| Low | No local schema, or schema with errors/placeholder content. |

# Related

Generate ready-to-paste JSON-LD via [maps schema generation](/maps/schema-generation.md). Don't mark up your own self-serving reviews — Google ignores LocalBusiness review markup that comes from the business itself.
