---
type: Maps Analysis
title: Schema Generation
description: Generate LocalBusiness JSON-LD markup from collected maps and business data.
tags: [maps, schema, json-ld]
tier: 0
generated: { by: human:craigburton, at: 2026-06-24T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
stale_after: 2027-01-27
sources:
  - id: schema-org-localbusiness
    resource: /references/schema-org-localbusiness.md
    title: Schema.org — LocalBusiness
  - id: google-search-central-local-business-localbusiness
    resource: /references/google-local-business-structured-data.md
    title: Google Search Central — Local Business (LocalBusiness) structured data
  - id: google-search-central-review-snippet-structured
    resource: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
    title: Google Search Central — Review snippet structured data (self-serving review policy)
    last_modified: 2026-07-24
---

Generate LocalBusiness JSON-LD from collected data. See [local schema markup](/local-seo/local-schema.md) for the audit-side view and industry subtypes.

# Workflow

1. Determine the most specific schema subtype for the industry (see [industry vertical detection](/local-seo/industry-vertical-detection.md)).
2. Populate required properties: `name`, `address` — Google's only two required LocalBusiness properties. Always set `@type` to the correct subtype (a schema.org syntax requirement, not a separate Google property). `image` is not required for LocalBusiness — add it if available, but don't block generation on it.
3. Add recommended properties: `telephone`, `url`, `geo`, `openingHoursSpecification`, `priceRange`.
4. Add multi-location properties where relevant: `branchOf`, `areaServed`, `sameAs`.
5. Add `aggregateRating` if review data is available.
6. Output a valid JSON-LD block ready to implement.

# Example

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Example Co",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1 High Street",
    "addressLocality": "Manchester",
    "postalCode": "M1 1AA",
    "addressCountry": "GB"
  },
  "telephone": "+44-161-000-0000",
  "url": "https://example.co.uk",
  "geo": { "@type": "GeoCoordinates", "latitude": 53.48095, "longitude": -2.23743 }
}
```

> Do **not** generate self-serving review markup — Google ignores LocalBusiness review markup from the business itself. Only mark up third-party reviews visible on the page.

# Provenance

This method generates markup against the in-bundle [local schema markup](/local-seo/local-schema.md) dimension. Authoritative definitions:
