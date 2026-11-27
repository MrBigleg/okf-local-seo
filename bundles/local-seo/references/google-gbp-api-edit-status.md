---
type: Reference
title: Google Business Profile APIs — Check edit status
description: "Read the merchant and consumer views, edit stage and policy rejection reasons per field or attribute."
resource: https://developers.google.com/my-business/content/edit-status
publisher: Google for Developers
published: 2026-11-02
accessed: 2026-11-27
confidence: high
scope: "My Business Business Information API v1alpha for authorised partner integrations. Google lists availability to all API partners without a market carve-out."
tags: [reference, gbp, api, edit-status]
generated: { by: openai/gpt-6, at: 2026-11-27T02:23:00Z }
verified: { by: openai/gpt-6, at: 2026-11-27T02:23:00Z }
status: stable
stale_after: 2026-12-27
sources:
  - id: edit-status
    resource: https://developers.google.com/my-business/content/edit-status
    title: Check edit status for locations and attributes
  - id: gbp-api-latest-updates
    resource: https://developers.google.com/my-business/content/latest-updates
    title: Business Profile APIs latest updates
---

Google [announced the edit status endpoints on 2 November 2026](https://developers.google.com/my-business/content/latest-updates#2026-11-02). The existing [Google Updates workflow](/references/google-manage-google-updates.md) exposes differences and a pending mask. The new read methods expose the lifecycle stage and policy rejection reason for individual fields and attributes.

* Use `locations.getExtended` for location fields and `locations.attributes.getExtended` for attributes. Each returns the merchant-provided values, consumer-facing values and edit metadata.
* Metadata identifies the latest edit stage, API or UI origin, update timestamp and policy reason when rejected. The reason can indicate account restrictions, suspended or unverified locations, an editing restriction or a content-policy issue.
* Google recommends waiting on pending edits and investigating the reason for a rejection before sending a corrected edit. A value updated by Google calls for checking the live value and deciding whether to accept it. The endpoints read the status of an edit. Appeals follow the [market-specific Help workflow](/references/google-gbp-appeals.md).
