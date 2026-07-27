---
type: Report
title: Verification report — 2026-07-27 (Group A1)
description: Claim-by-claim fact-check of the 13 Group A1 reference-backed docs, batched by shared reference, completed 27 July 2026.
tags: [governance, verification, local-seo, maps]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-27T00:00:00Z }
status: stable
stale_after: 2026-10-27
sources:
  - id: whitespark-2026
    resource: /references/whitespark-2026.md
    title: Whitespark Local Search Ranking Factors
  - id: brightlocal-apple-business-connect
    resource: /references/brightlocal-apple-business-connect.md
    title: BrightLocal Apple Business Connect research
  - id: ahrefs-ai-overviews
    resource: /references/ahrefs-ai-overviews.md
    title: Ahrefs AI Overview brand-correlation study
  - id: sterling-sky
    resource: /references/sterling-sky.md
    title: Sterling Sky review research
  - id: brightlocal-lcrs
    resource: /references/brightlocal-lcrs.md
    title: BrightLocal Local Consumer Review Survey
  - id: google-ai-optimization-guide
    resource: /references/google-ai-optimization-guide.md
    title: Google — AI features and your website
  - id: seer-chatgpt-conversion
    resource: /references/seer-chatgpt-conversion.md
    title: Seer Interactive ChatGPT conversion case study
  - id: dataforseo
    resource: /references/dataforseo.md
    title: DataForSEO
  - id: google-local-business-structured-data
    resource: /references/google-local-business-structured-data.md
    title: Google Search Central — LocalBusiness structured data
---

Checked against primary sources on 27 July 2026 — Group A1 of the citation backfill kickoff: the 13 docs that lean on already-verified references, batched by shared source so each was opened once (Whitespark ×3, BrightLocal ABC ×2, Ahrefs ×2, Sterling Sky ×3, BrightLocal LCRS ×1, Google AI features ×1, Seer ×1, DataForSEO ×5). Each reference's live source was re-opened to confirm it has not been superseded before checking the citing docs' wording against it. See the [maintenance policy](/maintenance.md) for review cadence.

# Reference freshness check

| Reference | Still current? | Notes |
|---|---|---|
| Whitespark Local Search Ranking Factors | Yes | Site now shows the "2026 edition" (published 6 Nov 2025). Full report content is gated behind the landing page, so the headline GBP-primacy claim could not be re-confirmed by automated fetch; the bundle already cites it qualitatively only, per its own scope note. |
| BrightLocal Apple Business Connect research | Yes | All three figures (16% / 58% / 59%) confirmed verbatim on the live page. Publish date is 1 June 2023 — older than the reference's "n.d." suggested, but the figures are unchanged. |
| Ahrefs AI Overview brand-correlation study | Yes | 0.664 / 0.218 correlation figures confirmed verbatim, ~75,000-brand sample confirmed. Published 26 May 2025. |
| Sterling Sky review research | Yes | The "18-Day Rule" phrase is confirmed live, in the article's TL;DR only ("fall off a cliff... for even three weeks"). The underlying case-study detail is thinner than the rule itself — consistent with the reference's own "community-recognised pattern, not confirmed Google policy" framing. Article dated 30 Apr 2025, labelled a 2025 update. |
| BrightLocal Local Consumer Review Survey | Yes | Now the 2026 edition (published 11 Feb 2026). Both figures (68% / 31%) confirmed verbatim. |
| Google — AI features and your website | Yes | Page live, last updated 10 Dec 2025. The "no separate AI SEO lever" position confirmed verbatim: "There are no additional requirements to appear in AI Overviews or AI Mode." |
| Seer Interactive ChatGPT conversion case study | Yes | 15.9% vs 1.76% conversion figures confirmed verbatim. Published 3 Jun 2025; single-client caveat still applies. |
| DataForSEO | Yes | Reviews and Business Data (Google My Business) capabilities confirmed live on both the marketing site and `docs.dataforseo.com`. Google's Maps search sits under DataForSEO's SERP API rather than a separately branded "Maps SERP API," and Google My Business sits under the Business Data API rather than a standalone "My Business Info API" — informal naming already used in this bundle, not a factual error, but noted here for anyone re-checking endpoint names directly against DataForSEO's docs. |

