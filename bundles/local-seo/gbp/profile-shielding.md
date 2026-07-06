---
type: Playbook
title: Profile Shielding
description: A generic detect-diff-decide-revert pattern for catching and reversing unauthorised Business Profile edits ("Google updates").
tags: [local-seo, gbp, monitoring, api]
timestamp: 2026-07-06T00:00:00Z
---

A [Google Business Profile](/gbp/google-business-profile.md) is not solely owner-authored. Google updates profiles from other sources — user suggestions and reports among them — to keep customer-facing information current. When that happens the owner gets a notification and an alert in the profile's Edit profile section; the change may already be live. "Profile shielding" is the generic operational pattern for catching these changes quickly and re-asserting the canonical data. It is written here product-neutrally: any scheduler, any alerting channel, any data store.

The risk being managed: a category, hours or address change you didn't make silently degrades [relevance](/local-seo/gbp-signals.md), misdirects customers, or (address changes) undermines [NAP consistency](/local-seo/nap-citations.md).

# The pattern: detect → diff → decide → re-assert

Google's Business Profile API documents the mechanics end-to-end ("Manage Google Updates", accessed 2026-07-06):

1. **Detect** — poll the locations you manage and check the **`metadata.hasGoogleUpdated`** flag. `true` means Google's serving version differs from your submitted version and needs review. This flag is the programmatic equivalent of the pending-updates alert in the profile editor.
2. **Diff** — call **`locations.getGoogleUpdated`** for the flagged location. The response carries a **`diffMask`** listing exactly which fields Google's serving data changed (action needed), and a `pendingMask` for fields you submitted that are still in review (no action needed — don't fight your own pending edits).
3. **Decide** — route the diff to a human with the canonical value alongside Google's value. Some Google updates are correct (a real hours change reported by the public); auto-reverting everything re-breaks those. This is a [human-in-the-loop](/agentic/hitl-gbp-management.md) decision point.
4. **Re-assert or accept** — both are the same API call: **`locations.patch`** with an `updateMask` scoped to the disputed fields. To accept, patch in Google's new value; to reject, patch your original value back, which re-submits it through Google's normal review. After a successful patch, `hasGoogleUpdated` clears.

# Operational notes

* **Keep a canonical record.** Reversion requires a trusted copy of every field's correct value, versioned and dated, outside the profile itself. The [audit checklist](/maps/gbp-profile-audit.md) fields are the natural schema.
* **Patch narrowly.** Always use the tightest `updateMask` that covers the disputed fields — a broad patch can overwrite unrelated pending changes.
* **Expect review latency.** Owner edits are themselves reviewed — usually about ten minutes, but up to 30 days for sensitive fields — so a re-asserted value is not instantly live, and repeated rapid flip-flopping of high-trust fields (name, address, category) invites scrutiny.
* **Alert on the fields that hurt most.** Primary category, name, address, phone, website and hours deserve immediate alerts; attribute-level drift can batch into a daily digest.
* **Non-API fallback.** The same loop runs manually at lower frequency: check the Edit profile section for the pending-updates alert on a schedule, compare against the canonical record, and accept or edit back through the editor.

# Citations

[1] [Google Business Profile APIs — Manage Google Updates](/references/google-manage-google-updates.md)

[2] [Google — Understand what happens to your Business Profile edits](https://support.google.com/business/answer/3038311)

[3] [Google Business Profile APIs — locations.patch](https://developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch)
