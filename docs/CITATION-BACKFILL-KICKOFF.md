# Kickoff — citation backfill and source attribution

A working brief, not knowledge. Delete it or convert it to issues once the work lands.

Opened 2026-07-27, immediately after the [OKF v0.2 migration](../bundles/local-seo/log.md). The migration moved provenance from `# Citations` body blocks into `sources` frontmatter and added the trust family. Doing that made two pre-existing gaps measurable for the first time. This brief closes them.

## First, a distinction that matters

**Nothing in this bundle is uncited.** All 55 concepts carry `sources`, and a scan for external links in bodies that are missing from frontmatter returns zero. The two gaps are narrower than "missing citations":

| Gap | Size | What is actually missing |
|---|---|---|
| **Track A — unverified** | 17 concepts | They have sources, but no dated claim-by-claim pass. They carry no `verified` key, so they read as the "unverified" tier. |
| **Track B — thin attribution** | 40 external URLs | They are cited, but as bare URLs in a `sources` entry. No publisher, no accessed date, no scope, no confidence — the provenance the 20 existing `Reference` docs carry. |

The tracks are independent. Track B spans the whole repo, including sections that are already verified; only 9 of its 40 URLs touch a Track A doc. Run them in either order, or in parallel by different people.

## Track A — verify the 17 unverified concepts

These are the `local-seo/`, `maps/` and `playbooks/` docs. They were written before the verification-report habit started with `agentic/` in June and `gbp/` in July, so they never got a pass.

They are short — 100 to 276 words each, about 3,000 words total — and most depend on in-bundle `Reference` docs that have already been checked. This is largely "does the body still say what the reference establishes", not fresh research.

### Group A1 — leans on already-verified references (13 docs)

The cited reference was verified on 2026-06-24/25. Confirm the concept's wording still matches its scope, and confirm the reference itself has not been superseded.

| Concept | Words | Cited reference(s) |
|---|---:|---|
| `local-seo/gbp-signals.md` | 233 | whitespark-2026 |
| `local-seo/local-onpage.md` | 244 | whitespark-2026 |
| `local-seo/local-schema.md` | 197 | whitespark-2026 |
| `local-seo/nap-citations.md` | 225 | brightlocal-apple-business-connect |
| `local-seo/local-authority-links.md` | 180 | ahrefs-ai-overviews |
| `local-seo/reviews-reputation.md` | 276 | sterling-sky, brightlocal-lcrs |
| `local-seo/ai-search-local.md` | 200 | google-ai-optimization-guide, seer-chatgpt-conversion, ahrefs-ai-overviews |
| `maps/capability-tiers.md` | 141 | dataforseo |
| `maps/competitor-radius.md` | 100 | dataforseo |
| `maps/gbp-profile-audit.md` | 123 | dataforseo |
| `maps/geo-grid-tracking.md` | 116 | dataforseo |
| `maps/review-intelligence.md` | 121 | sterling-sky, dataforseo |
| `playbooks/gbp-optimisation-checklist.md` | 249 | brightlocal-apple-business-connect, sterling-sky, ahrefs-ai-overviews |

Watch for the two named figures in this group — the Apple Business Connect adoption rate (~16%) and the Sterling Sky 18-day review-recency rule. Both are `note:` values on `sources` entries in `playbooks/gbp-optimisation-checklist.md`, and both are the kind of vendor-study number that goes stale quietly.

### Group A2 — cites bare external URLs (4 docs)

These overlap Track B. Verifying them and writing their `Reference` docs is the same sitting, so do both at once.

| Concept | Words | Bare URLs |
|---|---:|---|
| `local-seo/business-type-detection.md` | 161 | Google SAB help, `schema.org/areaServed` |
| `local-seo/industry-vertical-detection.md` | 193 | `schema.org/LocalBusiness`, Google categories |
| `maps/nap-verification.md` | 122 | Bing Places, Apple Business Connect, Nominatim |
| `maps/schema-generation.md` | 159 | `schema.org/LocalBusiness`, Google local-business and review-snippet structured data |

