---
type: Reference
title: Google Business Profile APIs — Manage Google Updates
description: Developer documentation for detecting and accepting or rejecting Google-initiated profile changes.
resource: https://developers.google.com/my-business/content/accept-or-reject-updates
publisher: Google (Business Profile APIs)
published: living document
accessed: 2026-07-06
confidence: high
scope: The hasGoogleUpdated flag, getGoogleUpdated endpoint, diffMask/pendingMask semantics, and patch-based accept/reject mechanics.
tags: [reference, gbp, api, monitoring]
timestamp: 2026-07-06T00:00:00Z
---

Google's developer documentation for handling Google-initiated updates to managed locations. Primary source for the [profile shielding](/gbp/profile-shielding.md) pattern.

# What the source establishes

* `metadata.hasGoogleUpdated` is `true` when a location has pending Google updates requiring review, and clears after they are processed.
* `locations.getGoogleUpdated` returns the Google-updated view with a **`diffMask`** (fields where Google's serving data differs from your submitted values — action needed) and a `pendingMask` (fields you submitted that are still in review — no action needed).
* Accepting and rejecting both use `locations.patch` with an `updateMask`: accept by patching in Google's value, reject by re-asserting your original value.

# Citations

[1] [Manage Google Updates](https://developers.google.com/my-business/content/accept-or-reject-updates)
