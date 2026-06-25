---
type: Policy
title: Maintenance Policy
description: Ownership, review cadence and freshness tiers for keeping fast-moving claims in this bundle accurate.
owner: CTB Marketing (bundle maintainer)
last_verified: 2026-06-25
review_cadence: quarterly (volatile claims monthly — see tiers)
tags: [governance, maintenance, policy]
timestamp: 2026-06-25T00:00:00Z
---

This bundle mixes durable principles with fast-moving product facts. This policy says who keeps it current, how often, and how to tell which claims need the closest watch.

# Ownership

* **Owner:** CTB Marketing (bundle maintainer).
* The owner is accountable for the scheduled reviews below and for re-running `tool/okf_verify.py` before any export or release.
* Each reference doc records its own `accessed` date in frontmatter; each concept records a `timestamp`. The `last_verified` date in this file is the date of the most recent full pass.

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
4. Re-run `python tool/okf_build.py bundles/local-seo --name "Local SEO OKF"` to regenerate `viz.html`.
5. Append a dated entry to the bundle `log.md` and update `last_verified` above.
6. File or update a dated verification report (see [the 2026-06-25 report](/references/verification-report-2026-06-25.md)) when a full claim-by-claim pass is done.

# Open follow-ups

Carried from the latest verification pass:

* Confirm whether Google has a current replacement for the earlier Maps grounding widget context token / "Contextual View".
* If OTA commission or rate-parity guidance is ever required, research it by jurisdiction, contract type and named platform rather than publishing a universal range.
