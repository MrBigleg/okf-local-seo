---
type: Report
title: GBP core pages verification report — 2026-11-16
description: Claim-by-claim maintenance review of four GBP pages and seven of their reference pages, with wording aligned to the live sources and unsupported claims removed.
tags: [governance, verification, gbp, maintenance]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
status: draft
sources:
  - id: src-blog-google-products-ads-commerce-connect-local-holiday-shop
    resource: https://blog.google/products/ads-commerce/connect-local-holiday-shoppers/
    title: Connect with local holiday shoppers (accessed 2026-11-16)
  - id: src-blog-google-products-google-plus-localnow-with-dash-of-zagat
    resource: https://blog.google/products/google-plus/localnow-with-dash-of-zagat-and/
    title: Local—now with a dash of Zagat and a sprinkle of Google+ (accessed 2026-11-16)
  - id: src-developers-google-com-my-business-content-accept-or-reject-u
    resource: https://developers.google.com/my-business/content/accept-or-reject-updates
    title: Manage Google Updates | Google Business Profile APIs | Google for Developers (accessed 2026-11-16)
  - id: src-developers-google-com-my-business-reference-businessinformat
    resource: https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch
    title: Method — locations.patch | Google Business Profile APIs | Google for Developers (accessed 2026-11-16)
  - id: src-googleblog-blogspot-com-2010-04-introducing-google-places-ht
    resource: https://googleblog.blogspot.com/2010/04/introducing-google-places.html
    title: Official Google Blog — Introducing Google Places (accessed 2026-11-16)
  - id: src-smallbusiness-googleblog-com-2014-06-help-your-business-shin
    resource: https://smallbusiness.googleblog.com/2014/06/help-your-business-shine-with-google-my.html
    title: Google Small Business — Help your business shine with Google My Business (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-14271705
    resource: https://support.google.com/business/answer/14271705
    title: Verify your business with a video recording - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-3038177
    resource: https://support.google.com/business/answer/3038177
    title: Guidelines for representing your business on Google - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-3038311
    resource: https://support.google.com/business/answer/3038311
    title: Understand what happens to your Business Profile edits - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-3039617
    resource: https://support.google.com/business/answer/3039617
    title: Edit your Business Profile - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-4566671
    resource: https://support.google.com/business/answer/4566671
    title: Request ownership of a Business Profile - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-7039811
    resource: https://support.google.com/business/answer/7039811
    title: Get started with Google Business Profile - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-7091
    resource: https://support.google.com/business/answer/7091
    title: Tips to improve your local ranking on Google - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-7107242
    resource: https://support.google.com/business/answer/7107242
    title: Verify your business on Google - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-9157481
    resource: https://support.google.com/business/answer/9157481
    title: Manage your service areas for service-area & hybrid businesses - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-business-thread-133876833
    resource: https://support.google.com/business/thread/133876833
    title: Introducing new updates to Business Profile - Google Business Profile Community (accessed 2026-11-16)
  - id: src-whitespark-ca-blog-study-how-keywords-in-business-names-curr
    resource: https://whitespark.ca/blog/study-how-keywords-in-business-names-currently-impact-google-local-pack-rank-and-ai-search/
    title: 2026 Study — How Keywords in Business Names Impact Google Local Rankings and AI (accessed 2026-11-16)
---

Third batch of the stale-page backlog in 2026-W47: four `gbp/` pages and seven of the reference pages they cite. Eleven pages, 17 external URLs, all fetched live on 2026-11-16.

Every page in this batch carried a human `verified` entry (`human:craigburton`, July or August 2026). The differences found between those pages and the live sources were listed for the maintainer, who instructed that all of them be applied. This pass replaces the human entries with an agent entry (`anthropic/claude-fable-5-2`). The method is the one described in the [agentic report of the same date](/references/verification-report-2026-11-16-agentic.md): claim matching by `anthropic/claude-haiku-5-5` without web access, every quote machine-checked against the saved source, and every unmatched or drifted item read by the reviewing agent.

# Results

| Document | Listed claims matched to a verbatim quote | New `stale_after` | Sources reopened |
|---|---|---|---|
| [gbp/business-description.md](/gbp/business-description.md) | 11 of 21 | 2027-05-16 | [^src-support-google-com-business-answer-3038177][^src-support-google-com-business-answer-3039617] |
| [gbp/google-business-profile.md](/gbp/google-business-profile.md) | 33 of 45 | 2027-05-16 | [^src-blog-google-products-ads-commerce-connect-local-holiday-shop][^src-blog-google-products-google-plus-localnow-with-dash-of-zagat][^src-googleblog-blogspot-com-2010-04-introducing-google-places-ht][^src-smallbusiness-googleblog-com-2014-06-help-your-business-shin][^src-support-google-com-business-answer-3038177][^src-support-google-com-business-answer-7039811][^src-support-google-com-business-answer-7091][^src-support-google-com-business-thread-133876833][^src-whitespark-ca-blog-study-how-keywords-in-business-names-curr] |
| [gbp/profile-shielding.md](/gbp/profile-shielding.md) | 12 of 21 | 2027-05-16 | [^src-developers-google-com-my-business-content-accept-or-reject-u][^src-developers-google-com-my-business-reference-businessinformat][^src-support-google-com-business-answer-3038311] |
| [gbp/verification.md](/gbp/verification.md) | 30 of 42 | 2027-05-16 | [^src-support-google-com-business-answer-14271705][^src-support-google-com-business-answer-4566671][^src-support-google-com-business-answer-7107242][^src-support-google-com-business-answer-9157481] |
| [references/google-gbp-categories-description.md](/references/google-gbp-categories-description.md) | 12 of 13 | 2027-02-16 | [^src-support-google-com-business-answer-3038177] |
| [references/google-local-ranking.md](/references/google-local-ranking.md) | 8 of 13 | 2027-02-16 | [^src-support-google-com-business-answer-7091] |
| [references/google-gbp-rename-2021.md](/references/google-gbp-rename-2021.md) | 8 of 11 | 2027-02-16 | [^src-blog-google-products-ads-commerce-connect-local-holiday-shop][^src-support-google-com-business-thread-133876833] |
| [references/google-gbp-business-name-guidelines.md](/references/google-gbp-business-name-guidelines.md) | 10 of 19 | 2027-02-16 | [^src-support-google-com-business-answer-3038177] |
| [references/google-manage-google-updates.md](/references/google-manage-google-updates.md) | 8 of 8 | 2027-02-16 | [^src-developers-google-com-my-business-content-accept-or-reject-u] |
| [references/google-gbp-verification.md](/references/google-gbp-verification.md) | 11 of 16 | 2027-02-16 | [^src-support-google-com-business-answer-14271705][^src-support-google-com-business-answer-7107242] |
| [references/google-gbp-service-areas.md](/references/google-gbp-service-areas.md) | 7 of 10 | 2027-02-16 | [^src-support-google-com-business-answer-9157481] |

Unmatched items that were kept are advice, statements of absence, cross-references, or illustrations (for example the list of multi-script markets affected by the name rule). Items that were changed or removed are below.

# Corrections and removals

| Page | Was | Now | Evidence |
|---|---|---|---|
| google-local-ranking, google-business-profile | Results ranked "primarily" on relevance, distance and prominence | Google's sentence quoted as written: "mainly based on relevance, distance, and popularity"; the section heading "Prominence" is noted | [^src-support-google-com-business-answer-7091] |
| google-gbp-service-areas | SABs "hide" their address; area "capped" at two hours | SABs remove the address; two hours is Google's tip | [^src-support-google-com-business-answer-9157481] |
| verification, google-gbp-verification, two indexes | "Six methods" | Five described methods plus instant verification as a separate case; no count stated | [^src-support-google-com-business-answer-7107242] |
| verification | "unlocking the premises", "business licence", email "code", "Google offers the option to claim" | The source's own examples and wording | [^src-support-google-com-business-answer-14271705][^src-support-google-com-business-answer-7107242][^src-support-google-com-business-answer-4566671] |
| profile-shielding | "usually about ten minutes", 30 days "for sensitive fields" | Google's sentence quoted; no sensitive-field qualifier | [^src-support-google-com-business-answer-3038311] |
| google-business-profile, google-gbp-rename-2021 | App "was retired in 2022"; console "transitioned" | Stated as what Google announced it would do | [^src-blog-google-products-ads-commerce-connect-local-holiday-shop] |
| google-business-profile | Managing in Search and Maps is for "single-location businesses" | Qualifier removed | [^src-blog-google-products-ads-commerce-connect-local-holiday-shop] |
| business-description | Links, phone numbers, ALL-CAPS and emoji runs "rejected or flagged" | URLs and HTML are barred; "gimmicky character use" is named as low quality. Phone numbers, capitals and emoji are not named for descriptions | [^src-support-google-com-business-answer-3039617][^src-support-google-com-business-answer-3038177] |
| business-description | Shown on "Search and Maps"; "on small screens only the opening is visible" | Both removed | [^src-support-google-com-business-answer-3039617] |
| google-business-profile, google-gbp-business-name-guidelines | "As of the August 2026 update"; signage "previously an accepted justification"; "effective retroactively"; "risk Google editing the name" | Removed. The rule itself, with its signage clause and examples, is confirmed | [^src-support-google-com-business-answer-3038177] |

# Notes for a human reviewer

* **"Popularity."** Google's summary sentence now says popularity where this bundle, and Google's own heading, say prominence. Other pages in the bundle still use "prominence" as the factor name, which matches the heading. No wider rename was made.
* **GMB app retirement.** The 2021 announcement is the only source cited. Whether and when the app was retired is not confirmed here.
* **Date of the bilingual-name rule.** The bundle's 2026-08-23 log entry records when the rule was first seen. The guideline page carries no date, so the pages no longer state one.
* **2014 launch quote.** Confirmed on a second fetch of the Google post.[^src-smallbusiness-googleblog-com-2014-06-help-your-business-shin]
* **Not covered in this batch:** `gbp/review-gating.md`, `gbp/reviews.md` and `gbp/spam-and-fake-listings.md`, which depend on ftc.gov pages that block automated access.
