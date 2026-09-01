---
type: Report
title: Agentic-section verification report — 2026-09-01
description: Monthly claim-by-claim maintenance review of the seven volatile agentic documents, completed 1 September 2026.
tags: [governance, verification, agentic, maintenance]
generated: { by: anthropic/claude-sonnet-5, at: 2026-09-01T00:00:00Z }
verified:  { by: anthropic/claude-sonnet-5, at: 2026-09-01T00:00:00Z }
status: stable
stale_after: 2026-12-01
sources:
  - id: ap2-protocol
    resource: https://ap2-protocol.org/
    title: Agent Payments Protocol (AP2)
  - id: google-cloud-ap2-announcement
    resource: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
    title: Google Cloud — Announcing the Agent Payments Protocol (AP2)
  - id: ucp
    resource: https://ucp.dev/
    title: Universal Commerce Protocol
  - id: ucp-specification-overview
    resource: https://ucp.dev/specification/overview/
    title: Universal Commerce Protocol — Specification overview
  - id: acp-specification
    resource: https://www.agenticcommerce.dev/
    title: Agentic Commerce Protocol — Open specification
  - id: coinbase-x402
    resource: https://docs.cdp.coinbase.com/x402/welcome
    title: Coinbase Developer Platform — x402 overview
  - id: google-agentic-commerce-blog
    resource: https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/
    title: Google — New tech and tools for retailers in an agentic shopping era
  - id: geo-paper
    resource: https://arxiv.org/abs/2311.09735
    title: Aggarwal et al. — GEO: Generative Engine Optimization
    last_modified: 2024-06-28
  - id: google-maps-contributor-updates
    resource: https://blog.google/products-and-platforms/products/maps/contributor-updates/
    title: Google Maps — Contributor updates
  - id: google-ask-maps
    resource: https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/
    title: Google — How we're reimagining Maps with Gemini
  - id: google-maps-grounding
    resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps
    title: Google Cloud — Grounding with Google Maps
  - id: google-maps-grounding-lite
    resource: https://developers.google.com/maps/ai/grounding-lite
    title: Google Maps Platform — Maps Grounding Lite
  - id: google-place-summaries
    resource: https://developers.google.com/maps/documentation/places/web-service/place-summaries
    title: Google Maps Platform — AI-powered place summaries
  - id: google-business-agent
    resource: https://support.google.com/brandprofile/answer/16410382?hl=en
    title: Google — Get started with Business Agent
  - id: google-hotel-prices
    resource: https://developers.google.com/hotels/hotel-prices/dev-guide
    title: Google Hotel APIs — Hotel Prices Developer's Guide
    last_modified: 2025-04-14
  - id: google-food-menus
    resource: https://developers.google.com/my-business/content/update-food-menus
    title: Google Business Profile APIs — Update Food Menus
  - id: google-gbp-posts
    resource: https://developers.google.com/my-business/content/posts-data
    title: Google Business Profile APIs — Create Posts
  - id: google-gbp-reviews
    resource: https://developers.google.com/my-business/content/review-data
    title: Google Business Profile APIs — Work with review data
  - id: google-gbp-location-patch
    resource: https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch
    title: Google Business Profile APIs — locations.patch
  - id: google-gbp-upload-media
    resource: https://developers.google.com/my-business/content/upload-photos
    title: Google Business Profile APIs — Upload media
  - id: google-gbp-attributes
    resource: https://developers.google.com/my-business/content/attributes
    title: Google Business Profile APIs — Add attributes
  - id: google-gbp-services
    resource: https://developers.google.com/my-business/content/services
    title: Google Business Profile APIs — Add services
  - id: google-gbp-prerequisites
    resource: https://developers.google.com/my-business/content/prereqs
    title: Google Business Profile APIs — Prerequisites
  - id: google-local-inventory-overview
    resource: https://support.google.com/merchants/answer/14615117?hl=en
    title: Google Merchant Center — Local inventory ads and free local listings overview
  - id: google-local-inventory-specification
    resource: https://support.google.com/merchants/answer/14819809?hl=en
    title: Google Merchant Center — Local inventory data specification
  - id: lastmile-high-dollar-survey
    resource: https://www.lastmileretail.com/expert-perspectives-blogs/data-based-tactics-for-increasing-high-dollar-local-purchases
    title: Lastmile Retail — Data-based Tactics for Increasing High-Dollar Local Purchases
---

Checked the seven volatile `agentic/` documents against their cited primary sources on 1 September 2026, the next scheduled monthly pass after [2026-08-01](/references/verification-report-2026-08-01-agentic.md). This was an AI-run evidence review; factual changes still require human approval before merge under the [maintenance policy](/maintenance.md).

# Results

Every claim across all seven documents was independently reconfirmed unchanged at source. No corrections were needed this pass.

