---
type: Report
title: Google Posts verification report — 2026-11-16
description: Claim-by-claim maintenance review of gbp/google-posts.md against its reopened sources, plus the weekly-posting wording fix across two GBP 2026 playbooks.
tags: [governance, verification, gbp, posts, maintenance]
generated: { by: iris/2026-W47, at: 2026-11-16T00:00:00Z }
status: draft
sources:
  - id: google-create-and-manage-posts-on
    resource: https://support.google.com/business/answer/7342169
    title: Google — Create and manage posts on your Business Profile (accessed 2026-11-16)
  - id: google-posts-content-policy
    resource: https://support.google.com/business/answer/7213077
    title: Google — Business Profile photos, videos & posts content policy (accessed 2026-11-16)
  - id: google-posts-content-policy-archive-2026-08-31
    resource: https://web.archive.org/web/20260831185738/https://support.google.com/business/answer/7213077
    title: Internet Archive — capture of Google's posts content policy on 31 August 2026 (accessed 2026-11-16)
  - id: uberall-crate-barrel-case-study
    resource: https://uberall.com/en-us/customers/how-crate-barrel-grew-google-visibility-by-31-while-saving-time
    title: Uberall — Crate & Barrel case study (accessed 2026-11-16)
  - id: google-gbp-playbook-2026-official
    resource: https://services.google.com/fh/files/helpcenter/1_official_gbp_best_practices_playbook_2026.pdf
    title: Google — GBP best practices playbook, 2026 edition (PDF; accessed 2026-11-16)
  - id: google-gbp-tours-2026
    resource: https://services.google.com/fh/files/helpcenter/1_tours_attractions_gbp_best_practices_playbook_2026.pdf
    title: Google — GBP best practices playbook for Tours & Attractions, 2026 edition (PDF; accessed 2026-11-16)
---

First batch of the stale-page backlog under the weekly cycle that took effect on 2026-11-16. One document was taken through the full pass: [Google Posts](/gbp/google-posts.md). It was chosen first because it sat inside a contradiction with two GBP 2026 playbooks about posting frequency.

The pass was carried out by an AI agent (`anthropic/claude-fable-5-2`, run as `iris/2026-W47`). Every source listed above was fetched live on 2026-11-16 and read in full; the two PDFs were downloaded and converted to text. No human has reviewed the result before this report was filed.

# Results

| Document | Result | Evidence |
|---|---|---|
| [gbp/google-posts.md](/gbp/google-posts.md) | Reconfirmed with corrections and two removals (below). Every claim left on the page was matched to a reopened source. `verified` updated, `stale_after` rolled to 2027-05-16 (durable tier, six months). | All four of its sources reopened.[^google-create-and-manage-posts-on][^google-posts-content-policy][^uberall-crate-barrel-case-study][^google-gbp-playbook-2026-official] |
| [playbooks/gbp-2026/master-overview.md](/playbooks/gbp-2026/master-overview.md) | One sentence reworded. **Not verified**: only the two sources behind that sentence were reopened. No `verified` entry added, `stale_after` unchanged. | [^google-gbp-playbook-2026-official][^google-posts-content-policy] |
| [playbooks/gbp-2026/tours-attractions.md](/playbooks/gbp-2026/tours-attractions.md) | One sentence reworded. **Not verified**: only the one source behind that sentence was reopened. No `verified` entry added, `stale_after` unchanged. | [^google-gbp-tours-2026] |

# The weekly-posting contradiction

* The posts help page and the posts content policy state no posting frequency.[^google-create-and-manage-posts-on][^google-posts-content-policy]
* Google's 2026 best-practices playbook lists "Post at least once a week" under Google Posts best practices, beside a Crate & Barrel case study.[^google-gbp-playbook-2026-official] The Tours & Attractions edition carries the same line.[^google-gbp-tours-2026]
* Both earlier statements were therefore partly right. The three pages now say the same thing: weekly is Google's recommendation in its playbook, and it is not a requirement.

# Claims checked on gbp/google-posts.md

| Claim | Result |
|---|---|
| Posts show in the Updates or Overview tab on mobile and "From the owner" on desktop | Confirmed.[^google-create-and-manage-posts-on] |
| Posts older than six months are archived unless a date range is set | Confirmed.[^google-create-and-manage-posts-on] |
| Update posts require a description | **Corrected.** The help page lists description, photo, video and button as things you can add and states no required field.[^google-create-and-manage-posts-on] |
| Offer posts require a title and start/end dates | **Corrected** to title, dates and time, as the help page words it.[^google-create-and-manage-posts-on] |
| Event posts: title, start and end dates and times; 24-hour display without times | Confirmed.[^google-create-and-manage-posts-on] |
| Current "Posts including contact information" policy wording, and the "Important" note on phone numbers | Confirmed word for word.[^google-posts-content-policy][^google-create-and-manage-posts-on] |
| Hotels cannot create offer posts (cited by the master playbook) | Confirmed.[^google-posts-content-policy] |
| "Google sets no required frequency" | **Corrected** by addition: true of the help pages, but Google's playbook recommends at least weekly.[^google-gbp-playbook-2026-official] |
| Posts "carry the only native call-to-action buttons on the profile" | **Removed.** None of the page's sources says this. Replaced with the supported statement that posts carry action buttons.[^google-create-and-manage-posts-on] |
| Case study: 161 locations in the US and Canada, +31% Maps views and +6% Search views 2024 against 2023, 95% profile completeness, Monday planning, UTM tracking | Confirmed.[^uberall-crate-barrel-case-study] |
| Google documents no ranking boost from posting | Confirmed as an absence: neither Google page nor the playbook states one.[^google-create-and-manage-posts-on][^google-posts-content-policy][^google-gbp-playbook-2026-official] |

# Source access notes and what a human still needs to check

* **Earlier "phone stuffing" policy wording.** Reconfirmed in a second attempt on 2026-11-16: the Internet Archive capture of 31 August 2026 shows the section "Avoid 'phone stuffing'" with the quoted wording.[^google-posts-content-policy-archive-2026-08-31] The page now cites that capture. Its earlier statement that the change happened before 25 September 2026 could not be reconfirmed and was removed; what is established is the old wording on 31 August and the new wording live on 16 November.
* **"Active-profile signal."** Both sentences saying that posting feeds an actively maintained profile signal were removed. None of the page's sources states it.
* **Featured posts.** The help page now describes featured posts for single-location food and drink businesses in five English-speaking countries.[^google-create-and-manage-posts-on] The Google Posts page does not cover this. Nothing was added; it is a candidate for a later edit.
* **Previous human verification.** The page's earlier `verified` entry was `human:craigburton` on 2026-07-06. This pass replaces it with an agent entry. A human reviewer may prefer to re-read the page and restore a human entry.
* **PDF text extraction.** The playbook PDFs are designed slides. The quoted line was read from extracted text and its position beside the case study was judged from layout.

# Changes made

* `gbp/google-posts.md`: cadence section rewritten; two table cells corrected; one unsupported phrase removed; playbook PDF added to `sources`; `generated`, `verified` and `stale_after` updated.
* `playbooks/gbp-2026/master-overview.md` and `playbooks/gbp-2026/tours-attractions.md`: weekly-posting sentence reworded as a recommendation; `generated` updated.
