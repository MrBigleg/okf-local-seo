---
type: Playbook
title: GBP Business Description
description: The 750-character "From the business" field — what Google allows, a working formula, and the anti-patterns that get descriptions rejected.
tags: [local-seo, gbp, content]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
verified:  { by: anthropic/claude-fable-5-2, at: 2026-11-16T00:00:00Z }
status: stable
stale_after: 2027-05-16
sources:
  - id: google-edit-your-business-profile
    resource: https://support.google.com/business/answer/3039617
    title: Google — Edit your Business Profile
  - id: google-guidelines-for-representing-your-business
    resource: /references/google-gbp-categories-description.md
    title: Google — Guidelines for representing your business on Google
---

The business description is the free-text field on a [Google Business Profile](/gbp/google-business-profile.md), shown in the **"From the business"** section of the profile. Google's editing help confirms a limit of **750 characters** (accessed 2026-11-16). In some regions and languages Google offers AI-assisted drafting inside the profile editor.

Treat the description primarily as a conversion asset: Google's guidance frames it as customer information ("services and products offered, as well as the mission and history of your business"), and no primary source documents a specific ranking weight for it. Completeness in general feeds relevance — see [GBP signals](/local-seo/gbp-signals.md).

# What Google's rules allow

From Google's guidelines for representing your business and the profile-editing help:

* Describe what you offer, what makes the business unique, your history, and anything else useful to customers.
* **No links of any type** — URLs and HTML are rejected.
* Don't focus on promotions, prices or sales ("Everything on sale, −50%" is Google's own example of what to avoid).
* No low-quality or irrelevant content: misspellings, gimmicky character use, gibberish.
* Be "upfront and honest about the information provided".

# A working formula

Spend the 750 characters in roughly this order, most important first:

1. **What you are and where** — one plain sentence: offer + primary service area. Front-load it.
2. **Core services** — the two-to-four things people actually search for, phrased the way customers say them (which supports relevance matching without stuffing).
3. **Differentiators** — years trading, credentials, guarantees, specialisms. Verifiable claims only.
4. **A soft close** — what to do next, without a URL: "Call for a same-day quote."

Reuse the same factual core on the website's homepage or location page and in the `LocalBusiness` schema `description` — consistency across surfaces is the point of [NAP & citations](/local-seo/nap-citations.md) and [local schema](/local-seo/local-schema.md).

# Anti-patterns

* **Keyword stuffing** — a list of city names and service permutations reads as low-quality content and wastes the field's persuasive job.
* **Promo copy** — offer-led text breaches the guideline outright; put offers in [Google Posts](/gbp/google-posts.md), which exist for that.
* **URLs and HTML** — Google's editing help says not to include them. Its guidelines also name misspellings, "gimmicky character use" and gibberish as low-quality content to keep out of the description.
* **Restating the category list** — the categories, services and attributes fields already carry that data structurally; duplicating them spends characters without adding information.
* **Unverifiable superlatives** — "the best in town" is neither honest per the guidelines nor useful to a reader.