| Document | Result | Primary-source evidence |
|---|---|---|
| `agentic/agentic-commerce-readiness.md` | Business Agent eligibility (US store, verified Merchant Center, 50+ approved free listings, claimed brand profile), structured food-menu support, UCP's `/.well-known/ucp` discovery model, and Hotel Prices' availability/rates/inventory messaging remain unchanged. UCP's Food and Lodging verticals still show "detailed specifications coming soon" on the live site. | [Business Agent](https://support.google.com/brandprofile/answer/16410382?hl=en); [Food Menus](https://developers.google.com/my-business/content/update-food-menus); [UCP](https://ucp.dev/); [UCP overview](https://ucp.dev/specification/overview/); [Hotel Prices](https://developers.google.com/hotels/hotel-prices/dev-guide) (still dated 2025-04-14) |
| `agentic/agentic-commerce.md` | UCP (launched January 2026, Google-co-developed), AP2 (announced September 2025, now "more than 60" partner organisations — reconfirmed), ACP (OpenAI + Stripe, September 2025) and x402 (Coinbase) remain distinct, live protocols with the same conservative adoption framing. | [Google agentic commerce launch](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/); [AP2 site](https://ap2-protocol.org/); [AP2 announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol); [ACP](https://www.agenticcommerce.dev/); [x402](https://docs.cdp.coinbase.com/x402/welcome) |
| `agentic/ask-maps.md` | Name, 12 March 2026 launch date, 300M+ places, 500M+ contributors, and US/India Android/iOS rollout with desktop "coming soon" remain unchanged on the live announcement. | [Google — How we're reimagining Maps with Gemini](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/) |
| `agentic/generative-engine-optimization.md` | The GEO paper's KDD 2024 acceptance is still shown on its arXiv listing. Google's April 2026 Gemini caption-suggestion feature (English, iOS, U.S., expanding) is unchanged on the source blog post. | [GEO paper](https://arxiv.org/abs/2311.09735); [Google Maps contributor update](https://blog.google/products-and-platforms/products/maps/contributor-updates/) |
| `agentic/grounding-google-maps.md` | 250M+ places, `groundingChunks`/`placeAnswerSources` response fields, Find Directions and Search Along Route, Grounding Lite's MCP tools and experimental `resolveNames`/`resolveMapsUrls` (still v1alpha), and Places API `generativeSummary` (still English-only, India/US) all remain unchanged. | [Full Maps grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps); [Grounding Lite](https://developers.google.com/maps/ai/grounding-lite); [Place summaries](https://developers.google.com/maps/documentation/places/web-service/place-summaries) |
| `agentic/hitl-gbp-management.md` | Posts (event/CTA/offer, product posts still excluded), review reply/delete, location patch's `updateMask`, media upload, attributes, services and prerequisites all remain unchanged on their respective API docs. | [Posts](https://developers.google.com/my-business/content/posts-data); [Reviews](https://developers.google.com/my-business/content/review-data); [locations.patch](https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch); [Upload media](https://developers.google.com/my-business/content/upload-photos); [Attributes](https://developers.google.com/my-business/content/attributes); [Services](https://developers.google.com/my-business/content/services); [Prerequisites](https://developers.google.com/my-business/content/prereqs) |
| `agentic/real-time-local-inventory.md` | Merchant Center's local inventory fields (ID, store code, availability values, quantity, pickup method, **pickup SLA**) and the 24-hour Business Profile → Merchant Center sync note remain unchanged. The Lastmile survey's 95%, 40% and 37% figures were reconfirmed directly against the publisher's own site (a non-gated mirror of the LinkedIn article); the 56% and 48% figures remain embedded in chart images not extractable as text, consistent with the prior pass's access note. | [Local inventory overview](https://support.google.com/merchants/answer/14615117?hl=en); [Data specification](https://support.google.com/merchants/answer/14819809?hl=en); [Lastmile article, publisher mirror](https://www.lastmileretail.com/expert-perspectives-blogs/data-based-tactics-for-increasing-high-dollar-local-purchases) |

# Source-access notes

* The Lastmile survey article was reconfirmed via `lastmileretail.com`'s own site rather than the LinkedIn URL cited in `references/lastmile-high-dollar-survey.md` — the LinkedIn page still fails automated retrieval (blocks bot access), but the publisher's own mirror carries the same text and confirms three of the five cited figures directly (95%, 40%, 37%). The two chart-only figures (56%, 48%) were not independently re-extracted this pass; no reason to doubt them was found.
* All 24 other primary sources were reopened directly and returned live, matching content.

# Changes made

* Rolled all seven volatile documents to `stale_after: 2026-10-01` and recorded AI verification provenance.
* No factual corrections were needed — every claim reconfirmed unchanged at source.
* Regenerated `viz.html` and ran the verifier before review.

# Human review gate

No factual update should merge until a human reviewer has checked this report and the diff, as required by the maintenance policy.
