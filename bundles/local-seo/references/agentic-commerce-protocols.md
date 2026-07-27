---
type: Reference
title: Agentic commerce protocols (UCP, AP2, ACP, x402)
description: Primary specifications and announcements for the open protocols behind agent-led commerce.
resource: https://ucp.dev/
publisher: Multiple (Google, OpenAI, Stripe, Coinbase) — see per-protocol provenance below
published: 2025-09 to 2026-01 (per protocol)
accessed: 2026-06-25
confidence: high for existence; low for universal adoption
scope: Existence, backers and stated scope of each protocol. Does NOT establish universal merchant, wallet or payment-network adoption.
tags: [reference, commerce, agentic, protocols]
generated: { by: human:craigburton, at: 2026-06-25T00:00:00Z }
verified:  { by: human:craigburton, at: 2026-06-25T00:00:00Z }
status: stable
stale_after: 2026-09-25
sources:
  - id: universal-commerce-protocol-specification-and-ecosystem
    resource: https://ucp.dev/
    title: Universal Commerce Protocol — Specification and ecosystem
  - id: agent-payments-protocol-ap2-specification
    resource: https://ap2-protocol.org/
    title: Agent Payments Protocol (AP2) — Specification
  - id: google-cloud-announcing-the-agent-payments
    resource: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
    title: Google Cloud — Announcing the Agent Payments Protocol (AP2)
  - id: agentic-commerce-protocol-open-specification
    resource: https://www.agenticcommerce.dev/
    title: Agentic Commerce Protocol — Open specification
  - id: coinbase-developer-platform-x402-overview
    resource: https://docs.cdp.coinbase.com/x402/welcome
    title: Coinbase Developer Platform — x402 overview
---

Primary sources for the open protocols referenced by [Agentic Commerce](/agentic/agentic-commerce.md) and [Agentic Commerce Readiness](/agentic/agentic-commerce-readiness.md). These are distinct, independently governed specifications — not one universal, fully adopted stack.

# Per-protocol provenance

| Protocol | Publisher / backers | First public | Canonical source |
|---|---|---|---|
| Universal Commerce Protocol (UCP) | Google with retail and platform partners | January 2026 | https://ucp.dev/ |
| Agent Payments Protocol (AP2) | Google + 60+ participating organisations | September 2025 | https://ap2-protocol.org/ |
| Agentic Commerce Protocol (ACP) | OpenAI and Stripe | September 2025 | https://www.agenticcommerce.dev/ |
| x402 | Coinbase (open protocol) | per Coinbase docs | https://docs.cdp.coinbase.com/x402/welcome |

# What the sources establish

* Each protocol has a public specification and named backers; early production integrations exist.
* UCP defines discovery via `/.well-known/ucp`; cryptographically signed mandates are a mechanism **within AP2**, not a separate protocol; AP2 documents an A2A x402 extension for stablecoin payments.

# What they do not establish

Universal adoption is not demonstrated. A business should adopt a protocol only when a target channel or integration partner supports it, and should preserve ordinary web and API fallbacks.
