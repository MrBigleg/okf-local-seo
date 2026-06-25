---
type: Maps Analysis
title: Competitor Radius Mapping
description: Identify and analyse competitors within a defined radius, free via Overpass or richer via DataForSEO.
tags: [maps, competitors, radius]
tier: 0
timestamp: 2026-06-24T00:00:00Z
---

Identify and analyse competitors within a defined radius. Available from [Tier 0](/maps/capability-tiers.md).

# Tier 0 (Overpass API)

1. Geocode the business address.
2. Query Overpass for businesses with the same OSM tag within the radius.
3. Parse name, address, phone, website, and distance from centre.
4. Sort by distance and present as a competitor landscape table.

# Tier 1 (DataForSEO)

1. Use the Maps SERP API with the business keyword + location.
2. Extract the top 20 competitors with full profile data.
3. Compare rating, review count, categories, photos, and attributes.
4. Calculate a competitive density score (competitors per km²).

# Citations

[1] [DataForSEO](/references/dataforseo.md)
