---
type: Report
title: Verification report — 2026-07-27 (Group A2)
description: Claim-by-claim fact-check of Group A2 (the four detection/maps docs citing bare external URLs) against primary sources, completed 27 July 2026.
tags: [governance, verification, local-seo, maps]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
stale_after: 2026-10-27
sources:
  - id: schema-org-areaserved
    resource: https://schema.org/areaServed
    title: Schema.org — areaServed
  - id: google-gbp-service-areas
    resource: /references/google-gbp-service-areas.md
    title: Google — Manage your service areas for service-area and hybrid businesses
  - id: schema-org-localbusiness
    resource: /references/schema-org-localbusiness.md
    title: Schema.org — LocalBusiness
  - id: google-gbp-categories-description
    resource: /references/google-gbp-categories-description.md
    title: Google — Guidelines for representing your business on Google
  - id: bing-places-for-business
    resource: https://www.bingplaces.com/
    title: Bing Places for Business
  - id: apple-business-connect
    resource: https://businessconnect.apple.com/
    title: Apple Business Connect
  - id: nominatim-docs
    resource: https://nominatim.org/release-docs/latest/
    title: Nominatim release documentation
  - id: google-local-business-structured-data
    resource: https://developers.google.com/search/docs/appearance/structured-data/local-business
    title: Google Search Central — LocalBusiness structured data
  - id: google-review-snippet-structured-data
    resource: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
    title: Google Search Central — Review snippet structured data
---

Checked against primary sources on 27 July 2026 — Group A2 of the citation backfill kickoff: the four docs that cited bare external URLs, verified in the same sitting as promoting their multi-cited sources to `Reference` docs. See the [maintenance policy](/maintenance.md) for review cadence.

# Results

| Document | Claim | Result | Primary source |
|---|---|---|---|
| `local-seo/business-type-detection.md` | SAB signal: `areaServed` in schema without `address.streetAddress` | Verified: `areaServed` (domainIncludes `Organization`, `Service`, `ContactPoint`, `Offer`, others) is defined as the geographic area a service or offer is provided — consistent with using it as a no-storefront signal. | https://schema.org/areaServed |
| `local-seo/business-type-detection.md` | Hybrid businesses keep an address and add service areas; SABs clear the address | Verified against the promoted reference. | /references/google-gbp-service-areas.md |
| `local-seo/industry-vertical-detection.md` | Schema subtypes it routes to are defined by the `LocalBusiness` hierarchy | Verified against the promoted reference — Restaurant, Store, and 30+ other subtypes confirmed live. | /references/schema-org-localbusiness.md |
| `local-seo/industry-vertical-detection.md` | Vertical routing follows GBP category patterns | Verified against the promoted reference. | /references/google-gbp-categories-description.md |
| Both detection docs | "A heuristic detection method derived from observable page signals; not an externally published taxonomy" | Confirmed as the correct framing — no external source claims these detection signal tables as a taxonomy; kept as-is per the kickoff brief's explicit guidance not to force a green tick on an unverifiable method. | n/a |
| `maps/nap-verification.md` | Apple has no public NAP API; recommend Apple Business Connect | Verified functionally: `businessconnect.apple.com` currently redirects (302) to `business.apple.com`, Apple's consolidated business hub, which still surfaces Maps-listing management ("Put your business on the map for millions to see"). No public API found. | https://businessconnect.apple.com/ |
| `maps/nap-verification.md` | Bing Places for Business is the claiming tool for Bing Maps | Verified with a redirect note: `bingplaces.com` now permanently (301) redirects to `bing.com/forbusiness`, Bing's consolidated business hub. The capability (claiming/managing a Bing listing) is unchanged; only the marketing URL moved. | https://www.bingplaces.com/ |
| `maps/nap-verification.md` | OSM/Nominatim search covers address lookups | Verified: the Nominatim 5.3.2 manual documents `Search` and `Reverse` API endpoints for looking up OSM data by name and address. | https://nominatim.org/release-docs/latest/ |
| `maps/schema-generation.md` | Required properties: `@type`, `name`, `address`, `image` | **Corrected**: Google's current LocalBusiness structured-data guidelines require only `name` and `address`. `@type` is a schema.org syntax requirement, not a Google-listed property, and `image` is not required (or even recommended) for `LocalBusiness` — unlike Product/Recipe types. The workflow step was rewritten to state this accurately. | https://developers.google.com/search/docs/appearance/structured-data/local-business |
| `maps/schema-generation.md` | Recommended properties: `telephone`, `url`, `geo`, `openingHoursSpecification`, `priceRange` | Verified: all five appear in Google's current recommended-properties list (which also lists `aggregateRating`, `department`, `menu`, `review`, `servesCuisine`, not claimed by this doc). | https://developers.google.com/search/docs/appearance/structured-data/local-business |
| `maps/schema-generation.md` | Self-serving review markup is ignored by Google | Verified with precision: Google states a page is "ineligible for star review feature" if the entity being reviewed controls the reviews about itself — functionally what the doc calls "ignores"; wording left as-is since the practical guidance is unchanged. | https://developers.google.com/search/docs/appearance/structured-data/review-snippet |
| `maps/schema-generation.md` | Schema subtype authority is `LocalBusiness` | Verified against the promoted reference. | /references/schema-org-localbusiness.md |

# Claims requiring human follow-up

None. The one substantive error found — `image` listed as a required LocalBusiness property in `maps/schema-generation.md` — was corrected in this pass, not deferred.
