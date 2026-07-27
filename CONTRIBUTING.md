# Contributing

Thank you for helping keep the Local SEO OKF accurate, current, and useful.

## Before opening a pull request

1. Search existing issues and pull requests for the same claim or source.
2. Put the page in the appropriate bundle folder and link it from an index.
3. Use bundle-relative Markdown links such as `/gbp/reviews.md`.
4. Add or update a reference page for material evidence, and list it in the
   page's `sources` frontmatter.
5. Update `generated` (`{ by, at }`) when you change a page's content.
6. Append a dated summary to `bundles/local-seo/log.md`.
7. Run the validation commands from the README and commit the regenerated
   `viz.html`.

## Trust fields

This bundle uses the OKF v0.2 trust family, and the fields mean exactly what
they say:

- `generated` records who wrote the current content. Use `human:<id>` when a
  person wrote or rewrote it; use `<producer>/<version>` for tool output.
- `verified` records a *completed check* against the sources. Only add it when
  a dated verification report covers the page, or — for a reference page — when
  you have re-opened the cited source and updated its `accessed` date. Never
  add `verified` to a page simply because it looks correct.
- `stale_after` follows the freshness tier in `bundles/local-seo/maintenance.md`,
  counted from the last verification.

Removing or backdating a `verified` entry is a legitimate change. If a page has
drifted from its sources, drop the entry rather than leaving a stale claim of
verification in place.

## Evidence rules

- Prefer current primary sources: official product documentation, policies,
  specifications, regulator publications, or original research.
- Label vendor studies and case studies as directional; do not generalise a
  single programme into a universal benchmark.
- State region, date, sample, eligibility, and product-version limitations.
- Do not present an observed correlation as a confirmed ranking factor.
- If a claim cannot be verified, remove it or identify it explicitly as an
  open research question rather than publishing it as guidance.

## Public-only boundary

Everything committed to this repository is public. Never include credentials,
customer or employee data, private operating procedures, RankinMaps admin
material, unpublished commercial information, or customer-specific Second
Brain content. Frontmatter declaring `audience: internal` is rejected.

## Contribution terms

By submitting a contribution, you confirm that you have the right to submit it
and agree that it is distributed under this repository's MIT License. Retain
source attribution and copyright notices where required.

All factual changes require human review. Scheduled automation may prepare a
draft review report, but it never approves or merges knowledge changes.
