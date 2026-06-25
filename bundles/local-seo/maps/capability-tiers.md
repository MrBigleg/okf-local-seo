---
type: Concept
title: Maps Capability Tiers
description: Three-tier capability model for maps intelligence — detect the available tier before any analysis and communicate it to the user.
tags: [maps, dataforseo, tiers]
timestamp: 2026-06-24T00:00:00Z
---

Maps intelligence analyses the business on maps **platforms** (via APIs), as opposed to [local on-page SEO](/local-seo/local-onpage.md) which analyses the **website** via HTML fetch. Detect the available tier first and always communicate it to the user.

# Tiers

| Tier | Detection | Capabilities |
|------|-----------|--------------|
| **0 — Free** | No DataForSEO MCP tools | Overpass API competitor discovery, Geoapify POI search, Nominatim geocoding, static GBP checklist, schema generation, cross-platform NAP guidance. |
| **1 — DataForSEO** | `business_data_business_listings_search` available | Tier 0 + [geo-grid rank tracking](/maps/geo-grid-tracking.md), live [GBP profile audit](/maps/gbp-profile-audit.md), [review intelligence](/maps/review-intelligence.md), GBP post/Q&A data, Tripadvisor/Trustpilot reviews. |
| **2 — DataForSEO + Google Maps** | Tier 1 + Google Maps API key | Tier 1 + Google Places details, real-time business status, AI place summaries, photo analysis. Google ToS restricts storage to `place_id`; lat/lng cached 30 days max. |

# Citations

[1] [DataForSEO](/references/dataforseo.md)
