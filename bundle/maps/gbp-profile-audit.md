---
type: Maps Analysis
title: GBP Profile Audit
description: Score the 25 Google Business Profile fields that affect quality and ranking, with industry weighting.
tags: [maps, gbp, audit]
tier: 1
timestamp: 2026-06-24T00:00:00Z
---

Audits the 25 fields that affect GBP quality and ranking. Tier 1 uses live API data; [Tier 0](/maps/capability-tiers.md) falls back to detectable on-page signals. Complements the on-page view in [GBP signals](/local-seo/gbp-signals.md).

# Tier 1 workflow

1. Fetch the profile via the DataForSEO My Business Info API (keyword or CID).
2. Map the API response to the 25-field checklist.
3. Score each field: Present + Optimised = 2pts, Present = 1pt, Missing = 0pts.
4. Apply industry-specific weight multipliers.
5. Normalise to a 0–100 scale.

# Tier 0 workflow

1. Fetch the business website.
2. Extract visible GBP signals (Maps embed, place references, review widgets).
3. Apply the static checklist from detectable signals.
4. Mark undetectable fields as "Unknown (requires DataForSEO for live data)".

# Citations

[1] [DataForSEO](/references/dataforseo.md)
