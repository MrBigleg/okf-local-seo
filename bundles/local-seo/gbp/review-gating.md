---
type: Concept
title: Review Gating
description: Where "ask happy customers first" crosses Google's review policy, and what the FTC Consumer Reviews and Testimonials Rule's text does and does not cover.
tags: [local-seo, gbp, reviews, policy, compliance]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
verified:  { by: anthropic/claude-fable-5-2, at: 2026-11-16T00:00:00Z }
status: stable
stale_after: 2027-05-16
sources:
  - id: google-maps-prohibited-and-restricted-content
    resource: /references/google-review-policy.md
    title: Google Maps — Prohibited and restricted content
  - id: doj-best-gdr-2026
    resource: /references/doj-best-gdr-2026.md
    title: "US DOJ — press release on the complaint against B.E.S.T. GDR, LLC (11 May 2026)"
  - id: ecfr-16-cfr-part-465
    resource: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
    title: "eCFR — 16 CFR Part 465, Rule on the Use of Consumer Reviews and Testimonials (accessed 2026-11-16)"
  - id: federal-register-2024-18519
    resource: https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials
    title: "Federal Register — Trade Regulation Rule on the Use of Consumer Reviews and Testimonials, 89 FR 68034 (22 August 2024; accessed 2026-11-16)"
---

Review gating is filtering customers by satisfaction before asking for a public review — typically a "how was your experience?" pre-survey that routes happy customers to Google and unhappy ones to a private feedback form. It sits in genuine tension with mainstream advice to "ask your happy customers for reviews", and since 2024 a US federal rule on reviews sits alongside the platform policy. The generation workflow it constrains is in [reviews on GBP](/gbp/reviews.md); the ranking dimension is in [reviews & reputation](/local-seo/reviews-reputation.md).

# Google's policy

Google Maps' prohibited-content policy bars merchants from conduct including, verbatim: "Discourage or prohibit negative reviews, or selectively solicit positive reviews from customers." The same policy prohibits offering incentives — payment, discounts, free goods or services — in exchange for posting, revising or removing a review, and prohibits pressuring users to review while on the premises. Merchants *may* "solicit or encourage the posting of content that does represent a genuine experience, without offering incentives". Google says incentivised or biased reviews "are not allowed and will be removed from Maps".

So the platform line is clear: ask everyone, incentivise no one.

# The FTC Consumer Reviews and Testimonials Rule

The FTC's Rule on the Use of Consumer Reviews and Testimonials (16 CFR Part 465) took effect on **21 October 2024**.[^federal-register-2024-18519] Provisions relevant to review programmes, from the rule text:[^ecfr-16-cfr-part-465]

* **§465.2** — fake or false reviews (including buying, selling or creating them).
* **§465.4** — compensation or incentives **conditioned on the review's sentiment**, positive or negative, express or implied. Incentives for reviews as such are not banned by this rule; incentives for *positive* reviews are (and remain banned by Google's stricter policy either way).
* **§465.5** — undisclosed insider reviews (owners, employees, relatives).
* **§465.7** — review suppression: false accusations against reviewers, or presenting a review set as complete while hiding negatives.

On gating specifically, the rule text contains no provision on asking only satisfied customers for reviews. Its prohibitions that touch review requests are the sentiment-conditioned incentive in §465.4 and the insider-review provisions in §465.5, and §465.5 does not apply to "generalized solicitations to purchasers" to post reviews about their experience.[^ecfr-16-cfr-part-465] This page makes no statement about how the FTC treats gating outside the rule: the FTC's own guidance pages could not be reopened for this bundle and are no longer cited. Gating does breach Google's policy, as set out above.

# Enforcement

* The Rule was invoked in the May 2026 federal complaint over mass fake listings and fabricated reviews[^doj-best-gdr-2026] — see [spam & fake listings](/gbp/spam-and-fake-listings.md).

# Safe pattern vs risk pattern

| Safe | Risk |
|------|------|
| Ask **every** customer, through the same flow, at the same moment. | Pre-survey that routes only satisfied customers to Google. |
| Internal satisfaction surveys, run separately from review requests. | Survey that suppresses the review ask when the score is low. |
| Respond to negatives and resolve offline; invite an updated review afterwards. | Incentives to remove or revise a negative review. |
| Incentive-free requests via link or QR code. | Any incentive tied to sentiment; any incentive at all on Google. |
