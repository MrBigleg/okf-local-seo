---
type: Report
title: Follow-up verification report — 2026-08-27
description: Closes three carried-over follow-up issues — the OpenAI Instant Checkout citation, DataForSEO endpoint naming drift, and the Whitespark 2026 headline re-confirmation.
tags: [governance, verification, maintenance]
generated: { by: anthropic/claude-sonnet-5, at: 2026-08-27T00:00:00Z }
verified:  { by: anthropic/claude-sonnet-5, at: 2026-08-27T00:00:00Z }
status: stable
stale_after: 2026-11-27
sources:
  - id: openai-instant-checkout
    resource: https://openai.com/index/buy-it-in-chatgpt/
    title: OpenAI — Buy it in ChatGPT — Instant Checkout and the Agentic Commerce Protocol
  - id: whitespark-2026
    resource: https://whitespark.ca/local-search-ranking-factors/
    title: Whitespark — Local Search Ranking Factors 2026
  - id: dataforseo-docs
    resource: https://docs.dataforseo.com/v3/
    title: DataForSEO API documentation v3
---

Closed three low-effort follow-up issues carried from the 2026-07-27 and 2026-08-01 verification passes: [#8](https://github.com/MrBigleg/okf-local-seo/issues/8), [#9](https://github.com/MrBigleg/okf-local-seo/issues/9), and [#10](https://github.com/MrBigleg/okf-local-seo/issues/10). This was an AI-run evidence review; factual changes still require human approval before merge under the [maintenance policy](/maintenance.md).

# Results

| Issue | Result | Primary-source evidence |
|---|---|---|
| #8 — OpenAI Instant Checkout citation | The URL, previously blocked (HTTP 403) to automated fetch, is now reachable and its content is unchanged: Instant Checkout, powered by the Agentic Commerce Protocol, built with Stripe, announced 29 September 2025. This matches the already-active ACP canonical-spec citation in `references/agentic-commerce-protocols.md`, which was substituted for this URL during the 2026-08-01 pass. No content or `sources` change was needed — the substitution remains the correct citation. | [OpenAI — Buy it in ChatGPT](https://openai.com/index/buy-it-in-chatgpt/) |
| #9 — DataForSEO endpoint naming drift | Confirmed DataForSEO's current documented structure: SERP API → Google → Maps; Business Data API → Google → Google My Business; Business Data API → Google → Google Reviews. Renamed the informal shorthand ("Maps SERP API", "My Business Info API", "Reviews API") to match, across `references/dataforseo.md` and the five citing `maps/` docs. No capability claims changed — naming only. | [DataForSEO API docs v3](https://docs.dataforseo.com/v3/) |
| #10 — Whitespark 2026 headline re-confirmation | Reopened the full 2026 edition directly (the earlier pass only reached the gated landing page). Confirmed **Primary GBP Category** is the single highest-scored local pack/Maps factor (score 227) and Google Business Profile signals remain the first-listed, most prominent signal group — the qualitative "GBP is the leading driver of local pack visibility" claim holds. | [Whitespark — Local Search Ranking Factors 2026](https://whitespark.ca/local-search-ranking-factors/) (published 2025-11-06) |

# Changes made

* `references/agentic-commerce-protocols.md`: no change — confirmed the existing substitution is correct.
* `references/dataforseo.md`: renamed endpoints in `description` and body; `accessed` and `verified` updated; `stale_after` rolled to 2026-11-27.
* `maps/capability-tiers.md`, `maps/competitor-radius.md`, `maps/gbp-profile-audit.md`, `maps/geo-grid-tracking.md`, `maps/review-intelligence.md`: endpoint names updated where cited; `verified` updated; `stale_after` rolled to 2027-02-27.
* `references/whitespark-2026.md`: `accessed`, `published` (dated to the confirmed 2026 edition), and `verified` updated; `stale_after` rolled to 2026-11-27; added a body note confirming the re-check.
* `local-seo/gbp-signals.md`, `local-seo/local-onpage.md`, `local-seo/local-schema.md`: `verified` updated; `stale_after` rolled to 2027-02-27 (no body change — the qualitative claim they cite was reconfirmed unchanged).
* Regenerated `viz.html` and re-ran the verifier before review.

# Human review gate

No factual update should merge until a human reviewer has checked this report and the diff, as required by the maintenance policy.
