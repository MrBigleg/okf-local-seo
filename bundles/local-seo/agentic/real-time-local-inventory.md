---
type: Ranking Dimension
title: Real-Time Local Inventory
description: Store-level product availability, price and pickup data that makes local retail results actionable.
tags: [local-seo, retail, inventory, agentic, ai-search]
timestamp: 2026-06-25T00:00:00Z
---

Real-time local inventory is store-level data showing whether a product is available at a particular location, at what price and under which pickup terms. It helps a shopper or agent distinguish a product that exists in a catalogue from one that can actually be obtained nearby.

“Real-time” is an operational objective, not a guarantee made by every publishing channel. Google notes that Business Profile locations can take up to 24 hours to synchronise into Merchant Center.

# Consumer evidence

Lastmile Retail reported results from a consumer survey conducted with Greg Sterling among **1,000 US adults** about local purchases totalling **$300 or more**:

* **95%** said confirming that an item priced at $300 or more is available locally before visiting is somewhat to extremely important.
* **56%** selected real-time product availability before visiting as a factor that would influence them to choose a local option instead of remote shipping.
* **48%** selected the option to reserve online for in-store purchase or pickup.
* **40%** reported insufficient product information on company websites when searching online to buy locally.
* **37%** reported being unable to confirm whether a product was available at a particular store; the same proportion reported inaccurate inventory information.

These findings are specific to the reported US survey and high-dollar purchase scenario. They should not be generalised to all markets or purchase values.

# Minimum data

Google's local inventory specification supports:

* product ID;
* store code matched to the corresponding Business Profile;
* availability: in stock, limited availability, on display to order or out of stock;
* store-specific price and sale price;
* optional quantity;
* pickup method, including buy, reserve or ship to store; and
* pickup service level, such as same day or next day.

The submitted availability, price and pickup promise should match the physical store and the landing or checkout experience.

# Implementation checklist

* Maintain one stable product identifier across product and local-inventory data.
* Publish availability for each store, not only at chain level.
* Update stock promptly after sales, returns and stock transfers.
* Show nearby alternatives when the preferred branch is unavailable.
* Keep first-party pages, Merchant Center and the [Business Profile](/local-seo/gbp-signals.md) consistent.
* Provide a human confirmation path for expensive, scarce or fast-moving items.

# Agentic angle

Availability, price and fulfilment are decision inputs for [Agentic Commerce Readiness](/agentic/agentic-commerce-readiness.md). An agent should not reserve or purchase when those inputs are stale or contradictory.

# Citations

[1] [Google Merchant Center — Local inventory ads and free local listings overview](https://support.google.com/merchants/answer/14615117?hl=en)

[2] [Google Merchant Center — Local inventory data specification](https://support.google.com/merchants/answer/14819809?hl=en)

[3] [Lastmile Retail / Miriam Ellis — Data-based Tactics for Increasing High-Dollar Local Purchases](https://www.linkedin.com/pulse/data-based-tactics-increasing-high-dollar-local-purchases-lastmile-ozqte)
