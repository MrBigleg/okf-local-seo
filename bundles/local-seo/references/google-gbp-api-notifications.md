---
type: Reference
title: Google Business Profile APIs — Notification topic ownership
description: "Google requires a Pub/Sub topic in the OAuth client's Cloud project for GBP notification settings."
resource: https://developers.google.com/my-business/content/notification-setup
publisher: Google for Developers
published: living document
accessed: 2026-11-27
confidence: high
scope: "My Business Notifications API v1, all markets where the integration is used. Applies to configuring notification settings."
tags: [reference, gbp, api, notifications]
generated: { by: openai/gpt-6, at: 2026-11-27T02:23:00Z }
verified: { by: openai/gpt-6, at: 2026-11-27T02:23:00Z }
status: stable
stale_after: 2026-12-27
sources:
  - id: notification-setup
    resource: https://developers.google.com/my-business/content/notification-setup
    title: Manage real-time notifications
  - id: notification-change-log
    resource: https://developers.google.com/my-business/content/notifications/change-log
    title: Notifications API change log
  - id: cross-project-notifications
    resource: https://developers.google.com/my-business/content/cross-project-notifications
    title: Receive notifications in another Cloud project
---

Google's [13 November 2026 changelog](https://developers.google.com/my-business/content/notifications/change-log) added `PUBSUB_TOPIC_NOT_IN_CALLER_PROJECT` for updates where the submitted Pub/Sub topic is outside the Google Cloud project that owns the calling OAuth client. The [setup guide](https://developers.google.com/my-business/content/notification-setup) updated on 25 November instructs integrators to create the topic in the OAuth client's project and grant the Business Profile notification service account permission to publish.

A consumer can still run elsewhere using Google's documented [cross-project subscription setup](https://developers.google.com/my-business/content/cross-project-notifications). Keep the topic in the OAuth project and grant the other project's subscriber the necessary access. Google gives no shutdown date for existing bindings in these notices.
