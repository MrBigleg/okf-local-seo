---
type: Reference
title: Google review deletions — measured rates, timing and correlates
description: A 4.9-million-review panel measuring how often Google deletes new reviews, when in a review's first two weeks deletions happen, and which business, reviewer and behaviour traits associate with higher deletion rates.
resource: https://www.reviewflowz.com/research/disappearing-google-reviews
publisher: Reviewflowz (review-management software) with Cartelis (data and CRM consultancy)
published: 2026-10 (report published October 2026; measurement window 11–24 August 2026)
accessed: 2026-11-01
confidence: medium
scope: Covers observed deletion rates for new and existing Google reviews, the day-by-day distribution of deletions within a review's first two weeks, and measured associations with owner reply timing, review-spike days versus busy months, reviewer account history, star rating, and profile rating mix. Vendor research — the publisher sells review management, the figures are associations rather than causes, and the study observes only reviews that appeared and were then removed. Studies reviews that were published and then deleted, so it does not measure reviews withheld before publication, does not explain why any individual review was removed, and makes no claim about ranking or visibility effects for a business with deleted reviews.
tags: [reference, reviews, gbp, review-deletion, review-removal, vendor-research]
generated: { by: iris/2026-W44, at: 2026-11-01T00:00:00Z }
status: draft
stale_after: 2027-02-01
sources:
  - id: reviewflowz-gone-in-7-days
    resource: https://www.reviewflowz.com/research/disappearing-google-reviews
    title: Reviewflowz with Cartelis — "Gone in 7 Days: why Google reviews disappear" (October 2026)
  - id: near-media-ep-280
    resource: https://www.nearmedia.co/ep-280-why-google-deletes-2-of-reviews-siri-search-googles-new-in-stock-check-its-ad-revenue-miss/
    title: Near Media EP 280 — discussion of the study, 29 October 2026
  - id: google-contribution-policy
    resource: https://support.google.com/contributionpolicy/answer/7400114
    title: Google contribution policy — fake and misleading content, reviews
---

A panel study of what Google actually removes from Google Maps profiles. It is the largest public dataset on review deletion that this bundle has reviewed, and it measures a surface that policy documents do not describe: which already-published reviews disappear, and when.

**Treat it as directional evidence, not as Google's enforcement criteria.** The publisher sells review-management software, the results are associations rather than demonstrated causes, and Google publishes no documentation of these mechanics. The figures below are reproduced with attribution as the study permits; the interpretation is limited to what the data can carry.

# What the study measured

| Item | Value |
|---|---|
| Reviews tracked | 4,876,933 |
| Profiles | 9,048 Google Maps profiles, in seven industries and three group sizes, half US and half Europe |
| Countries | 41 |
| Measurement window | Daily crawls from 11 to 24 August 2026 (14 crawls) |
| Deletions observed | 4,590 |
| Deletion definition | A review present in one complete listing and absent from the next; a crawl that did not reach the end of a listing does not count |
| Brands excluded from comparative figures | Six brands hit by mass removals, excluded because a single purge moves every average |

# What the study establishes

* **Just under 2% of new reviews are deleted within a week** — 1.95% across the panel.
* **Deletions are concentrated.** 13% of businesses lost at least one review over two weeks, and **1% of businesses account for half of all deletions**.
* **Google removes the extremes.** Deletion rates within the first week by rating: 5.7% (1-star), 2.2% (2-star), 0.9% (3-star), 1.0% (4-star), 1.8% (5-star). Within the same business a 1-star review is 3.9× more likely to be deleted than a 4-star one. 1- and 2-star reviews are 9% of all reviews and 20% of deletions.
* **Deletions barely move ratings.** For businesses that lost five or more reviews, the average rating changed by 0.01 star.

## The first-week window

The study reports a consistent daily pattern rather than a continuous risk:

