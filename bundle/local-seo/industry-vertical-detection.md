---
type: Detection Method
title: Industry Vertical Detection
description: Detect the industry vertical from page and GBP signals to route to industry-specific local SEO checks.
tags: [local-seo, detection]
timestamp: 2026-06-24T00:00:00Z
---

Detect the vertical from page signals and GBP category patterns, then route to industry-specific checks (see [local schema markup](/local-seo/local-schema.md)). If no vertical is detected, use the generic `LocalBusiness` path.

# Detection signals

| Vertical | Detection signals |
|----------|-------------------|
| **Restaurant** | /menu, menu items, reservations, cuisine types, food ordering, "dine-in", "takeout" |
| **Healthcare** | insurance accepted, patients, appointments, NPI, medical terms, "Dr.", HIPAA notice |
| **Legal** | attorney, lawyer, practice areas, bar admission, case results, "free consultation" |
| **Home Services** | service area, emergency service, "free estimate", licensed/insured/bonded, "24/7" |
| **Real Estate** | listings, MLS, properties for sale/rent, agent bio, brokerage, "open house" |
| **Automotive** | inventory, VIN, test drive, dealership, service department, "new/used/certified" |

# Why it matters

The vertical changes the correct schema subtype, the citation directories worth pursuing, and the review-response rules (e.g. HIPAA constraints for healthcare). When the vertical is unclear, present the top two detected verticals with supporting signals and confirm before applying industry-specific recommendations.
