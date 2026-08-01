---
type: Reference
title: Google Business Profile APIs — locations.patch
description: The Business Information API's PATCH endpoint for updating a location, and its update-mask requirement.
resource: https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch
publisher: Google (Business Profile APIs)
published: living document
accessed: 2026-08-01
confidence: high
scope: Confirms the endpoint updates only the fields named in a required updateMask parameter — a targeted patch, not a full-record overwrite. Does not establish a generic revert, undo, or reversion endpoint; none is documented on this page or elsewhere in the Business Information API reference.
tags: [reference, gbp, api]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
verified:  { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
status: stable
stale_after: 2026-11-01
sources:
  - id: google-business-profile-apis-locations-patch
    resource: https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch
    title: Google Business Profile APIs — locations.patch
---

Google's REST reference for `locations.patch` in the Business Information API. Used as the primary source for API-driven profile edits in [Human-in-the-Loop GBP Management](/agentic/hitl-gbp-management.md) and [Profile Shielding](/gbp/profile-shielding.md).

# What the source establishes

* `updateMask` is a required, comma-separated list of fully qualified field names — the PATCH only touches fields named in the mask.
* There is no generic "undo" or "reversion" endpoint. Reverting an unwanted change means issuing a new patch back to a known-good snapshot, not calling a built-in rollback.