* negative reviews disappear mainly on **day 2 and day 3**;
* positive reviews disappear mainly on **day 6 and day 7**, regardless of the day of the week they were posted;
* by day 7, **1.7%** of new positive reviews and **4.7%** of negative reviews are gone;
* from **day 8**, daily deletion risk falls to roughly **0.1% a day** — about a tenth of the day-7 rate.

The study's own operational reading is that a review campaign should be judged on what remains published on day 8.

# Measured associations

| Factor | Result |
|---|---|
| Owner reply to a **positive** review within two days | 1.5% deleted against 2.4% without a reply. Same-day, next-day and day-2 replies gave similar deletion odds (0.46, 0.52, 0.51 against no reply). The study states this is an association, not a proven cause. |
| Owner reply to a **1-star** review | No measurable difference (4.9% against 6.0%). |
| **Spike day** — at least 3 positive reviews *and* at least 4× the business's usual daily count | Reviews posted that day were deleted 1.8× more often. The effect is strongest in Europe (0.9% → 2.2%); in the US the difference was too small to be certain of (2.1% → 2.4%). |
| **Busy month** — a month three times busier than normal | No increase (1.1% against 1.9%). The study reads the pattern as a reaction to individual days, not to monthly volume. |
| Reviewer account history | A first review was deleted 5.6× more often than a review from a Local Guide of level 6 or above. First-review accounts wrote 14% of reviews and took 22% of deletions. Where the author could be traced, about one deletion in five was Google removing the whole account, which removes that person's reviews from every business. |
| Profile at **85%+ five-star** | 0.13–0.14% of reviews deleted over two weeks against 0.03% for profiles at 50–70%: 2.2× at equal sector, size and volume. On profiles rated 4.8 and above, a 4-star review was deleted 9× more often than on profiles under 4.5. |
| Review length, images, stock phrases such as "highly recommended" | No measurable effect on deletion. |

## Regional and sector variation

New positive reviews deleted within their first week:

| Sector | Europe | US |
|---|---:|---:|
| Home services | 3.3% | 4.1% |
| Healthcare | 0.6% | 3.4% |
| Wellness and fitness | 1.6% | 3.0% |
| Travel | 1.0% | 2.5% |
| Automotive | 1.9% | 1.1% |
| Food and beverage | 0.7% | 1.0% |
| Hospitality | 0.9% | 0.4% |

* Over two weeks, Google deleted 0.09% of existing reviews on US profiles against 0.04% in Europe.
* Spain had the highest share of new reviews deleted within a week (2.9%), ahead of the US (2.4%), Germany (1.8%), France (1.4%) and Italy (0.9%).
* US groups of four to ten locations were the most exposed size segment, at 0.11% of their reviews over two weeks.

# What this study cannot tell you

Limitations stated by the study itself, plus one that follows from its method:

* Two weeks in **August** — seasonality is not covered.
* It records that a review was deleted, not **why**: user flags, reports, legal requests and reviewers deleting their own reviews all register identically.
* Reviews blocked **before publication** are invisible to it, so it measures deletion of published reviews only. It is not a measure of total review suppression.
* The **UK** is not in the panel.
* Results are **associations, not causes**. Google does not expose which reviews were flagged or why.

# A note on staff names

The study reports that reviews naming a staff member were deleted at effectively the same rate as any other (1.01× within the same business, across 2.7 million positive reviews). It also observes that since April 2026 Google's contribution policy tells businesses not to direct staff to request reviews that identify a staff member, and comments that it found no evidence of that rule being enforced through review deletion.

These are two different questions. The measurement is about deletion rates; the policy is about what businesses are permitted to request. This bundle records the measurement and the policy side by side and does not treat the former as permission for the latter.

Sources: Reviewflowz with Cartelis, https://www.reviewflowz.com/research/disappearing-google-reviews (published October 2026, accessed 2026-11-01); discussion and caveats in Near Media EP 280, https://www.nearmedia.co/ep-280-why-google-deletes-2-of-reviews-siri-search-googles-new-in-stock-check-its-ad-revenue-miss/ (29 October 2026); Google contribution policy, https://support.google.com/contributionpolicy/answer/7400114.
