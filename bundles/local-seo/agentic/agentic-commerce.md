---
type: Concept
title: Agentic Commerce
description: Commerce in which an AI agent can help discover, select and transact with a business under explicit user authority.
tags: [local-seo, ai-search, commerce, agentic]
generated: { by: human:craigburton, at: 2026-06-25T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-06-25T00:00:00Z }
status: stable
stale_after: 2026-07-25
sources:
  - id: google-new-tech-and-tools-for
    resource: https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/
    title: Google — New tech and tools for retailers to succeed in an agentic shopping era
  - id: universal-commerce-protocol-specification-and-ecosystem
    resource: /references/agentic-commerce-protocols.md
    title: Universal Commerce Protocol — Specification and ecosystem
  - id: google-cloud-powering-ai-commerce-with
    resource: /references/agentic-commerce-protocols.md
    title: Google Cloud — Powering AI commerce with the Agent Payments Protocol
  - id: openai-instant-checkout-and-the-agentic
    resource: https://openai.com/index/buy-it-in-chatgpt/
    title: OpenAI — Instant Checkout and the Agentic Commerce Protocol
  - id: agentic-commerce-protocol-open-specification
    resource: /references/agentic-commerce-protocols.md
    title: Agentic Commerce Protocol — Open specification
  - id: coinbase-developer-platform-x402-overview
    resource: /references/agentic-commerce-protocols.md
    title: Coinbase Developer Platform — x402 overview
---

Agentic commerce describes commerce in which an AI agent can move beyond recommendation into actions such as building a cart, initiating checkout or completing an authorised purchase. For local businesses, the practical shift is from being merely discoverable to exposing reliable data and transaction capabilities that an agent can use.

# The protocol landscape

As of 25 June 2026, several distinct open protocols exist. They are not one universal, fully adopted stack.

| Protocol | Scope | Primary backing and status |
|---|---|---|
| Universal Commerce Protocol (UCP) | Discovery, catalogue, cart, checkout, identity linking and order management | Launched in January 2026; co-developed by Google and several retailers and platforms, with public specifications and reference implementations. |
| Agent Payments Protocol (AP2) | Verifiable authority, payment instructions and accountability for agent-led payments | Announced by Google in September 2025 with more than 60 participating organisations; public specification available. |
| Agentic Commerce Protocol (ACP) | Programmatic checkout between buyers, agents and businesses | Open-sourced in September 2025 and developed by OpenAI and Stripe; first implemented for an in-chat checkout experience. |
| x402 | HTTP-native, programmatic stablecoin payments | Developed by Coinbase as an open protocol. AP2 also documents an A2A x402 extension for agent-based crypto payments. |

# Signed mandates

Cryptographically signed mandates are a mechanism within AP2, not a separate commerce protocol. AP2 uses tamper-evident digital credentials to record checkout and payment authority for both human-present and delegated transactions.

# Adoption should not be overstated

Public specifications, launch partners and early production integrations demonstrate that these protocols exist. They do not establish universal merchant, wallet or payment-network adoption. A business should select a protocol only when a target channel or integration partner supports it, then preserve ordinary web and API fallbacks.

# Local-business implication

The durable requirement is structured, current and actionable data: identity, offers, price, availability, fulfilment and a safe way to authorise an action. See [Agentic Commerce Readiness](/agentic/agentic-commerce-readiness.md) and [Real-Time Local Inventory](/agentic/real-time-local-inventory.md).

Per-protocol provenance (publisher, first-public date, canonical spec) lives in the reference page [Agentic commerce protocols](/references/agentic-commerce-protocols.md).
