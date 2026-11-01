---
type: Playbook
title: Reviews on GBP
description: GBP-specific review mechanics — the response flow, a generation workflow with review links and QR codes, handling problematic reviews, and what measured deletion data adds.
tags: [local-seo, gbp, reviews]
generated: { by: iris/2026-W44, at: 2026-11-01T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-07-06T00:00:00Z }
status: stable
stale_after: 2026-10-06
sources:
  - id: reviewflowz-gone-in-7-days
    resource: /references/reviewflowz-review-deletion-2026.md
    title: Reviewflowz with Cartelis — Google review deletions, measured (October 2026)
  - id: soci-cbi-2025
    resource: /references/soci-cbi-2025.md
    title: SOCi 2025 Consumer Behavior Index
  - id: google-tips-to-get-more-reviews
    resource: https://support.google.com/business/answer/3474122
    title: Google — Tips to get more reviews
  - id: google-maps-prohibited-and-restricted-content
    resource: /references/google-review-policy.md
    title: Google Maps — Prohibited and restricted content
  - id: ftc-consumer-review-rule
    resource: /references/ftc-consumer-review-rule.md
    title: "FTC — Consumer Reviews and Testimonials Rule: Questions and Answers"
---

This is the operational playbook for reviews on a [Google Business Profile](/gbp/google-business-profile.md). The ranking dimension — recency, thresholds, the 18-day rule — lives in [reviews & reputation](/local-seo/reviews-reputation.md); cross-platform velocity and fake-review detection live in [review intelligence](/maps/review-intelligence.md).

Why the effort is justified: in the 2025 SOCi Consumer Behavior Index (1,001 US adults, February 2025), **91% of consumers rely on peer-generated content to evaluate local businesses**, and among younger consumers **65% say they are more likely to choose a business that actively responds to reviews**.

# Response flow

Reviews are read and answered from the profile management surface in Google Search or the Maps app (the Reviews section). Google's own response guidance:

1. **Respond to everything**, positive and negative — response behaviour is visible to every future reader, not just the reviewer.
2. Keep replies **professional, short and personalised**; don't use replies as advertising.
3. For negatives: acknowledge, apologise where warranted, state the fix, and move detail offline. Never make accusations about the reviewer (see problematic reviews below).
4. Respond promptly — a stale unanswered negative does compounding damage.

Industry constraints (healthcare/HIPAA, legal privilege) are noted in [reviews & reputation](/local-seo/reviews-reputation.md).

# Generation workflow

Google explicitly supports asking for reviews — it provides each verified profile with a shareable **review link and QR code** for exactly this purpose. What it prohibits is filtering who you ask and paying for outcomes (see [review gating](/gbp/review-gating.md)).

1. **Get the short link / QR code** from the profile's "Ask for reviews" facility.
2. **Ask everyone, systematically** — build the ask into the moment the job finishes or the order completes, not an occasional campaign. Asking all customers is both the policy-safe pattern and what keeps velocity steady.
3. **Match the channel to the customer**: SMS or email follow-up with the link for remote customers; the QR code on receipts, invoices, packaging, table cards or the van for in-person ones.
4. **Never offer incentives.** Google treats free or discounted goods in exchange for reviews as fake and misleading content, and incentives conditioned on sentiment breach the FTC rule — details in [review gating](/gbp/review-gating.md).
5. **Respond as they arrive** — the response flow above is part of generation: visible responses raise the perceived value of leaving a review.

# Handling problematic reviews

* **Policy-violating content** (spam, off-topic, conflict of interest, harassment, fake) — report it through the profile's review-reporting flow against Google's prohibited-content policy, and document what you reported. Removal is Google's decision; report and move on rather than replying in kind.
* **Genuine negatives** — not removable and not worth fighting: respond with the flow above. A visible, calm owner response is read by prospects as a trust signal.
* **Suspected fake attacks** — the detection heuristics (timing, account history, text similarity) are in [review intelligence](/maps/review-intelligence.md); report matches through the same flow.
* **Never pay for removal or revision.** Offering money, discounts or goods for changing or deleting a negative review breaches Google policy, and the FTC has stated that such incentives can be an unfair practice under the FTC Act.

# What measured deletion data adds

Google does not document when or why it removes reviews that were already published. The largest public measurement of that behaviour is the [4.9M-review Reviewflowz/Cartelis panel](/references/reviewflowz-review-deletion-2026.md), which found that **just under 2% of new reviews are deleted within a week**, that deletions cluster in a review's first seven days (negative reviews on days 2–3, positive on days 6–7, roughly a tenth of that risk from day 8), and that deletion concentrates: 1% of businesses accounted for half of all deletions in the panel.

Two findings are operationally relevant to the flow above, and both are **associations in vendor research rather than demonstrated causes**:

* **Reply timing correlated with retention.** A positive review answered within two days was deleted at 1.5% against 2.4% for unanswered positive reviews. Whether the reply came the same day or on day two made no measurable difference, and there was no measurable effect on 1-star reviews. Reply promptness is justified by customer experience regardless, so treat this as a reason to keep the habit, not as a retention tactic to optimise.
* **Single-day bursts correlated with deletion; busy months did not.** Reviews posted on a day with at least three positive reviews and at least four times the business's usual daily count were deleted 1.8× more often, while a month three times busier than normal showed no increase. Spreading asks across days is consistent with the systematic, always-on generation workflow above.

The panel observes only reviews that appeared and were later removed, so it says nothing about reviews withheld before publication, and it records deletions without their cause. It is a measurement of an undocumented behaviour, not a statement of Google policy.
