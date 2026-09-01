---
type: Playbook
title: Human-in-the-Loop GBP Management
description: A control pattern in which AI drafts Google Business Profile changes and an authorised human approves execution.
tags: [local-seo, gbp, ai-ops, hitl]
generated: { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
verified:  { by: anthropic/claude-sonnet-5, at: 2026-09-01T00:00:00Z }
status: stable
stale_after: 2026-10-01
sources:
  - id: google-business-profile-apis-create-posts
    resource: https://developers.google.com/my-business/content/posts-data
    title: Google Business Profile APIs — Create Posts on Google
    last_modified: 2026-02-24
  - id: google-business-profile-apis-work-with
    resource: https://developers.google.com/my-business/content/review-data
    title: Google Business Profile APIs — Work with review data
    last_modified: 2025-08-28
  - id: google-business-profile-apis-update-a
    resource: /references/google-locations-patch.md
    title: Google Business Profile APIs — Update a location
  - id: google-business-profile-apis-update-food
    resource: /references/google-food-menus-api.md
    title: Google Business Profile APIs — Update Food Menus
  - id: google-business-profile-apis-upload-media
    resource: https://developers.google.com/my-business/content/upload-photos
    title: Google Business Profile APIs — Upload media
    last_modified: 2025-08-28
  - id: google-business-profile-apis-attributes
    resource: https://developers.google.com/my-business/content/attributes
    title: Google Business Profile APIs — Add attributes
    last_modified: 2025-08-28
  - id: google-business-profile-apis-services
    resource: https://developers.google.com/my-business/content/services
    title: Google Business Profile APIs — Add services
    last_modified: 2025-08-28
  - id: google-business-profile-apis-prerequisites
    resource: https://developers.google.com/my-business/content/prereqs
    title: Google Business Profile APIs — Prerequisites
    last_modified: 2025-08-28
---

Human-in-the-loop (HITL) Business Profile management is a governance pattern: software prepares a proposed change, but an authorised person reviews it before any customer-visible write.

Google does not require this approval pattern. It is an operator control for reducing accidental, misleading or policy-breaking changes.

# Control flow

1. **Draft** — generate a proposed reply, post or field update.
2. **Validate** — check required fields, policy constraints and current profile state.
3. **Approve** — record the human reviewer, decision and any edits.
4. **Execute** — use the relevant Business Profile API only after approval.
5. **Audit** — store the request, response, timestamp and resulting resource identifier.

# Supported candidates

Google's Business Profile APIs document support for:

* creating, editing and deleting event, call-to-action and offer posts;
* listing reviews, publishing or replacing an owner reply, and deleting an owner reply;
* patching supported location fields with an update mask;
* uploading media;
* updating eligible food menus; and
* managing services and attributes through their relevant resources.

Product posts cannot currently be created through the documented Posts API.

# Guardrails

* Compare the proposed update with the latest live resource immediately before execution.
* Reject a change if the live profile changed after the draft was approved.
* Use the narrowest possible update mask.
* Never fabricate customer experiences, prices, availability or review details.
* Treat “reversion” as a new, reviewed API update based on a known-good snapshot; there is no generic undo endpoint.
* Keep credentials, approval authority and execution authority separately scoped where practical.

# Suitable drafting tasks

* review replies;
* event, offer and call-to-action posts;
* category, hours, service or attribute corrections supported by the API; and
* structured menu updates for eligible restaurant locations.
