# Verification report

Checked against primary sources on 25 June 2026.

| Document | Claim | Result | Primary source |
|---|---|---|---|
| `ask-maps.md` | Official name is Ask Maps | Verified | https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/ |
| `ask-maps.md` | Entry point is under the Maps search bar | Corrected: Google confirms an **Ask Maps** button but does not specify a durable screen position in the primary announcement. | https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/ |
| `ask-maps.md` | Gemini-powered | Verified | https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/ |
| `ask-maps.md` | Launch date and regions | Verified: announced 12 March 2026; rolling out on Android and iOS in the US and India; desktop described as coming soon. | https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/ |
| `ask-maps.md` | Inputs include place facts, reviews, saved/search history and route context | Corrected to Google's wording: 300M+ places, reviews from 500M+ contributors, searched/saved places, directions and ETAs. Cross-app personal data was not claimed. | https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/ |
| `agentic-commerce.md` | Universal Commerce Protocol exists | Verified: launched January 2026 with public specification and named co-developers/endorsers. | https://ucp.dev/ |
| `agentic-commerce.md` | Agent Payments Protocol exists | Verified: announced September 2025 with 60+ participating organisations. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol |
| `agentic-commerce.md` | Agentic Commerce Protocol exists | Verified: developed by OpenAI and Stripe and open-sourced in September 2025. | https://www.agenticcommerce.dev/ |
| `agentic-commerce.md` | Signed payment mandates are a protocol layer | Corrected: signed mandates are an AP2 mechanism, not a separate protocol. | https://ap2-protocol.org/ |
| `agentic-commerce.md` | x402 exists and is relevant to agents | Verified: Coinbase documents an open HTTP-native stablecoin payment protocol; AP2 documents an x402 extension. | https://docs.cdp.coinbase.com/x402/welcome |
| `agentic-commerce.md` | The protocols form an adopted industry stack | Corrected: specifications and early implementations exist, but universal adoption is not established. | https://ucp.dev/ |
| `agentic-commerce-readiness.md` | Merchant Center should align with GBP “Brand Profile” | Corrected: Google's Search brand profile and Google Business Profile are separate surfaces. Business Agent eligibility uses Merchant Center plus a claimed brand profile. | https://support.google.com/brandprofile/answer/16410382?hl=en |
| `agentic-commerce-readiness.md` | Roughly 50 offers unlock Business Agent | Corrected to **at least 50 approved free listings**, plus other eligibility conditions. | https://support.google.com/brandprofile/answer/16410382?hl=en |
| `agentic-commerce-readiness.md` | Vision AI extracts menu items and prices from GBP photos | Dropped: no primary source found. Replaced with the documented structured Food Menus API. | https://developers.google.com/my-business/content/update-food-menus |
| `agentic-commerce-readiness.md` | Commerce protocol discovery uses `/.well-known/` | Verified specifically for UCP at `/.well-known/ucp`. | https://ucp.dev/specification/overview/ |
| `agentic-commerce-readiness.md` | POS-to-KDS order injection is a protocol requirement | Corrected to an operational recommendation. UCP describes food ordering and real-time availability, but detailed food specifications were still forthcoming. | https://ucp.dev/ |
| `agentic-commerce-readiness.md` | Real-time “86-ing” is supported by a named standard | Dropped as a platform capability claim; retained only as an operational consistency requirement. | https://ucp.dev/ |
| `agentic-commerce-readiness.md` | Hotel PMS two-way sync through named vendors | Corrected: Google documents availability, rates and inventory integrations, but no universal requirement for the named vendors was established. | https://developers.google.com/hotels/hotel-prices/dev-guide |
| `agentic-commerce-readiness.md` | OTA rate parity is universal | Dropped: contracts and law vary by market; no single primary source supports a universal claim. | — |
| `agentic-commerce-readiness.md` | OTA commissions are 15–25% | Dropped: no primary source supports this as a universal range. | — |
| `grounding-google-maps.md` | Google Maps grounding tool exists | Verified. Current documentation places it in Gemini Enterprise Agent Platform and exposes it through Vertex AI Studio. | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps |
| `grounding-google-maps.md` | Place index size | Corrected to **over 250 million places**. | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps |
| `grounding-google-maps.md` | Response has `grounding_metadata` and Maps chunks | Verified with naming correction: REST uses `groundingMetadata.groundingChunks`; SDKs may use snake case. | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps |
| `grounding-google-maps.md` | Widget context token / Contextual View | Dropped: not present in the current primary documentation. | — |
| `grounding-google-maps.md` | Grounding Lite is MCP-native | Verified: MCP service with place, weather and route tools. | https://developers.google.com/maps/ai/grounding-lite |
| `grounding-google-maps.md` | Grounding Lite provides navigation | Corrected: it does not provide turn-by-turn directions, real-time traffic or navigation. | https://developers.google.com/maps/ai/grounding-lite |
| `grounding-google-maps.md` | Places API (New) has AI summaries | Verified; returned through `generativeSummary`, with limited language/region/type availability. | https://developers.google.com/maps/documentation/places/web-service/place-summaries |
| `generative-engine-optimization.md` | Defensible GEO definition | Verified against the original GEO paper and narrowed to visibility in generative-engine responses. | https://arxiv.org/abs/2311.09735 |
| `generative-engine-optimization.md` | GEO and AEO have a settled distinction | Corrected: no authoritative standard was found; the document labels its distinction as a bundle-specific working definition. | https://arxiv.org/abs/2311.09735 |
| `generative-engine-optimization.md` | 2026 Maps contributor/Gemini caption update | Verified: announced 7 April 2026, initially English on iOS in the US. | https://blog.google/products-and-platforms/products/maps/contributor-updates/ |
| `real-time-local-inventory.md` | ~95% say pre-visit confirmation is important | Verified and made exact: **95%** said confirming local availability before visiting was somewhat to extremely important for an item priced at $300 or more. | https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte |
| `real-time-local-inventory.md` | ~56% rank real-time availability first | Verified and made exact: **56%** selected real-time product availability before visiting as a factor favouring local over remote shipping. | https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte |
| `real-time-local-inventory.md` | ~48% want reserve/pickup | Verified and made exact: **48%** selected reserving online for in-store purchase or pickup. | https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte |
| `real-time-local-inventory.md` | ~40% blame websites | Verified and narrowed: **40%** reported insufficient product information on company websites. | https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte |
| `real-time-local-inventory.md` | ~37% cannot confirm branch availability | Verified and made exact: **37%** could not confirm availability at a particular store; another **37%** reported inaccurate inventory information. | https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte |
| `real-time-local-inventory.md` | Merchant Center supports branch-level availability, price and pickup | Verified. | https://support.google.com/merchants/answer/14819809?hl=en |
| `hitl-gbp-management.md` | GBP review replies can be written through API | Verified. | https://developers.google.com/my-business/content/review-data |
| `hitl-gbp-management.md` | GBP posts can be created and edited through API | Verified for event, call-to-action and offer posts; product posts are excluded. | https://developers.google.com/my-business/content/posts-data |
| `hitl-gbp-management.md` | Profile fields can be patched through API | Verified for supported fields using an update mask. | https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch |
| `hitl-gbp-management.md` | Approval gates are a Google requirement or norm | Corrected: HITL is presented as an operator governance pattern, not a Google API requirement. | — |
| `hitl-gbp-management.md` | GBP has a generic reversion endpoint | Dropped: no generic undo endpoint was found; reversion is described as a reviewed patch from a known-good snapshot. | https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch |

# Claims requiring human follow-up

* Confirm whether Google has a current replacement for the earlier Maps grounding widget context token or “Contextual View”; neither appears in the current documentation.
* If OTA commission or rate-parity guidance is required, research it by jurisdiction, contract type and named platform rather than publishing a universal range.
