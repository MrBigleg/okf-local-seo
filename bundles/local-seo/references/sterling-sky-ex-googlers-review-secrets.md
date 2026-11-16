---
type: Reference
title: Sterling Sky — Ex-Googlers on review filtering, review parties, and manual-to-automated workflows
description: Former Google Trust & Safety employees (Brad Weatherall, Joel Headley) explain how review-spam detection algorithms cause collateral damage, how 'review parties' trigger proximity/IP filters, and the diminishing number of human-managed workflows at Google.
resource: https://www.youtube.com/watch?v=rym8pD9Gnhc
publisher: Sterling Sky (Joy Hawkins)
published: 2026-06-24
accessed: 2026-11-16
confidence: low-medium
scope: Insider perspective from two former Google employees (11 years each). Covers review algorithm seasonality, not Google's current policy.
tags: [reference, reviews, review-filtering, google-trust-safety]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
status: draft
stale_after: 2027-03-19
sources:
  - id: notebooklm-source-267c82a1
    resource: https://www.youtube.com/watch?v=rym8pD9Gnhc
    title: "Ex-Googlers Reveal 3 Google Business Profile Secrets"
---

An hour-long Sterling Sky interview (published 24 June 2026) in which Joy Hawkins questions two former Google employees, Brad Weatherall and Joel Headley, about review filtering, support and verification. [^notebooklm-source-267c82a1]

**Read everything here as recollection and opinion from former staff, not as Google policy or current practice.** Weatherall says he left Google about two years before the interview; Headley says he is about ten years removed. Both say they were at Google for a little over eleven years. Several answers are explicitly labelled by the speakers as speculation. [^notebooklm-source-267c82a1]

> This page was written on 2026-11-16 from the video's captions and YouTube metadata, not from a viewing of the video. Captions can mis-transcribe names and numbers, and anything shown only on screen is not captured here. A human should confirm any figure against the video before relying on it.

# Review filtering

* **Seasonality (Weatherall).** He describes review-spam enforcement as cyclical: the Trust and Safety team tends to experiment with detection in roughly March and April, sometimes over-tightens, catches legitimate reviews, and then relaxes after support contacts spike. He says changes are avoided in Q4 because of the holiday code freeze. [^notebooklm-source-267c82a1]
* **Not all removed reviews return (Weatherall).** After an adjustment, he suggests a business that lost ten reviews might get six to eight back, and calls a 100% recovery an unrealistic expectation. These are illustrative numbers, not measurements. [^notebooklm-source-267c82a1]
* **Scripts, not one algorithm (Headley).** He describes a collection of scripts written against known spam examples and accepted on sampled hit rates, giving 80% targeted and 20% not as an example of a result a team would accept. Weatherall says the conversations he was in were closer to 90/10, and that he pushed to lower it. [^notebooklm-source-267c82a1]
* **Legitimate behaviour can look like spam (Headley).** His examples are a business that suddenly starts review campaigns after none, and reviews arriving from accounts that have never reviewed before. [^notebooklm-source-267c82a1]
* **"Review parties" (Weatherall).** He says reviews left by many people at the same place and time are being removed, and that the detected pattern is the closeness in time and location, not on-site reviewing as such. He still calls a steady drip of on-site reviews a valuable approach, and warns against treating any single signal as absolute. [^notebooklm-source-267c82a1]
* **Two tactics relayed by the host.** Asking a reviewer to edit a filtered review slightly, and sending reviewers to the search result instead of a direct review link. Hawkins says she tested the first and it worked once for her own agency. Headley's explanation is that spammers do not come back to edit and that more on-page interaction looks human; Weatherall's is that an edit triggers reprocessing and that more engagement raises trust. Both are offering reasons, not confirming a mechanism. [^notebooklm-source-267c82a1]
* **Staff names in reviews.** Hawkins raises a recent Google guideline against employees asking to be named in reviews. Weatherall, saying he is speculating, guesses at a privacy motive and says he would advise restaurants against the practice but not service trades. [^notebooklm-source-267c82a1] This bundle's position is in [Reviews on GBP](/gbp/reviews.md): follow Google's contribution policy; a former employee's guess is not permission.

# How removed reviews are stored (Headley, Weatherall)

* Content deleted by its author is purged. Content removed by Google is hidden from public serving, stays attached to the author's account, and can reappear when it is reprocessed. The author continues to see it. [^notebooklm-source-267c82a1]
* Because the review belongs to the reviewer's account and not to the profile, a support agent looking at the listing may say the reviews cannot be found. Weatherall's advice is to bring evidence: notification emails or an exported backup listing the missing reviews. [^notebooklm-source-267c82a1]

# Support and verification (mostly Weatherall, as of about two years before the interview)

* Missing-review cases are, in his account, re-run through the automated check under a defined process; agents do not read and judge each review. [^notebooklm-source-267c82a1]
* He describes three support levels: levels one and two sit together in the same call centres, and level three is a small US group that logs product defects with engineering. He says asking for level two gets a more experienced agent but may not change the answer. Headley adds that a missing review or a suspension is a data issue, not a bug, so it is not what level three exists for. [^notebooklm-source-267c82a1]
* He says call-centre quality varied by location and that Spanish-language support scored higher than English-language support in his time. This is an unverifiable anecdote about a past state. [^notebooklm-source-267c82a1]
* Agents were once rewarded on satisfaction scores, which he says led them to approve too much, including spam reinstatements, until the incentive was changed to decision quality. [^notebooklm-source-267c82a1]
* **Manual verification path.** He says postcard verification was retired and video verification replaced it; that a human-run "on-demand video verification" call exists; and that a manual, document-upload verification form becomes reachable through the support flow only after a video verification attempt has failed, when a "contact us" link replaces "send feedback". He says this went to a human reviewer when he left and that manual workflows are being reduced. [^notebooklm-source-267c82a1]

# Limits

* No data, no documents and no current Google staff. Every statement is a personal account of a past state. [^notebooklm-source-267c82a1]
* The interview's review-removal context is spring 2026. For measured deletion rates see [Google review deletions: measured rates, timing and correlates](/references/reviewflowz-review-deletion-2026.md).
* The support-flow details (link wording, eligibility after a failed video attempt) should be tested live before being given to a business as steps.
