---
type: Reference
title: Google Local Services Ads — how leads are charged
description: The rules that decide whether a Local Services Ads lead is billable, including the 20-second missed-call rule, IVR timer semantics, charge statuses, and the 15-day no-recharge window.
resource: https://support.google.com/localservices/answer/7195435
publisher: Google (Local Services Help)
published: living document (no effective date or changelog entry published)
accessed: 2026-10-25
confidence: high
scope: Covers which contacts count as valid billable leads under Local Services Ads, how the 20-second missed-call rule interacts with IVR menus and voicemail, the four per-lead charge statuses, the 30-day reassessment window that can produce automatic credits, and the 15-day rule against re-charging the same customer. Records the documented regional and vertical carve-outs. Does not cover pricing levels, bidding economics, ranking or ad-position mechanics, and makes no claim about visibility effects. Lead credit availability is stated by Google as unavailable in EEA countries and, for lead credits and call recordings, unavailable for tax specialists and health-care verticals.
tags: [reference, lsa, local-services-ads, billing, gbp, policy]
generated: { by: iris/2026-W43, at: 2026-10-25T00:00:00Z }
status: draft
stale_after: 2026-11-25
sources:
  - id: google-lsa-how-leads-work
    resource: https://support.google.com/localservices/answer/7195435
    title: How leads work — Local Services Help
  - id: google-lsa-archive-2026-02-25
    resource: https://web.archive.org/web/20260225022736/https://support.google.com/localservices/answer/7195435
    title: Internet Archive snapshot of the same page, 25 February 2026 (prior state)
---

Google's Local Services Ads (LSA) help page documenting which customer contacts are billable. This is the primary source for the lead-charging rules; the page had substantially less detail on charging mechanics in the February 2026 archive snapshot (see [What changed](#what-changed-and-how-it-is-bracketed)).

# What the source establishes

Google states the model plainly: "With Local Services Ads, you pay for valid leads."

## Which contacts count as valid leads

The page lists the scenarios that can generate a valid lead, each of which is a billable contact when it meets the stated conditions:

* You answer a phone call, or you call the customer back and speak with the customer.
* You **missed** a phone call during your business hours and the customer stays on the line for **more than 20 seconds**.
* You receive a text message or email from the customer.
* You receive a voicemail from the customer.
* You receive a booking request from a customer (United States and Canada only).

## The 20-second missed-call rule

The rule is narrow in two directions, and both narrowings are documented:

* **It applies only to unanswered calls.** Google's own FAQ: "The 20-second ring rule applies only to unanswered (missed) calls. If you or someone at your business answers the phone (even after 20 seconds of ringing) you aren't charged based on the ring time." An answered call is instead evaluated as a call lead on the basis of the conversation.
* **It is measured on the line, not on the ring.** The 20 seconds is time the customer stays connected, not time the phone rings.

## IVR menus reset and then hold the timer

Where the call path requires a key press, Google documents three distinct behaviours:

* "If your call-receiving setup requires customers to press a key to route them to the relevant department, then the 20 second-timer will start once customers press the key. You won't be charged if customers don't press a key to get routed."
* "Once the caller presses their first key, the 20-second timer resets. You're charged if the call continues for more than 20 seconds after that first key press."
* "Additional key presses in multi-level menus don't reset the timer again."

So the timer starts at the **first** key press only. A caller who navigates a deep menu but hangs up inside 20 seconds of that first press is not billable, and later menu levels do not restart the clock.

## Voicemail and automated greetings

"If a call goes to voicemail or an automated greeting during your business hours, it's treated as a connected call and is charged if the caller stays on the line for more than 20 seconds, whether or not they leave a message."

## Charge statuses

Each lead carries a charge status in the **Charge Status** column on the Leads page in Google Ads, listed by Google as: **"Charged," "Not charged," "In review," or "Credited."**

## 30-day reassessment and automatic credits

"Google continuously assesses lead quality over a 30-day period. If a lead is determined to be of poor quality, duplicate, or invalid, a credit is automatically applied to your account balance."

The page also notes that leads are assessed at first contact, that leads judged invalid or low quality are not charged, and that charged leads are "reassessed by our models over time" and may be credited automatically.

## The 15-day rule against re-charging the same customer

"Once a lead is charged, any follow-up calls or messages with that customer are not charged again, provided there is interaction within 15 days and the contact comes from the same phone number or email address. If 15 days pass with no activity, a new call or message from that customer creates a new lead and will be charged if it meets valid lead criteria."

The rule is keyed on the **same phone number or email address** and on **activity within 15 days**, not on a fixed calendar window from first contact.

## Business hours come from the Google Business Profile

This is the direct link between GBP configuration and LSA billing:

> "Business hours" are the hours you set in your Google Business Profile, which you can update at any time. If you've set an ad schedule that differs from your business hours, unanswered calls are only charged when they happen during your active ad schedule and within your business hours.

A missed call only becomes billable if it falls inside **both** the ad schedule and the GBP business hours. Changing business hours in the Business Profile therefore changes which missed calls can be charged.

## Budget and spend mechanics

* You set an **average weekly budget** based on the average number of leads you want per week.
* "You can spend more than your average weekly budget in a given week on your leads, but you'll never spend more than your monthly max."
* "After you've reached your monthly max, your ad won't appear for the remainder of the month (unless you adjust your budget)."
* Billing is managed by Google Ads, and "Any suspension in your Google Ads account will also suspend your Local Services Ads."

## Documented carve-outs

* "Automatic lead credits are not available for accounts located in European Economic Area (EEA) countries."
* "Lead credits aren't available for health care verticals, tax specialists, or for advertisers in EMEA." The same note records that call recordings and lead credits are not available for tax specialists or health-care verticals located within the United States, and are not available for any verticals in Europe.
* Booking leads are only available in the United States and Canada.

# What changed, and how it is bracketed

The page is a living help document with **no effective date and no changelog entry**, so the change is bracketed rather than dated. The Internet Archive snapshot of **25 February 2026** renders the same page and contains **none** of the charging-mechanics vocabulary now present:

| Probe | 2026-02-25 snapshot | Live, 2026-10-25 |
|---|---|---|
| "20 second" | 0 occurrences | present |
| "In review" (charge status) | 0 occurrences | present |
| "Charge Status" | 0 occurrences | present |
| "30-day" assessment | 0 occurrences | present |
| "15 day" no-recharge rule | 0 occurrences | present |

The archived snapshot is a real render of the page (it contains the page heading and the opening "you pay for valid leads" text), so the absence is a content absence, not a failed retrieval.

**Bracket:** the charging mechanics were absent on 2026-02-25 and present on 2026-10-25. No intermediate snapshot was checked, so the change is bounded to that window and precisely dated by neither Google nor this page.

# What this source does not establish

* No ranking, ad-position or visibility claim is made in either direction.
* No pricing level, cost-per-lead figure or bidding behaviour is documented here.
* The 30-day reassessment is described as continuous and model-driven; the page states no dispute process beyond the per-lead Feedback Survey and no remedy beyond automatic credits.
* No effective date exists for the charging rules, so this page must not be read as evidence that any particular account was billed under these rules before 2026-10-25.

# Related

* [Google Business Profile](/gbp/google-business-profile.md) — business hours are configured here and drive the missed-call billing window.
* [GBP Profile Audit](/maps/gbp-profile-audit.md) — relevant when auditing whether stated hours match actual call-handling.
