---
type: Reference
title: Google Search Central — LocalBusiness structured data
description: Google's required and recommended LocalBusiness structured-data properties, and its ranking-vs-rich-results distinction.
resource: https://developers.google.com/search/docs/appearance/structured-data/local-business
publisher: Google (Search Central)
published: living document
accessed: 2026-11-16
confidence: high
scope: The only two required LocalBusiness properties (name, address) and the recommended set (telephone, url, geo, openingHoursSpecification, priceRange, aggregateRating, review, department, menu, servesCuisine). Does not itself state the ranking-vs-rich-results distinction — see the companion General Structured Data Guidelines page for that. Field/property names on this page can drift with Google's documentation updates.
tags: [reference, schema, structured-data, google]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
verified:  { by: anthropic/claude-fable-5-2, at: 2026-11-16T00:00:00Z }
status: stable
stale_after: 2027-02-16
sources:
  - id: google-search-central-local-business-localbusiness
    resource: https://developers.google.com/search/docs/appearance/structured-data/local-business
    title: Google Search Central — Local Business (LocalBusiness) structured data
  - id: google-search-central-general-structured-data-guidelines
    resource: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
    title: Google Search Central — General Structured Data Guidelines
---

Google's structured-data reference for the `LocalBusiness` type. Used as the primary source in [Local Schema Markup](/local-seo/local-schema.md) and [Schema Generation](/maps/schema-generation.md).

# What the source establishes

* Only `name` and `address` are required. Everything else — `telephone`, `url`, `geo`, `openingHoursSpecification`, `priceRange`, `aggregateRating`, `review`, `department`, `menu`, `servesCuisine` — is recommended, not required. `image` appears in neither list for `LocalBusiness`.
* Per the companion [General Structured Data Guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) page: structured data enables eligibility for a rich-result feature, it does not guarantee the feature appears, and a structured data manual action "doesn't affect how the page ranks in Google web search" — it removes rich-result eligibility, not ranking position.
