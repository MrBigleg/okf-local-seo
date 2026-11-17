---
type: Detection Method
title: Business Type Detection
description: Classify a business as brick-and-mortar, service-area, or hybrid before running local SEO checks, including service area schema for businesses with no street address.
tags: [local-seo, detection, gbp, service-area, schema]
generated: { by: google/gemini-4-hydrogen, at: 2026-11-17T00:00:00Z }
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

# Service-area business schema

A service-area business (SAB) has no shop front or public street address — it visits or delivers to customers at their location.[^google-business-profile-help-service-area] In `LocalBusiness` JSON-LD:

* **Omit `address.streetAddress`** and use `areaServed` with named cities, `AdministrativeArea`, `Place`, or `GeoShape` values to show where the business operates.[^schema-org-localbusiness-areaserved]
* **Match GBP service areas:** align `areaServed` with the cities, postal codes, or geographic regions configured on the Google Business Profile (Google allows up to 20 service areas defined by geographic designation, not a radius).[^google-business-profile-help-service-area]
* **Hybrid businesses** (which have both a public storefront and a service area) include both their physical `address` and `areaServed`.

Note that Google Search Central's [LocalBusiness structured data](/local-seo/local-schema.md) documentation lists `name` and `address` as required for rich-result eligibility; SABs without a public address use Schema.org's `areaServed` to describe their service footprint rather than publishing a private or unverified street address. See [schema generation](/maps/schema-generation.md) for JSON-LD output.

# Provenance

A heuristic detection method derived from observable page signals; not an externally published taxonomy. Its schema implications follow Google's service-area handling:
