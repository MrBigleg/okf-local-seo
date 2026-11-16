---
type: Reference
title: Schema.org — LocalBusiness
description: The LocalBusiness type definition, its position in the type hierarchy, and its properties including areaServed.
resource: https://schema.org/LocalBusiness
publisher: Schema.org
published: living document
accessed: 2026-11-16
confidence: high
scope: The vocabulary and subtype hierarchy — LocalBusiness inherits from both Organization and Place, with more specific subtypes — plus its properties (address, geo, openingHours, priceRange, areaServed, and more). Does not establish that LocalBusiness markup is a ranking or SEO signal; the page documents structure only, not search-algorithm weight.
tags: [reference, schema, structured-data]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
verified:  { by: anthropic/claude-fable-5-2, at: 2026-11-16T00:00:00Z }
status: stable
stale_after: 2027-02-16
sources:
  - id: schema-org-localbusiness
    resource: https://schema.org/LocalBusiness
    title: Schema.org — LocalBusiness
---

The canonical Schema.org vocabulary page for `LocalBusiness`. Used as the primary source for the subtype hierarchy and `areaServed` in [Industry Vertical Detection](/local-seo/industry-vertical-detection.md), [Business Type Detection](/local-seo/business-type-detection.md), and [Schema Generation](/maps/schema-generation.md).

# What the source establishes

* `LocalBusiness` has dual inheritance from `Organization` and `Place`, and carries properties from both (e.g. `legalName`, `founder` from Organization; `geo`, `photo` from Place) plus business-specific properties like `openingHours`, `priceRange`, and `currenciesAccepted`.
* `areaServed` is defined as the geographic area where a service or offered item is provided — the property this bundle's service-area detection relies on.
* Adoption statistics (schema.org lists "1M–10M Domains") describe prevalence, not algorithmic weight; this page makes no ranking claim.
