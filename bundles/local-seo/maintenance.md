---
type: Policy
title: Maintenance Policy
description: Ownership, review cadence and freshness tiers for keeping fast-moving claims in this bundle accurate.
owner: CTB Marketing (bundle maintainer)
review_cadence: weekly queue (volatile claims monthly — see tiers)
tags: [governance, maintenance, policy]
generated: { by: human:craigburton, at: 2026-06-25T00:00:00Z }
verified:  { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
status: stable
stale_after: 2027-02-01
---

This bundle mixes durable principles with fast-moving product facts. This policy says who keeps it current, how often, and how to tell which claims need the closest watch.

# Ownership

* **Owner:** CTB Marketing (bundle maintainer).
* The owner is accountable for the scheduled reviews below and for re-running `tool/okf_verify.py` before any export or release.
* Each concept records `generated: { by, at }` for its last content change, and `verified: { by, at }` once a dated pass has confirmed it. This file's own `verified` date is the date of the most recent full pass.
* Each reference doc also records an `accessed` date — the day the maintainer last opened the canonical source. That date is the evidence behind the reference's `verified` entry.
* A concept with no `verified` entry has not been through a claim-by-claim pass. That is a real signal for readers and agents, so leave it absent rather than asserting a check that did not happen.
* A scheduled workflow opens a weekly draft review report. It is a queue for human research, never approval or evidence by itself.

# Freshness tiers

| Tier | What it covers | Review cadence |
|---|---|---|
| **Volatile** | Named product names, eligibility thresholds, launch dates, rollout regions, API field names, protocol adoption status. Mostly the `agentic/` section. | Monthly, plus on any known vendor announcement. |
| **Semi-stable** | Survey figures, study percentages, ranking-factor framing. The `references/` studies. | Quarterly; re-check the source for a newer edition. |
| **Durable** | Method and detection docs, governance principles (HITL, NAP consistency, schema fundamentals). | Semi-annually, or when a dependency changes. |

# Review procedure

1. Run `python tool/okf_verify.py bundles/local-seo` and resolve every hard failure.
2. Run it with `--check-urls` to catch dead external links.
3. For each **volatile** claim, re-open the cited primary source and confirm the figure, name and status still match. Update the doc body and the reference's `accessed` date.
4. For every doc the pass actually covered, add or update its `verified: { by, at }` and roll `stale_after` forward by the tier cadence below. Leave docs the pass did not cover untouched.
5. Re-run `python tool/okf_build.py bundles/local-seo --name "Local SEO OKF"` to regenerate `viz.html`.
6. Append a dated entry to [log.md](/log.md) and update this file's own `verified` date.
7. File or update a dated verification report (see [the 2026-06-25 report](/references/verification-report-2026-06-25.md)) when a full claim-by-claim pass is done.
8. Require human approval before merging any factual update; automation must never auto-merge knowledge claims.

# Open follow-ups

Carried from the latest verification pass:

* Confirm whether Google has a current replacement for the earlier Maps grounding widget context token / "Contextual View".
* If OTA commission or rate-parity guidance is ever required, research it by jurisdiction, contract type and named platform rather than publishing a universal range.
