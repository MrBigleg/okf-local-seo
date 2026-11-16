---
type: Report
title: Reviews, spam and remaining references verification report — 2026-11-16
description: Removal of the ftc.gov citations that could not be reopened, and a claim-by-claim review of three GBP pages and eleven reference pages.
tags: [governance, verification, gbp, reviews, maintenance]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
status: draft
sources:
  - id: src-ahrefs-com-blog-ai-overview-brand-correlation
    resource: https://ahrefs.com/blog/ai-overview-brand-correlation/
    title: An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied) (accessed 2026-11-16)
  - id: src-developers-google-com-search-docs-appearance-ai-features
    resource: https://developers.google.com/search/docs/appearance/ai-features
    title: AI Features and Your Website — Google Search Central | Documentation | Google for Developers (accessed 2026-11-16)
  - id: src-opers-google-com-search-docs-appearance-structured-data-local-business
    resource: https://developers.google.com/search/docs/appearance/structured-data/local-business
    title: Local Business (LocalBusiness) Structured Data — Google Search Central | Documentation | Google for Developers (accessed 2026-11-16)
  - id: src-velopers-google-com-search-docs-appearance-structured-data-sd-policies
    resource: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
    title: General Structured Data Guidelines — Google Search Central | Documentation | Google for Developers (accessed 2026-11-16)
  - id: src-schema-org-localbusiness
    resource: https://schema.org/LocalBusiness
    title: LocalBusiness - Schema.org Type (accessed 2026-11-16)
  - id: src-support-google-com-business-answer-3474122
    resource: https://support.google.com/business/answer/3474122
    title: Tips to get more reviews - Google Business Profile Help (accessed 2026-11-16)
  - id: src-support-google-com-contributionpolicy-answer-7400114
    resource: https://support.google.com/contributionpolicy/answer/7400114
    title: Prohibited & restricted content - Maps User Generated Content Policy Help (accessed 2026-11-16)
  - id: src-brightlocal-com-research-are-businesses-using-apple-business-connect
    resource: https://www.brightlocal.com/research/are-businesses-using-apple-business-connect/
    title: (Poll) Are Businesses Using Apple Business Connect? - BrightLocal (accessed 2026-11-16)
  - id: src-brightlocal-com-research-local-consumer-review-survey
    resource: https://www.brightlocal.com/research/local-consumer-review-survey/
    title: LCRS 2026 — Study Shows Reviews Matter More Than Ever - BrightLocal (accessed 2026-11-16)
  - id: src-ecfr-gov-current-title-16-chapter-i-subchapter-d-part-465
    resource: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
    title: eCFR — — 16 CFR Part 465 -- Rule on the Use of Consumer Reviews and Testimonials (accessed 2026-11-16)
  - id: src-trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials
    resource: https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials
    title: Federal Register — — Trade Regulation Rule on the Use of Consumer Reviews and Testimonials (accessed 2026-11-16)
  - id: src-les-complaint-against-best-gdr-llc-doing-business-premium-home-service
    resource: https://www.justice.gov/opa/pr/department-justice-files-complaint-against-best-gdr-llc-doing-business-premium-home-service
    title: Office of Public Affairs — Department of Justice Files Complaint Against B.E.S.T. GDR, LLC, Doing Business As Premium Home Service, and its CEO Yosef Bernath for Violations of the FTC Act and Related Laws — United States Department of Justice (accessed 2026-11-16)
  - id: src-of-reviews-siri-search-googles-new-in-stock-check-its-ad-revenue-miss
    resource: https://www.nearmedia.co/ep-280-why-google-deletes-2-of-reviews-siri-search-googles-new-in-stock-check-its-ad-revenue-miss/
    title: EP 280- Why Google Deletes 2% of Reviews, Siri Search, Google’s New In-Stock Check & Its Ad Revenue Miss (accessed 2026-11-16)
  - id: src-s-brands-to-embrace-human-validation-or-get-left-behind-302472784-html
    resource: https://www.prnewswire.com/news-releases/ai-suggests-humans-decide-soci-warns-brands-to-embrace-human-validation-or-get-left-behind-302472784.html
    title: AI Suggests, Humans Decide — SOCi Warns Brands to Embrace Human Validation or Get Left Behind (accessed 2026-11-16)
  - id: src-reviewflowz-com-research-disappearing-google-reviews
    resource: https://www.reviewflowz.com/research/disappearing-google-reviews
    title: Why Google Reviews Disappear — 10 Stats From 4.9M Reviews (accessed 2026-11-16)
  - id: src-nsights-case-study-6-learnings-about-how-traffic-from-chatgpt-converts
    resource: https://www.seerinteractive.com/insights/case-study-6-learnings-about-how-traffic-from-chatgpt-converts
    title: Case Study — 6 Learnings, 1 site - How Traffic from ChatGPT Converts (accessed 2026-11-16)
  - id: src-soci-ai-insights-consumer-behavior-index
    resource: https://www.soci.ai/insights/consumer-behavior-index
    title: How Consumers Discover Local Businesses in 2026 — SOCi Local Discovery Index (accessed 2026-11-16)
  - id: src-sterlingsky-ca-number-of-reviews-impact-ranking
    resource: https://www.sterlingsky.ca/number-of-reviews-impact-ranking/
    title: 2025 UPDATE — Does the Number of Google Reviews Impact Ranking? (Case Study) (accessed 2026-11-16)
