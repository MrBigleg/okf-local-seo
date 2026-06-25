---
type: Maps Analysis
title: Schema Generation
description: Generate LocalBusiness JSON-LD markup from collected maps and business data.
tags: [maps, schema, json-ld]
tier: 0
timestamp: 2026-06-24T00:00:00Z
---

Generate LocalBusiness JSON-LD from collected data. See [local schema markup](/local-seo/local-schema.md) for the audit-side view and industry subtypes.

# Workflow

1. Determine the most specific schema subtype for the industry (see [industry vertical detection](/local-seo/industry-vertical-detection.md)).
2. Populate required properties: `@type`, `name`, `address`, `image`.
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

# Citations

This method generates markup against the in-bundle [local schema markup](/local-seo/local-schema.md) dimension. Authoritative definitions:

[1] [Schema.org — LocalBusiness](https://schema.org/LocalBusiness)

[2] [Google Search Central — Local Business (LocalBusiness) structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business)

[3] [Google Search Central — Review snippet structured data (self-serving review policy)](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
