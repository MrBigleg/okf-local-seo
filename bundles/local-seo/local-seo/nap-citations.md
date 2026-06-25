---
type: Ranking Dimension
title: NAP Consistency & Citations
description: Consistent name/address/phone across sources, and presence on the directories that feed search and AI.
tags: [local-seo, nap, citations, ranking-factors]
timestamp: 2026-06-25T00:00:00Z
---

Citations carry less weight for the traditional local pack than they once did, but consistency still matters — and citation-style signals feed AI discovery, which sources business facts from across the web rather than from Google Business Profile directly.

# What to check

* **NAP consistency** — compare name, address, and phone across three sources and flag any mismatch:
  1. Visible page HTML (footer, contact page).
  2. LocalBusiness JSON-LD schema.
  3. Any visible GBP data.
* Presence on core directories — Google Business Profile, plus the likes of Yelp, BBB, and Facebook. Quick checks: `site:yelp.com "Business Name"`, `site:bbb.org "Business Name"`.
* **Apple Business Connect** — adoption is strikingly low (BrightLocal: only ~16% of businesses use it, and ~58% haven't even claimed their Apple Maps listing). That makes claiming it a cheap, uncontested win.
* **Bing Places** — worth claiming; the Bing index feeds several AI assistants, so it has reach beyond Bing search itself.
* Data aggregators (e.g. Data Axle, Foursquare) for downstream distribution.

# Scoring guide

| Level | Criteria |
|-------|----------|
| Full | Consistent NAP across page/schema/GBP; present on core directories. |
| Partial | NAP present but with inconsistencies; some listings missing. |
| Low | NAP discrepancies, no detectable listings, no schema address. |

# Related

Cross-platform NAP across Google, Bing, Apple, and OSM is verified in [maps NAP verification](/maps/nap-verification.md).

# Citations

[1] [BrightLocal Apple Business Connect research](/references/brightlocal-apple-business-connect.md)