---

Fourth batch of the stale-page backlog in 2026-W47. It does two things: it removes every citation of ftc.gov from the bundle, and it re-verifies the three `gbp/` pages that were waiting on that decision together with eleven reference pages. Fourteen pages, 18 external URLs, all fetched live on 2026-11-16. The method is the one described in the [agentic report of the same date](/references/verification-report-2026-11-16-agentic.md).

All fourteen pages carried a human `verified` entry or one from an earlier agent pass. This pass records an agent entry (`anthropic/claude-fable-5-2`). No human has reviewed it before filing.

# The ftc.gov citations

Four ftc.gov URLs returned an "abusive automated request" block page to every automated fetch, including a browser. They could not be reopened, so by the maintainer's instruction the citations were removed, together with every claim that rested only on them.

| Removed | Where it was |
|---|---|
| The reference page `references/ftc-consumer-review-rule.md` | Deleted; its index entry removed; one historical log link unlinked |
| The FTC Q&A quotation on asking only happy customers, and the reading that gating "could violate the FTC Act" | review-gating |
| The $53,088-per-violation figure and the 22 December 2025 warning letters | review-gating |
| "The FTC has stated that such incentives can be an unfair practice under the FTC Act" | reviews |
| "Risks FTC enforcement" | local-seo/reviews-reputation |
| Complaint-only figures (since 2018, over 100,000 consumers, "tens of millions of dollars", 7,600 phone numbers) and the "$79 million" clarification | spam-and-fake-listings, doj-best-gdr-2026 |

**What was kept, on other primary sources.** The rule itself is published outside ftc.gov. The provisions summarised on the review-gating page (§465.2, §465.4, §465.5, §465.7) and the "generalized solicitations" exemption were confirmed in the eCFR text of 16 CFR Part 465,[^src-ecfr-gov-current-title-16-chapter-i-subchapter-d-part-465] and the 21 October 2024 effective date in the Federal Register notice.[^src-trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials] Both are now cited directly. The May 2026 complaint is described from the DOJ press release alone.[^src-les-complaint-against-best-gdr-llc-doing-business-premium-home-service] This re-sourcing goes one step beyond "remove": if the maintainer prefers the rule content gone as well, it is one section on one page.

**Consequence a reader should know.** The bundle no longer says anything about how the FTC treats review gating outside the rule text. The review-gating page states that gap in so many words.

# Results

| Document | Listed claims matched to a verbatim quote | New `stale_after` | Sources reopened |
|---|---|---|---|
| [gbp/review-gating.md](/gbp/review-gating.md) | 16 of 21 | 2027-05-16 | [^src-support-google-com-contributionpolicy-answer-7400114][^src-ecfr-gov-current-title-16-chapter-i-subchapter-d-part-465][^src-trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials] |
| [gbp/reviews.md](/gbp/reviews.md) | 27 of 37 | 2027-05-16 | [^src-support-google-com-business-answer-3474122][^src-support-google-com-contributionpolicy-answer-7400114][^src-ecfr-gov-current-title-16-chapter-i-subchapter-d-part-465][^src-of-reviews-siri-search-googles-new-in-stock-check-its-ad-revenue-miss][^src-s-brands-to-embrace-human-validation-or-get-left-behind-302472784-html][^src-reviewflowz-com-research-disappearing-google-reviews][^src-soci-ai-insights-consumer-behavior-index] |
| [gbp/spam-and-fake-listings.md](/gbp/spam-and-fake-listings.md) | 14 of 21 | 2027-05-16 | [^src-support-google-com-contributionpolicy-answer-7400114][^src-les-complaint-against-best-gdr-llc-doing-business-premium-home-service] |
| [references/ahrefs-ai-overviews.md](/references/ahrefs-ai-overviews.md) | 6 of 9 | 2027-02-16 | [^src-ahrefs-com-blog-ai-overview-brand-correlation] |
| [references/brightlocal-apple-business-connect.md](/references/brightlocal-apple-business-connect.md) | 3 of 4 | 2027-02-16 | [^src-brightlocal-com-research-are-businesses-using-apple-business-connect] |
| [references/brightlocal-lcrs.md](/references/brightlocal-lcrs.md) | 7 of 9 | 2027-02-16 | [^src-brightlocal-com-research-local-consumer-review-survey] |
| [references/doj-best-gdr-2026.md](/references/doj-best-gdr-2026.md) | 14 of 17 | 2027-02-16 | [^src-les-complaint-against-best-gdr-llc-doing-business-premium-home-service] |
| [references/google-ai-optimization-guide.md](/references/google-ai-optimization-guide.md) | 3 of 6 | 2027-02-16 | [^src-developers-google-com-search-docs-appearance-ai-features] |
| [references/google-local-business-structured-data.md](/references/google-local-business-structured-data.md) | 4 of 8 | 2027-02-16 | [^src-opers-google-com-search-docs-appearance-structured-data-local-business][^src-velopers-google-com-search-docs-appearance-structured-data-sd-policies] |
| [references/google-review-policy.md](/references/google-review-policy.md) | 4 of 11 | 2027-02-16 | [^src-support-google-com-contributionpolicy-answer-7400114] |
| [references/schema-org-localbusiness.md](/references/schema-org-localbusiness.md) | 9 of 13 | 2027-02-16 | [^src-schema-org-localbusiness] |
| [references/seer-chatgpt-conversion.md](/references/seer-chatgpt-conversion.md) | 4 of 6 | 2027-02-16 | [^src-nsights-case-study-6-learnings-about-how-traffic-from-chatgpt-converts] |
| [references/soci-cbi-2025.md](/references/soci-cbi-2025.md) | 12 of 15 | 2027-02-16 | [^src-s-brands-to-embrace-human-validation-or-get-left-behind-302472784-html][^src-soci-ai-insights-consumer-behavior-index] |
| [references/sterling-sky.md](/references/sterling-sky.md) | 3 of 7 | 2027-02-16 | [^src-sterlingsky-ca-number-of-reviews-impact-ranking] |

# Other corrections and removals

| Page | Change | Evidence |
|---|---|---|
| review-gating | Enforcement sentence replaced by Google's own: incentivised or biased reviews "are not allowed and will be removed from Maps". The broader "feature limits and account suspension" wording appears in the policy only under child safety | [^src-support-google-com-contributionpolicy-answer-7400114] |
| reviews | "each verified profile" and the "Ask for reviews facility" removed; Google's page says only that a link or QR code can be created | [^src-support-google-com-business-answer-3474122] |
| spam-and-fake-listings | Tactic list reduced to what the DOJ release states: no keyword-loaded name examples, no "five-star", no "bury one-star reviews", no area codes; "postcards were spoofable at scale" and "redressal channels" removed | [^src-les-complaint-against-best-gdr-llc-doing-business-premium-home-service] |
| brightlocal-lcrs | Scope "primarily US/UK respondents" corrected to a panel of 1,002 US adults | [^src-brightlocal-com-research-local-consumer-review-survey] |
| google-ai-optimization-guide | "Runs on the same systems as ordinary Search" replaced by Google's sentence that there are no additional requirements | [^src-developers-google-com-search-docs-appearance-ai-features] |
| google-local-business-structured-data | "Policy violation" corrected to "manual action"; the Product and Recipe aside removed | [^src-velopers-google-com-search-docs-appearance-structured-data-sd-policies] |
| google-review-policy | Title aligned to the page's own; scope now notes that Google says violating reviews are removed | [^src-support-google-com-contributionpolicy-answer-7400114] |
| schema-org-localbusiness | "30+ subtypes such as Restaurant and Store" reduced to "more specific subtypes"; the fetched page text carries no list or count | [^src-schema-org-localbusiness] |
| seer-chatgpt-conversion | Title aligned; publication date 3 June 2025 added | [^src-nsights-case-study-6-learnings-about-how-traffic-from-chatgpt-converts] |
| soci-cbi-2025 | Sentence about the index page's wording removed; a note records that the index URL now shows a different report | [^src-soci-ai-insights-consumer-behavior-index][^src-s-brands-to-embrace-human-validation-or-get-left-behind-302472784-html] |
| sterling-sky | 18-day rule quoted as published ("fall off a cliff", "even three weeks"); "drawn from client case studies" removed | [^src-sterlingsky-ca-number-of-reviews-impact-ranking] |

# Notes for a human reviewer

* **18-day rule wording elsewhere.** Other pages describe it as a case-study observation of "two to three weeks". The cited Sterling Sky post says three weeks and does not tie the rule to client case studies. Those pages were not in this batch and were not changed.
* **SOCi.** The 2025 Consumer Behavior Index is no longer at its cited URL. The reference survives on the press release; consider replacing it with the 2026 report.
* **schema.org subtypes.** The subtype list is likely on the page in a section the text fetch dropped. A person can restore the count after looking.
* **Five stale pages remain**, all of them earlier verification reports. A report is a dated record of a past pass; reopening its sources would make it a different report. They were left alone. Whether reports should carry `stale_after` at all is a tooling question for the maintainer.
