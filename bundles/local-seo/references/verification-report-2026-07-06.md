---
type: Report
title: Verification report — 2026-07-06
description: Claim-by-claim fact-check of the new gbp/ section against primary sources, completed 6 July 2026.
verified_on: 2026-07-06
verifier: CTB Marketing (bundle maintainer)
tags: [governance, verification, gbp]
timestamp: 2026-07-06T00:00:00Z
---

Checked against primary sources on 6 July 2026, before the `gbp/` section was written. Each row records the claim as it arrived from internal notes, the verification result, and the primary source consulted. See the [maintenance policy](/maintenance.md) for review cadence.

# Results

| Document | Claim | Result | Primary source |
|---|---|---|---|
| `gbp/google-business-profile.md` | Google's local ranking factors are relevance, distance, prominence | Verified, with Google's definitions quoted; prominence explicitly considers links and review count, and Google states ranking cannot be requested or paid for. | https://support.google.com/business/answer/7091 |
| `gbp/google-business-profile.md` | GMB was renamed Google Business Profile in 2021 | Verified against Google's own live announcement: "Connect with local holiday shoppers" (Matt Madrigal, **4 November 2021**) — "To keep things simple, 'Google My Business' is being renamed 'Google Business Profile.'" Corroborated by Google's Business Profile Community announcement (app retirement 2022, Business Profile Manager, Business Profile API). | https://blog.google/products/ads-commerce/connect-local-holiday-shoppers/ |
| `gbp/google-business-profile.md` | Pre-2014 lineage (Local Business Center → Places → Google+ Local) | Verified with exact dates from Google's own live posts: Local Business Center became Google Places **20 April 2010** ("Introducing Google Places"); Google+ Local launched **30 May 2012** (owners kept managing via Google Places for Business); Google My Business launched **11 June 2014**, "upgrading current users of Places for Business and the Google+ Dashboard". | https://googleblog.blogspot.com/2010/04/introducing-google-places.html; https://blog.google/products/google-plus/localnow-with-dash-of-zagat-and/; https://smallbusiness.googleblog.com/2014/06/help-your-business-shine-with-google-my.html |
| `gbp/business-description.md` | Description limit is 750 characters | Verified; shown in the "From the business" section; no URLs or HTML allowed. | https://support.google.com/business/answer/3039617 |
| `gbp/business-description.md` | Description content rules | Verified: no links of any type; don't emphasise promotions/prices; no gimmicky or low-quality content; "upfront and honest". | https://support.google.com/business/answer/3038177 |
| `gbp/reviews.md` | "91% of consumers use reviews to evaluate local businesses" (2025 SOCi CBI) | Verified with wording correction: **"91% of consumers rely on peer-generated content to evaluate local businesses"** (all respondents; survey 19–24 Feb 2025, n=1,001 US adults; released 4 June 2025). | https://www.prnewswire.com/news-releases/ai-suggests-humans-decide-soci-warns-brands-to-embrace-human-validation-or-get-left-behind-302472784.html |
| `gbp/reviews.md` | "65% more likely to choose a business that responds to reviews" (2025 SOCi CBI) | Corrected scope: the primary release presents the 65% figure in the context of **younger audiences**, not all consumers. Cited as younger-consumers. | https://www.prnewswire.com/news-releases/ai-suggests-humans-decide-soci-warns-brands-to-embrace-human-validation-or-get-left-behind-302472784.html |
| `gbp/reviews.md` | Google supports review links and QR codes; incentives prohibited | Verified: Google's own "Tips to get more reviews" page provides the link/QR facility and prohibits incentives as "fake & misleading content". | https://support.google.com/business/answer/3474122 |
| `gbp/google-posts.md` | Post types are Update, Offer, Event | Verified, including required/optional fields per type, placement (Updates/Overview tab on mobile; "From the owner" on desktop), and 6-month archiving of undated posts. | https://support.google.com/business/answer/7342169 |
| `gbp/google-posts.md` | Crate & Barrel + Uberall case study | Verified against the vendor-published case study: **+31% Google Maps views and +6% Google Search views, 2024 vs 2023**, across 161 locations, with 95% profile completeness. Cited with vendor-published, correlation-not-experiment caveats. | https://uberall.com/en-us/customers/how-crate-barrel-grew-google-visibility-by-31-while-saving-time |
| `gbp/verification.md` | Five verification methods (postcard, phone, email, video, live walkthrough) | Corrected: the current help page lists **six** — video recording, phone/text, email, live video call, postcard, and instant verification via Search Console. | https://support.google.com/business/answer/7107242 |
| `gbp/verification.md` | Method is auto-assigned by business category | Verified with broader wording: methods "are automatically determined by Google and can't be changed", based on business type, public info, region and hours. | https://support.google.com/business/answer/7107242 |
| `gbp/verification.md` | Review window "up to 5 business days" | Verified; also: codes expire after 30 days, postcards mostly arrive within 14 days. | https://support.google.com/business/answer/7107242 |
| `gbp/verification.md` | Video verification requirements | Verified: continuous unedited live recording ≥30 seconds showing location/signage, business evidence, and proof of management. | https://support.google.com/business/answer/14271705 |
| `gbp/verification.md` | Ownership-request flow | Verified: current owner is notified and has 3 days to respond. | https://support.google.com/business/answer/4566671 |
| `gbp/verification.md` | SAB/hybrid rules | Verified: SABs clear the address and set up to 20 service areas (city/postal-code based, ~2 hours' driving guidance); hybrids keep address + hours and add areas. | https://support.google.com/business/answer/9157481 |
| `gbp/spam-and-fake-listings.md` | DOJ action against "BEST"/Premium Home Service, individual Yossef Bernath | Verified with corrections: complaint filed **11 May 2026** (N.D. Illinois) against B.E.S.T. GDR, LLC d/b/a Premium Home Service and CEO **Yosef** Bernath (one "s"); DOJ states **over 15,000 fake Google Search/Maps profiles**. | https://www.justice.gov/opa/pr/department-justice-files-complaint-against-best-gdr-llc-doing-business-premium-home-service |
| `gbp/spam-and-fake-listings.md` | "~$79M in gains" | **Dropped/replaced**: not in the DOJ release, FTC release, or the filed complaint. The complaint alleges "tens of millions of dollars" from "well over 100,000 consumers" since at least 2018, via 7,600+ phone numbers in 250+ area codes. The $79M figure traces to KARE 11 investigative reporting and is noted as such. | https://www.ftc.gov/system/files/ftc_gov/pdf/premium_home_service_-_filed_complaint.pdf |
| `gbp/profile-shielding.md` | `hasGoogleUpdated` flag and `diffMask` | Verified: `metadata.hasGoogleUpdated`; `locations.getGoogleUpdated` returns `diffMask` (differences needing action) and `pendingMask` (own edits in review). | https://developers.google.com/my-business/content/accept-or-reject-updates |
| `gbp/profile-shielding.md` | Revert via PATCH | Verified: accept and reject both use `locations.patch` with an `updateMask` — accept by patching Google's value, reject by re-asserting your own. | https://developers.google.com/my-business/content/accept-or-reject-updates |
| `gbp/profile-shielding.md` | "Google updates" pending-edit banner | Verified as a notification plus an alert in the profile's Edit profile section; the word "banner" is not in the primary source, so the doc uses Google's wording. Owner-edit review timing (≈10 minutes, up to 30 days) verified on the same page. | https://support.google.com/business/answer/3038311 |
| `gbp/review-gating.md` | Google policy bars selective solicitation | Verified verbatim: merchants must not "discourage or prohibit negative reviews, or selectively solicit positive reviews from customers"; incentivised reviews prohibited. | https://support.google.com/contributionpolicy/answer/7400114 |
| `gbp/review-gating.md` | FTC rule effective 21 October 2024 | Verified (16 CFR Part 465); the FTC's Q&A states gating is not specifically prohibited by the rule but could violate the FTC Act (Endorsement Guides 16 CFR 255.2(d), (e)(11)). | https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers |
| `gbp/review-gating.md` | December 2025 FTC warning letters | Verified: 22 December 2025, ten companies, civil-penalty exposure up to $53,088 per violation; letters are warnings, not adjudications. | https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-warns-10-companies-about-possible-violations-agencys-new-consumer-review-rule |

# Claims requiring human follow-up

None. Three items initially flagged here were resolved on 6 July 2026:

* **GMB→GBP announcement primary source** — resolved. Google's announcement is live at blog.google under ads-commerce ("Connect with local holiday shoppers", 4 November 2021); the trade-press citation was replaced. See [the rename reference](/references/google-gbp-rename-2021.md).
* **Pre-2014 product lineage dates** — resolved. Google's original announcements for Places (2010), Google+ Local (2012) and Google My Business (2014) are all live on Google-owned domains; the lineage is now stated with exact dates and quoted wording.
* **SOCi 65% figure scope** — resolved by policy: the bundle's truth of record is the citable primary release, which presents the figure in the context of younger audiences, and the bundle cites it with exactly that scope. The full CBI report is gated; nothing gated is treated as citable. If SOCi publishes an ungated statement with a different scope, update [the SOCi reference](/references/soci-cbi-2025.md) first, then the citing documents.

# Citations

[1] [Tips to improve your local ranking on Google](https://support.google.com/business/answer/7091)

[2] [Verify your business on Google](https://support.google.com/business/answer/7107242)

[3] [Manage Google Updates](https://developers.google.com/my-business/content/accept-or-reject-updates)

[4] [DOJ press release — B.E.S.T. GDR, LLC (11 May 2026)](https://www.justice.gov/opa/pr/department-justice-files-complaint-against-best-gdr-llc-doing-business-premium-home-service)

[5] [FTC — Consumer Reviews and Testimonials Rule Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)