Both detection docs already say in a `# Provenance` section that they are heuristics "derived from observable page signals; not an externally published taxonomy". Keep that framing. The right verification outcome for those two may be that the *method* is unverifiable by nature and only its schema implications are checkable — record that rather than forcing a green tick.

### Definition of done — Track A

For each doc that genuinely passes:

```yaml
verified: { by: human:craigburton, at: <ISO datetime of the pass> }
stale_after: <verified date + tier cadence from maintenance.md>
```

Then file a dated verification report in `references/` in the same table format as [2026-07-06](../bundles/local-seo/references/verification-report-2026-07-06.md) — one row per claim, with the result column recording **Verified / Corrected / Dropped**, and append to `log.md`.

**A doc that fails its pass does not get `verified`.** Fix the body and leave it unverified until the next pass, or drop the claim. Partial credit is not a thing here; a `verified` key asserts the whole document was checked.

## Track B — credit 40 external sources properly

Every one of these is cited today as a bare URL in a `sources` entry. That satisfies OKF (only `resource` is required) but falls short of this repo's own bar, where a source is traceable and re-checkable.

By publisher:

| Publisher | URLs | Notes |
|---|---:|---|
| `support.google.com` | 12 | Living documents. `published: living document`, `accessed` is the real signal. |
| `developers.google.com` | 9 | API and structured-data docs; version/field names drift. |
| `blog.google` + `googleblog.blogspot.com` + `smallbusiness.googleblog.com` | 5 | Dated announcements — the strongest primary sources here. |
| `www.ftc.gov` | 2 | Regulator publications; cite the release, note it is not adjudication. |
| `schema.org` | 2 | Vocabulary definitions; effectively living documents. |
| `ucp.dev`, `agenticcommerce.dev`, `docs.cdp.coinbase.com`, `cloud.google.com`, `openai.com` | 5 | Protocol specs, fast-moving; treat as volatile. |
| `arxiv.org` | 1 | Preprint — label as not peer-reviewed. |
| `uberall.com` | 1 | Vendor case study — directional only, never a benchmark. |
| `bingplaces.com`, `businessconnect.apple.com`, `nominatim.org` | 3 | Product landing pages / docs, used as capability evidence. |

### Promote or enrich?

Do not mint 40 `Reference` docs reflexively; that would triple the reference set and bury the load-bearing sources among one-off links. Use this rule:

- **Promote to a `Reference` doc** when the source is load-bearing (a factual claim depends on it), when it is cited by 2+ concepts, or when it needs scope caveats. These 6 are cited by 2+ docs and should be promoted first:
  - `developers.google.com/my-business/content/update-food-menus`
  - `developers.google.com/my-business/reference/businessinformation/rest/v1/locations/patch`
  - `schema.org/LocalBusiness`
  - `support.google.com/business/answer/3038177` (categories / description rules)
  - `support.google.com/business/answer/9157481` (service-area businesses)
  - `support.google.com/contributionpolicy/answer/7400114` (cited by 3 docs)
- **Enrich in place** otherwise — keep the bare URL as a `sources` entry but add the v0.2 per-source signals so it is still attributable:

  ```yaml
  sources:
    - id: schema-area-served
      resource: https://schema.org/areaServed
      title: "Schema.org — areaServed"
      last_modified: 2026-05-30     # when the SOURCE changed, not when you read it
  ```

  Two traps in these optional signals:

  - `last_modified` means when the source itself last changed. If you cannot establish that, **omit it**. Do not put your own reading date there — that is `accessed`, and it belongs on a `Reference` doc.
  - `author` is loosely specified. §5.1 says it follows the §7 actor convention, but §7 defines only `human:<id>`, `process:<id>` and `<producer>/<version>` — none of which fit a publishing organisation, and the spec's own example uses an undefined `team:ga4-docs` form. Prefer omitting `author` and carrying the organisation in `publisher` on a `Reference` doc, where this repo already has a field for it.

