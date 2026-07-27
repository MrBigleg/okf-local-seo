---
type: Detection Method
title: Business Type Detection
description: Classify a business as brick-and-mortar, service-area, or hybrid before running local SEO checks.
tags: [local-seo, detection, gbp]
generated: { by: human:craigburton, at: 2026-06-24T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
stale_after: 2027-01-27
sources:
  - id: google-business-profile-help-service-area
    resource: /references/google-gbp-service-areas.md
    title: Google Business Profile Help — Service-area businesses on Google
  - id: schema-org-localbusiness-areaserved
    resource: https://schema.org/areaServed
    title: Schema.org — LocalBusiness `areaServed`
    last_modified: 2026-03-19
---

Detect the business type from page signals **before** analysis. The type determines which checks apply — for example, service-area businesses skip embedded-map and physical-address checks.

# Types

| Type | Signals |
|------|---------|
| **Brick-and-mortar** | Physical street address in content/footer; Google Maps embed with pin/directions; "Visit us at", "Located at"; structured address in [LocalBusiness schema](/local-seo/local-schema.md). |
| **Service Area Business (SAB)** | No visible physical address; "serving [city/region]", "we come to you", "mobile [service]"; `areaServed` in schema without `address.streetAddress`. |
| **Hybrid** | Both a physical address and service-area language; e.g. "visit our showroom" plus "we also serve [areas]". |

# Impact on checks

SABs skip embedded-map verification and physical-address consistency. Brick-and-mortar gets the full [NAP and citation](/local-seo/nap-citations.md) checks. This classification also shapes [schema generation](/maps/schema-generation.md) — SABs use `areaServed` with named cities rather than a street address.

# Provenance

A heuristic detection method derived from observable page signals; not an externally published taxonomy. Its schema implications follow Google's service-area handling:
