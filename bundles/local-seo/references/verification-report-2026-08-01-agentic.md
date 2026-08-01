---
type: Report
title: Agentic-section verification report — 2026-08-01
description: Monthly claim-by-claim maintenance review of the seven volatile agentic documents, completed 1 August 2026.
tags: [governance, verification, agentic, maintenance]
generated: { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
verified:  { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
status: stable
stale_after: 2026-11-01
sources:
  - id: google-business-agent
    resource: https://support.google.com/brandprofile/answer/16410382?hl=en
    title: Google — Get started with Business Agent
  - id: google-food-menus
    resource: https://developers.google.com/my-business/content/update-food-menus
    title: Google Business Profile APIs — Update Food Menus
  - id: ucp-specification-overview
    resource: https://ucp.dev/specification/overview/
    title: Universal Commerce Protocol — Specification overview
    last_modified: 2026-04-08
  - id: google-hotel-prices
    resource: https://developers.google.com/hotels/hotel-prices/dev-guide
    title: Google Hotel APIs — Hotel Prices Developer's Guide
    last_modified: 2025-04-14
  - id: google-agentic-commerce
    resource: https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/
    title: Google — New tech and tools for retailers in an agentic shopping era
  - id: ucp
    resource: https://ucp.dev/
    title: Universal Commerce Protocol
  - id: ap2-specification
    resource: https://ap2-protocol.org/
    title: Agent Payments Protocol — Specification
  - id: google-cloud-ap2
    resource: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
    title: Google Cloud — Announcing AP2
  - id: acp-specification
    resource: https://www.agenticcommerce.dev/
    title: Agentic Commerce Protocol — Open specification
  - id: coinbase-x402
    resource: https://docs.cdp.coinbase.com/x402/welcome
    title: Coinbase Developer Platform — x402 overview
  - id: google-ask-maps
    resource: https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/
    title: Google — How we're reimagining Maps with Gemini
  - id: geo-paper
    resource: https://arxiv.org/abs/2311.09735
    title: Aggarwal et al. — GEO: Generative Engine Optimization
    last_modified: 2024-06-28
  - id: google-maps-contributor-updates
    resource: https://blog.google/products-and-platforms/products/maps/contributor-updates/
    title: Google Maps — Contributor updates
  - id: google-maps-grounding
    resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps
    title: Google Cloud — Grounding with Google Maps
    last_modified: 2026-07-31
  - id: google-maps-grounding-lite
    resource: https://developers.google.com/maps/ai/grounding-lite
    title: Google Maps Platform — Maps Grounding Lite
    last_modified: 2026-07-28
  - id: google-place-summaries
    resource: https://developers.google.com/maps/documentation/places/web-service/place-summaries
    title: Google Maps Platform — AI-powered place summaries
  - id: google-gbp-posts
    resource: https://developers.google.com/my-business/content/posts-data
    title: Google Business Profile APIs — Create Posts
    last_modified: 2026-02-24
  - id: google-gbp-reviews
    resource: https://developers.google.com/my-business/content/review-data
    title: Google Business Profile APIs — Work with review data
    last_modified: 2025-08-28
  - id: google-gbp-location-patch
    resource: https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch
    title: Google Business Profile APIs — locations.patch
  - id: google-gbp-upload-media
    resource: https://developers.google.com/my-business/content/upload-photos
    title: Google Business Profile APIs — Upload media
    last_modified: 2025-08-28
  - id: google-gbp-attributes
    resource: https://developers.google.com/my-business/content/attributes
    title: Google Business Profile APIs — Add attributes
    last_modified: 2025-08-28
  - id: google-gbp-services
    resource: https://developers.google.com/my-business/content/services
    title: Google Business Profile APIs — Add services
    last_modified: 2025-08-28
  - id: google-gbp-prerequisites
    resource: https://developers.google.com/my-business/content/prereqs
    title: Google Business Profile APIs — Prerequisites
    last_modified: 2025-08-28
  - id: google-local-inventory-overview
    resource: https://support.google.com/merchants/answer/14615117?hl=en
    title: Google Merchant Center — Local inventory ads and free local listings overview
  - id: google-local-inventory-specification
    resource: https://support.google.com/merchants/answer/14819809?hl=en
    title: Google Merchant Center — Local inventory data specification
  - id: lastmile-high-dollar-survey
    resource: https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte
    title: Lastmile Retail — Data-based Tactics for Increasing High-Dollar Local Purchases
---

Checked the seven volatile `agentic/` documents against the available cited primary sources on 1 August 2026. OpenAI's redundant Instant Checkout announcement could not be independently reopened because automated access returned HTTP 403, so it was removed from active provenance in favour of ACP's accessible canonical specification; [issue #8](https://github.com/MrBigleg/okf-local-seo/issues/8) remains the manual follow-up. This was an AI-run evidence review; factual changes still require human approval before merge under the [maintenance policy](/maintenance.md).

# Results

| Document | Result | Primary-source evidence |
|---|---|---|
| `agentic/agentic-commerce-readiness.md` | Core eligibility, structured-menu, UCP discovery and Hotel Prices claims remain supported. UCP still says detailed Food and Lodging specifications are coming soon, so the dated status note was advanced to this review date. | [Business Agent](https://support.google.com/brandprofile/answer/16410382?hl=en); [Food Menus](https://developers.google.com/my-business/content/update-food-menus); [UCP overview](https://ucp.dev/specification/overview/); [Hotel Prices](https://developers.google.com/hotels/hotel-prices/dev-guide) |
| `agentic/agentic-commerce.md` | UCP, AP2, ACP and x402 remain distinct public protocols with the same conservative adoption caveat. The inaccessible, redundant OpenAI announcement was removed from active provenance; the accessible canonical ACP specification supports the retained scope and backer claims. | [Google commerce announcement](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/); [UCP](https://ucp.dev/); [AP2](https://ap2-protocol.org/); [ACP](https://www.agenticcommerce.dev/); [x402](https://docs.cdp.coinbase.com/x402/welcome) |
| `agentic/ask-maps.md` | Name, launch date, 300M+ places, 500M+ contributors and supported actions remain supported. The concept now explicitly limits the announcement to historical March 2026 rollout evidence and makes no claim about current availability. | [Google — How we're reimagining Maps with Gemini](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/) |
| `agentic/generative-engine-optimization.md` | The GEO paper's definition and KDD 2024 status remain supported. Google's contributor announcement still supports the April 2026 caption feature and its launch limits. No ranking-factor claim was added. | [GEO paper](https://arxiv.org/abs/2311.09735); [Google Maps contributor update](https://blog.google/products-and-platforms/products/maps/contributor-updates/) |
| `agentic/grounding-google-maps.md` | Existing place-count, response-field, attribution, Grounding Lite and place-summary claims remain supported. Full grounding now documents Find Directions and Search Along Route; Grounding Lite now has an experimental Resolution API for names, addresses and Maps URLs. | [Full Maps grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps); [Grounding Lite](https://developers.google.com/maps/ai/grounding-lite); [Places summaries](https://developers.google.com/maps/documentation/places/web-service/place-summaries) |
| `agentic/hitl-gbp-management.md` | Posts, review replies, targeted location patching, food menus and the product-post exclusion remain supported. No generic undo endpoint is documented. Added missing primary citations for media, attributes, services and API prerequisites. | [Posts](https://developers.google.com/my-business/content/posts-data); [reviews](https://developers.google.com/my-business/content/review-data); [location patch](https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch); [media](https://developers.google.com/my-business/content/upload-photos); [attributes](https://developers.google.com/my-business/content/attributes); [services](https://developers.google.com/my-business/content/services); [prerequisites](https://developers.google.com/my-business/content/prereqs) |
| `agentic/real-time-local-inventory.md` | Merchant Center still supports the listed ID, store, availability, price, quantity and pickup fields. The field name was corrected to Google's current **pickup SLA** terminology. The scoped Lastmile article and embedded charts support the 1,000-person, $300+ scope and cited 95%, 56%, 48%, 40% and paired 37% figures; publication and authorship metadata were corrected. | [Local inventory overview](https://support.google.com/merchants/answer/14615117?hl=en); [data specification](https://support.google.com/merchants/answer/14819809?hl=en); [Lastmile survey article](https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte) |

# Source-access notes

* `python3 tool/okf_verify.py bundles/local-seo --check-urls` reported every external URL as `URLError` in this environment, including pages independently retrieved successfully with browser and `curl`. URL-check warnings were treated as a tooling/network limitation, not evidence that every source was dead.
* OpenAI's Instant Checkout announcement returned HTTP 403 to automated retrieval. It was removed from active provenance because the accessible canonical ACP specification supports the retained claim; issue #8 remains open for optional manual confirmation.
* The LinkedIn survey page showed a sign-in modal in the interactive browser, but its public server-rendered HTML and embedded charts were retrievable.

# Changes made

* Rolled all seven volatile documents to `stale_after: 2026-09-01` and recorded AI verification provenance.
* Updated the maintenance policy's own verification event and rolled its durable freshness date forward.
* Updated the accessed/verification dates on the first-class references actually reopened during the pass.
* Added newly documented Maps grounding and Resolution API capabilities.
* Corrected Merchant Center pickup terminology.
* Added missing HITL capability citations and corrected the Lastmile article's publication, authorship and methodology caveat.
* Regenerated `viz.html` and ran the verifier and test suite before review.

# Human review gate

No factual update should merge until a human reviewer has checked this report and the diff, as required by the maintenance policy.
