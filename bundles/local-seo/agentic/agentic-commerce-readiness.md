---
type: Playbook
title: Agentic Commerce Readiness
description: A conservative checklist for making a local business discoverable and safely transactable by supported AI agents.
tags: [local-seo, commerce, gbp, agentic, checklist]
generated: { by: human:craigburton, at: 2026-06-25T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-06-25T00:00:00Z }
status: stable
stale_after: 2026-07-25
sources:
  - id: google-get-started-with-business-agent
    resource: /references/google-business-agent.md
    title: Google — Get started with Business Agent
  - id: google-business-profile-apis-update-food
    resource: /references/google-food-menus-api.md
    title: Google Business Profile APIs — Update Food Menus
  - id: universal-commerce-protocol-specification-overview
    resource: https://ucp.dev/specification/overview/
    title: Universal Commerce Protocol — Specification overview
    last_modified: 2026-04-08
  - id: google-hotel-apis-hotel-prices-developer
    resource: https://developers.google.com/hotels/hotel-prices/dev-guide
    title: Google Hotel APIs — Hotel Prices Developer's Guide
    last_modified: 2025-04-14
  - id: universal-commerce-protocol-protocol-and-industry
    resource: /references/agentic-commerce-protocols.md
    title: Universal Commerce Protocol — Protocol and industry roadmap
---

This is the actionable counterpart to [Agentic Commerce](/agentic/agentic-commerce.md). Readiness means publishing reliable business, offer and fulfilment data, then exposing transaction capabilities only through channels the business can operate safely.

# 1. Separate local identity from retail identity

* Claim and maintain each [Google Business Profile](/local-seo/gbp-signals.md) for location facts such as address, hours, categories and services.
* Retailers should separately verify Merchant Center and, where eligible, claim their Search brand profile.
* Do not treat a brand profile as another name for a Business Profile; they are different surfaces.

Google's Business Agent is a Search experience for eligible US e-commerce retailers. Customisation requires a US-based store, a verified Merchant Center account, at least **50 approved free listings**, and a claimed brand profile. It uses Merchant Center data, the retailer's website and additional supplied business data. See the reference page [Google — Get started with Business Agent](/references/google-business-agent.md).

# 2. Publish structured offers

* Keep product identifiers, titles, descriptions, prices, availability and fulfilment terms consistent across the site and connected feeds.
* Use appropriate [schema](/local-seo/local-schema.md) on first-party pages, but do not assume schema alone enrols a business in an agent checkout programme.
* Restaurants should publish structured menu data. The Business Profile API supports menu-item names, prices, descriptions, dietary information and associated photos.
* Do not rely on photos of a printed menu as a substitute for structured menu data. No primary source was found for automatic menu extraction from Business Profile photos.

# 3. Expose only supported protocol capabilities

If adopting UCP, publish the business profile at `/.well-known/ucp`. The profile declares supported protocol versions, services, capabilities, endpoints, payment handlers and verification keys.

A discovery document is useful only when the corresponding protocol is actually implemented. Publishing an invented or incomplete endpoint creates false capability signals.

# 4. Connect operations to promises

## Retail

Publish branch-level [local inventory](/agentic/real-time-local-inventory.md), price and pickup terms. Availability shown to an agent must match the store.

## Restaurants

Ensure the ordering channel, point-of-sale system and kitchen workflow share the same menu and order state. Removing an unavailable item should update every active ordering surface. This is an operational requirement; current UCP food specifications were still described as forthcoming on 25 June 2026.

## Hotels

Connect the property or central reservation system to the chosen distribution channel through a supported integration. Google's Hotel Prices documentation supports availability, rates and inventory messages, along with price-accuracy and coverage reporting. This verifies channel synchronisation capabilities, but not a universal requirement to use any named property-management vendor.

# 5. Keep a safe fallback

When price, availability, identity or authority cannot be verified, the system should stop before purchase and hand the user to a human or first-party checkout. Readiness is not maximum automation; it is reliable execution within explicit limits.
