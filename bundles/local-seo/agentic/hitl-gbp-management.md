---
type: Playbook
title: Human-in-the-Loop GBP Management
description: An AI drafts GBP changes (replies, posts, corrections) but a human approves before anything is published.
tags: [local-seo, gbp, ai-ops, hitl]
timestamp: 2026-06-25T00:00:00Z
---

> **Draft — pending fact-check & citation URLs.**

Human-in-the-loop (HITL) GBP management is the execution pattern beneath agentic local ops: an AI *drafts* operational changes to a [Google Business Profile](/local-seo/gbp-signals.md) — review replies, posts, profile corrections, reversions — but a human *approves* before anything is written back to Google.

The one-liner: **AI proposes, you review, you approve, AI executes.**

# The control model

The agent is prohibited from direct external writes. Every customer-visible change passes an approval gate:

1. **Draft** — the agent generates a reply, post, correction, or reversion.
2. **Pending approval** — the draft is stored internally, never auto-published.
3. **Human authorises** — the operator reviews, edits, approves, or discards.
4. **Execute** — only approved changes are pushed via the relevant Google API.

# Why it matters

It captures the efficiency of automation without exposing a brand to unverified AI output. It also creates an audit trail — every published change has a human approver and a timestamp — which matters for reputation, compliance, and [review](/local-seo/reviews-reputation.md) integrity.

# Good candidates for drafting

* Review replies (tone-matched, policy-safe).
* Google Posts and offers.
* Profile field corrections and category fixes.
* Reversions when an unwanted edit appears.

# Citations

[1] Human-in-the-loop AI patterns for local operations (confirm sources).
