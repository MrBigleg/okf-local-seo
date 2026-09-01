---
name: okf-maintenance-review
description: Perform a claim-by-claim OKF maintenance review — reopen every primary source behind due documents, reconfirm or correct claims, roll freshness dates forward, and write the dated verification report. Use when a weekly/monthly review is due, when picking up an automation/weekly-okf-review-* branch, or when the user asks to "run the maintenance review", "verify the agentic docs", "close out the review queue", or similar.
---

# OKF Maintenance Review

This skill turns the repo's automated **review queue** (an empty checklist naming
pages that are due) into a **completed review** (sources reopened, claims
reconfirmed or corrected, dates rolled forward, a dated report on record). It
codifies the pass done manually in the 2026-08-27 follow-up review and the
2026-09-01 agentic monthly review — see `bundles/local-seo/log.md` for those
entries and their linked reports for worked examples.

Read `bundles/local-seo/maintenance.md` first if you haven't — it owns the
freshness tiers, cadence and review procedure this skill automates. This
skill does not override that policy; it executes it.

## When this runs

- A `automation/weekly-okf-review-*` branch/PR exists with pages listed under
  "Pages due for freshness review" (non-empty table) — the scheduled
  `weekly-review.yml` workflow prepares these but never researches them.
- `python tool/okf_verify.py bundles/local-seo` reports one or more `STALE`
  documents.
- The user asks directly for a review pass (e.g. "run this month's agentic
  review", "verify the maps/ docs").
- A specific low-effort follow-up issue asks for a single source to be
  manually reopened (e.g. a blocked automated fetch).

## Procedure

1. **Scope the pass.** Run `python tool/okf_verify.py bundles/local-seo` and
   note every `STALE` document, or use the due-pages table from the weekly
   review branch. Don't touch documents that aren't due — the maintenance
   policy is explicit that untouched docs keep their existing `verified`.

2. **Collect every primary source per document.** Read each due document's
   frontmatter `sources[]`. Where `resource` points at `/references/*.md`
   rather than a live URL, open that reference doc and follow its own
   `sources[].resource` to the actual external URL — reference docs are the
   indirection layer, not the evidence.

3. **Reopen every source directly.** Fetch each unique URL live (firecrawl
   scrape, or WebFetch as fallback). Do not rely on cached/trained knowledge
   of what a page says — the whole point of the pass is independent
   reconfirmation. Batch fetches to respect rate limits; retry on 429s rather
   than giving up after one failure.
   - If a fetch is blocked (403, bot-detection, gated content), try one
     alternate path before logging it as an access exception: a publisher's
     own site mirror, a differently-formatted URL, or a targeted search. Only
     write it up as an access exception (per the pattern in
     `verification-report-2026-08-01-agentic.md` and
     `verification-report-2026-09-01-agentic.md`) after that's exhausted.

4. **Check every claim against the live source**, not just the headline
   figure — dates, eligibility thresholds, field names, status wording
   ("coming soon" vs shipped), counts. Where a claim has drifted, correct the
   document body and cite the change explicitly in the report; where it's
   confirmed unchanged, no body edit is needed.

5. **Update frontmatter only for documents actually covered this pass:**
   - `verified: { by: <actor>, at: <ISO date> }` — actor follows the
     convention in `tool/okf_verify.py` (`human:<id>`, `process:<id>`, or
     `<producer>/<version>`, e.g. `anthropic/claude-sonnet-5`).
   - `stale_after` rolled forward from today by the tier cadence in
     `maintenance.md` (volatile = 1 month, semi-stable = 1 quarter, durable =
     6 months) — not from the old `stale_after` date.

6. **Write a dated verification report** at
   `bundles/local-seo/references/verification-report-<YYYY-MM-DD>-<scope>.md`,
   type `Report`, following the structure of the two examples above: a
   results table (document → result → primary-source evidence links), a
   source-access-notes section for any exceptions, and a changes-made list.
   Link it from `references/index.md` under "Bundle governance" (newest
   first).

7. **Log it.** Append a dated entry to `bundles/local-seo/log.md` (newest
   entry at the top, under a new `## <date>` heading) summarizing what was
   checked and what changed.

8. **Rebuild and verify:**
   ```
   python tool/okf_build.py bundles/local-seo --name "Local SEO OKF"
   python tool/okf_verify.py bundles/local-seo
   ```
   Confirm `RESULT: PASS` and that the documents just reviewed no longer
   appear in the `STALE` list.

9. **Respect the human-review gate.** Per `maintenance.md`, no factual update
   merges without human approval. Default to committing on a branch and
   opening a PR for review rather than pushing straight to `main` — only push
   directly if the operator explicitly asks for that (as happened in this
   session's precedent). If the pass was triggered by an
   `automation/weekly-okf-review-*` branch, commit onto that same branch and
   mark its PR ready for review instead of opening a new one.

10. **Surface anything you couldn't finish.** A source that stays genuinely
    inaccessible, a claim you can't confirm either way, or a correction that
    needs a human judgment call — file it as a new GitHub issue (label
    `documentation`, same as the existing follow-up issues in this repo)
    rather than silently skipping it or guessing.

## Non-goals

- Don't invent `last_modified` dates a source doesn't state.
- Don't roll `stale_after` forward on a document you didn't actually reopen
  sources for.
- Don't merge factual changes without a human in the loop, and don't delete
  or force-push anything as part of this skill — branch/PR hygiene is a
  separate, lower-stakes concern from claim verification.

## Reusable housekeeping check (optional, run alongside)

While in the repo for a review pass, it's cheap to also check for merged or
empty `automation/weekly-okf-review-*` branches (`git branch -a`, `gh pr list
--state all`) and flag or delete ones that are fully superseded — see the
2026-08-31 session for the worked example. This is separate from claim
verification and never needs the human-review gate, but still confirm with
the operator before deleting anything.
