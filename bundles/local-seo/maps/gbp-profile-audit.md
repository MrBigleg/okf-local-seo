---
type: Maps Analysis
title: GBP Profile Audit
description: Score the 25 Google Business Profile fields that affect quality and ranking, with industry weighting.
tags: [maps, gbp, audit]
tier: 1
generated: { by: openai/gpt-6, at: 2026-11-28T02:39:39Z }
status: stable
stale_after: 2027-02-27
sources:
  - id: dataforseo
    resource: /references/dataforseo.md
    title: DataForSEO
  - id: google-maps-merchant-advertising
    resource: /references/google-review-policy.md
    title: Google Maps — Advertising and solicitation
---

Audits the 25 fields that affect GBP quality and ranking. Tier 1 uses live API data; [Tier 0](/maps/capability-tiers.md) falls back to detectable on-page signals. Complements the on-page view in [GBP signals](/local-seo/gbp-signals.md).

# Tier 1 workflow

1. Fetch the profile via the DataForSEO Business Data API's Google My Business endpoint (keyword or CID).
2. Map the API response to the 25-field checklist.
3. Score each field: Present + Optimised = 2pts, Present = 1pt, Missing = 0pts.
4. Apply industry-specific weight multipliers.
5. Normalise to a 0–100 scale.

# Merchant content check for networks

Inspect the public listing and recent Posts for each location in scope, alongside the shared templates and local overrides. Record the profile URL, field or post, observed date and suggested correction. Flag promotional prices, limited-time offers and direct calls to action in permanent copy. For Posts, check eligibility by business category and confirm the offer dates, branch participation and destination. Mark any surface you cannot see as unknown. Use the [Google Posts publishing checklist](/gbp/google-posts.md#publishing-promotions-across-a-network) for the remediation steps.[^google-maps-merchant-advertising]

# Tier 0 workflow

1. Fetch the business website.
2. Extract visible GBP signals (Maps embed, place references, review widgets).
3. Apply the static checklist from detectable signals.
4. Mark undetectable fields as "Unknown (requires DataForSEO for live data)".