# Results

| Document | Claim | Result |
|---|---|---|
| `local-seo/gbp-signals.md` | GBP is the single biggest lever on local pack visibility (Whitespark) | Verified — wording matches the reference's scope (qualitative, no percentage asserted). |
| `local-seo/local-onpage.md` | Dedicated service pages rank near the top of Whitespark's local organic factors | Verified — wording matches the reference's scope. |
| `local-seo/local-schema.md` | Structured data is not a direct ranking factor; required/recommended properties | **Sourcing gap corrected**: this doc's Google-specific claims (the required-properties list, the "not a ranking factor" line) were cited only to Whitespark, which doesn't establish either claim. Added [Google Search Central — LocalBusiness structured data](/references/google-local-business-structured-data.md) (new promotion, now cited by this doc and `maps/schema-generation.md`) and [Schema.org — LocalBusiness](/references/schema-org-localbusiness.md) as sources. Content itself was accurate — `name`/`address` required, the rest recommended, `image` correctly placed under Recommended not Required. |
| `local-seo/nap-citations.md` | Apple Business Connect adoption ~16%, ~58% unclaimed | Verified verbatim against the reference. |
| `local-seo/local-authority-links.md` | Brand mentions correlate ~0.664 vs backlinks ~0.218 (Ahrefs) | Verified verbatim against the reference. |
| `local-seo/reviews-reputation.md` | 18-day rule; 68%/31% rating thresholds | Verified against both references; wording already carries the "community-recognised pattern, not confirmed Google policy" caveat. |
| `local-seo/ai-search-local.md` | No separate "AI SEO" lever; ChatGPT ~15.9% vs ~1.76% conversion; brand mentions > backlinks | Verified against all three references; all caveats (single-client, correlation-not-causation) preserved. |
| `maps/capability-tiers.md` | DataForSEO as the Tier 1+ boundary | Verified — DataForSEO remains a live, active commercial API. |
| `maps/competitor-radius.md` | Tier 1 uses the DataForSEO Maps SERP capability | Verified functionally — Google Maps search results are live under DataForSEO's SERP API. |
| `maps/gbp-profile-audit.md` | Tier 1 uses the DataForSEO My Business Info capability | Verified functionally — Google My Business data is live under DataForSEO's Business Data API. |
| `maps/geo-grid-tracking.md` | Tier 1 uses DataForSEO Maps SERP calls with `location_coordinate` | Verified functionally — capability confirmed live; exact parameter name not independently re-checked against the DataForSEO API reference in this pass. |
| `maps/review-intelligence.md` | DataForSEO Reviews API; 18-day rule | Verified — Reviews capability confirmed live; 18-day rule verified per the Sterling Sky row above. |
| `playbooks/gbp-optimisation-checklist.md` | Apple Business Connect ~16% adoption; 18-day rule; brand mentions correlate with AI visibility | Verified against all three cited references; all three `note:` figures confirmed unchanged. |

# Claims requiring human follow-up

* **DataForSEO endpoint naming** — this bundle uses informal product names ("Maps SERP API", "My Business Info API", "Reviews API") that correspond to, but don't literally match, DataForSEO's current documented structure ("SERP API → Google Maps", "Business Data API → Google My Business" / "→ Google Reviews"). Not a factual error and not corrected in this pass; worth a wording pass next time these docs are touched for any other reason.
* **Whitespark headline claim** — the specific "GBP is the leading driver of local pack visibility" framing could not be re-confirmed against the 2026 edition's actual report content (gated behind the landing page). The bundle's own scope note already treats this qualitatively; flag for re-confirmation if the full report ever becomes fetchable.
