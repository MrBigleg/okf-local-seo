---
type: Reference
title: DataForSEO
description: SEO data API powering Tier 1+ maps intelligence — SERP API (Google → Maps), Business Data API (Google → Google My Business), and Business Data API (Google → Google Reviews) endpoints.
resource: https://dataforseo.com/
publisher: DataForSEO
published: living document (product documentation)
accessed: 2026-08-27
confidence: high
scope: Commercial SEO data API; capabilities and endpoint names per vendor documentation.
tags: [reference, api, maps]
generated: { by: human:craigburton, at: 2026-06-24T00:00:00Z }
verified:  { by: anthropic/claude-sonnet-5, at: 2026-08-27T00:00:00Z }
status: stable
stale_after: 2026-11-27
sources:
  - id: dataforseo
    resource: https://dataforseo.com/
    title: DataForSEO
---

DataForSEO provides the live data behind [Tier 1+ maps intelligence](/maps/capability-tiers.md): the SERP API's Google → Maps endpoint ([geo-grid](/maps/geo-grid-tracking.md), [competitors](/maps/competitor-radius.md)), the Business Data API's Google → Google My Business endpoint ([GBP audit](/maps/gbp-profile-audit.md)), and the Business Data API's Google → Google Reviews endpoint ([review intelligence](/maps/review-intelligence.md)). Usage consumes credits — always show a cost estimate before geo-grid scans.

Confirmed against `docs.dataforseo.com/v3/` on 27 August 2026: the bundle previously used informal shorthand ("Maps SERP API", "My Business Info API", "Reviews API") that no longer matches DataForSEO's current documented product structure. The capabilities are unchanged — only the naming has been aligned to the vendor's SERP API / Business Data API hierarchy.
