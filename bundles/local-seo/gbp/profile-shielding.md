---
type: Playbook
title: Profile Shielding
description: A generic detect-diff-decide-revert pattern for catching and reversing unauthorised Business Profile edits ("Google updates").
tags: [local-seo, gbp, monitoring, api]
generated: { by: openai/gpt-6, at: 2026-11-27T02:23:00Z }
status: stable
stale_after: 2027-05-16
sources:
  - id: google-manage-google-updates
    resource: /references/google-manage-google-updates.md
    title: Google Business Profile APIs — Manage Google Updates
  - id: google-understand-what-happens-to-your
    resource: https://support.google.com/business/answer/3038311
    title: Google — Understand what happens to your Business Profile edits
  - id: google-business-profile-apis-locations-patch
    resource: /references/google-locations-patch.md
    title: Google Business Profile APIs — locations.patch
  - id: google-gbp-api-edit-status
    resource: /references/google-gbp-api-edit-status.md
    title: Google Business Profile APIs — Check edit status
  - id: google-gbp-api-notifications
    resource: /references/google-gbp-api-notifications.md
    title: Google Business Profile APIs — Notification topic ownership
---

A [Google Business Profile](/gbp/google-business-profile.md) is not solely owner-authored. Google updates profiles from other sources — user suggestions and reports among them — to keep customer-facing information current. When that happens the owner gets a notification and an alert in the profile's Edit profile section; the change may already be live. "Profile shielding" is the generic operational pattern for catching these changes quickly and re-asserting the canonical data. It is written here product-neutrally: any scheduler, any alerting channel, any data store.

The risk being managed: a category, hours or address change you didn't make silently degrades [relevance](/local-seo/gbp-signals.md), misdirects customers, or (address changes) undermines [NAP consistency](/local-seo/nap-citations.md).

# The pattern: detect → diff → decide → re-assert

Google's Business Profile API documents the mechanics end-to-end ("Manage Google Updates", accessed 2026-07-06):

1. **Detect** — poll the locations you manage and check the **`metadata.hasGoogleUpdated`** flag. `true` means Google's serving version differs from your submitted version and needs review. This flag is the programmatic equivalent of the pending-updates alert in the profile editor.
2. **Diff** — call **`locations.getGoogleUpdated`** for the flagged location. The response carries a **`diffMask`** listing exactly which fields Google's serving data changed (action needed), and a `pendingMask` for fields you submitted that are still in review (no action needed — don't fight your own pending edits).
3. **Decide** — route the diff to a human with the canonical value alongside Google's value. Some Google updates are correct (a real hours change reported by the public); auto-reverting everything re-breaks those. This is a [human-in-the-loop](/agentic/hitl-gbp-management.md) decision point.
4. **Re-assert or accept** — both are the same API call: **`locations.patch`** with an `updateMask` scoped to the disputed fields. To accept, patch in Google's new value; to reject, patch your original value back, which re-submits it through Google's normal review. After a successful patch, `hasGoogleUpdated` clears.

# Training and audit checks for API-managed networks

Google's [2 November 2026 edit status release](/references/google-gbp-api-edit-status.md) gives authorised API partners a way to distinguish a pending edit, a policy rejection and a Google-sourced change across locations.

* **Audit the edit:** When a location's submitted value differs from the live value, record the location ID, field or attribute, both values, latest stage, source, timestamp and any rejection reason. Use `locations.getExtended` for location fields and `locations.attributes.getExtended` for attributes where the integration supports `v1alpha`.
* **Train the support team:** Leave pending edits queued. For rejections, check the named reason and the underlying policy or account restriction before resubmitting. If a client disputes the decision, use the [applicable appeal route](/references/google-gbp-appeals.md). Route a Google-updated value to the person responsible for the canonical location record.
* **Advise clients:** Report whether a change is live, pending or rejected. For a rejected change, explain the policy or evidence issue and who needs to act. Teams without the alpha integration can compare the profile editor status with the public listing.

Google's [November 2026 Notifications API guidance](/references/google-gbp-api-notifications.md) also affects central alerting:

* **Audit notification setup:** Inventory every GBP account using the Notifications API, the calling OAuth client's Cloud project, its Pub/Sub topic project and the subscriber project. Flag cross-project topic bindings before onboarding or reconfiguration.
* **Update the integration runbook:** Register a topic in the OAuth client's project and verify delivery for each configured account. If consumers are hosted in another project, use Google's cross-project subscription pattern. Route `PUBSUB_TOPIC_NOT_IN_CALLER_PROJECT` to the integration owner for configuration review.
* **Advise clients:** On agencies' and franchises' shared notification systems, confirm who owns the OAuth client and topic before changing account configuration. Include review and location alert delivery in acceptance testing.

# Operational notes

* **Keep a canonical record.** Reversion requires a trusted copy of every field's correct value, versioned and dated, outside the profile itself. The [audit checklist](/maps/gbp-profile-audit.md) fields are the natural schema.
* **Patch narrowly.** Always use the tightest `updateMask` that covers the disputed fields — a broad patch can overwrite unrelated pending changes.
* **Expect review latency.** Owner edits are themselves reviewed — Google says edits "usually take up to 10 minutes to review, but sometimes it can take up to 30 days" — so a re-asserted value is not instantly live, and repeated rapid flip-flopping of high-trust fields (name, address, category) invites scrutiny.
* **Alert on the fields that hurt most.** Primary category, name, address, phone, website and hours deserve immediate alerts; attribute-level drift can batch into a daily digest.
* **Non-API fallback.** The same loop runs manually at lower frequency: check the Edit profile section for the pending-updates alert on a schedule, compare against the canonical record, and accept or edit back through the editor.
