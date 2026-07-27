---
type: Reference
title: Schema.org — LocalBusiness
description: The LocalBusiness type definition, its position in the type hierarchy, and its properties including areaServed.
resource: https://schema.org/LocalBusiness
publisher: Schema.org
published: living document
accessed: 2026-07-27
confidence: high
scope: The vocabulary and subtype hierarchy — LocalBusiness inherits from both Organization and Place, with 30+ subtypes such as Restaurant and Store — plus its properties (address, geo, openingHours, priceRange, areaServed, and more). Does not establish that LocalBusiness markup is a ranking or SEO signal; the page documents structure only, not search-algorithm weight.
tags: [reference, schema, structured-data]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
stale_after: 2026-10-27
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