### Reference doc template

Match the existing shape, e.g. [`google-local-ranking.md`](../bundles/local-seo/references/google-local-ranking.md):

```yaml
---
type: Reference
title: <Publisher — page title as published>
description: <One line: what this source establishes.>
resource: <canonical URL, no tracking or locale params>
publisher: <Organisation (product/section)>
published: <date | "living document" | "n.d.">
accessed: <ISO date you last opened it>
confidence: high | medium | low
scope: <What it does AND does not establish.>
tags: [reference, ...]
generated: { by: human:craigburton, at: <ISO datetime> }
verified:  { by: human:craigburton, at: <ISO datetime> }
status: stable
stale_after: <accessed + 3 months for references>
sources:
  - id: <slug>
    resource: <same canonical URL>
    title: <page title>
---
```

Then repoint the citing concept's `sources[].resource` from the bare URL to `/references/<slug>.md`, and keep the `id` stable so any `[^footnote]` still resolves.

### Definition of done — Track B

- Every promoted URL has a `Reference` doc with all six provenance fields, and no concept still cites it bare.
- Every enriched URL has at minimum `id`, `resource`, `title`.
- `scope` is written for every promoted source, and says what the source does **not** establish. This is the field that stops a Google help page being read as an algorithm disclosure.
- Vendor studies (`uberall.com`) and the preprint (`arxiv.org`) are explicitly labelled as directional / not peer-reviewed, per CONTRIBUTING's evidence rules.

## Fix while you are in there — URL canonicalisation

The same page is currently cited under two different `resource` values, so a consumer counts two sources where there is one:

- `support.google.com/business/answer/3038177` vs `…/3038177?hl=en`
- `support.google.com/business/answer/9157481` vs `…/9157481?hl=en`

Pick the no-`hl` form as canonical and strip locale/tracking params everywhere. Worth adding a verifier check that flags two `sources` entries whose resources differ only by query string — cheap, and it stops this recurring.

## Sequencing

1. **Canonicalise URLs** (small, mechanical, unblocks clean counting).
2. **Track B promotions** — the 6 multi-cited sources.
3. **Group A2** — the 4 docs that cite bare URLs, verified in the same sitting as their new `Reference` docs.
4. **Group A1** — the 13 reference-backed docs, batched by shared reference (all 4 `dataforseo` docs together, all 3 `whitespark` docs together) so each source is opened once.
5. **Track B enrichment** — the remaining ~34 URLs.
6. Regenerate, verify, log.

Batching by shared reference in step 4 is the whole efficiency play: 13 docs collapse to about 6 source-opening sessions.

## Guardrails

- **Never add `verified` without doing the check.** The 17 unverified docs are a truthful signal and a queue. Filling them in to make the dashboard green destroys the only thing the field is for.
- **`generated` does not change** unless you edit the body. Re-verifying is not regenerating.
- **A failed check is a result.** Correct or drop the claim and record it in the report, exactly as the 2026-07-06 pass did with the "$79M" figure and the SOCi 65% scope.
- **`human:` is reserved for a person.** If a script drafts a `Reference` stub, its `generated.by` is `<producer>/<version>`, and `verified` waits for the human pass.

## Commands

```bash
python tool/okf_verify.py bundles/local-seo --show-unverified   # the Track A queue
python tool/okf_verify.py bundles/local-seo --check-urls        # dead-link sweep before you start
python tool/okf_build.py  bundles/local-seo --name "Local SEO OKF"
python -m unittest discover -s tool -p "test_*.py"
```

Expect `RESULT: PASS (7 stale)` today. The 7 are the volatile `agentic/` docs on the monthly cadence — a separate queue from this brief, and the next one due.
