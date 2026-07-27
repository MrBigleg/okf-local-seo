#!/usr/bin/env python3
"""
okf_verify.py — a strict, dependency-free quality gate for an OKF v0.2 bundle.

Goes beyond tool/okf_build.py conformance. Checks, per bundle:

  HARD failures (exit 1):
    * missing / unparseable YAML frontmatter
    * empty or missing `type`
    * missing or malformed `generated` (§5.2) — `by` must follow the actor
      convention (§7) and `at` must be an ISO 8601 datetime
    * malformed `verified` entries (§5.2)
    * `status` outside draft | stable | deprecated (§5.4)
    * `stale_after` that is not a plain YYYY-MM-DD date (§5.5)
    * missing `sources` on a knowledge doc, or a `sources` entry with no
      `resource` / no `id` / a duplicate `id` (§5.1)
    * a `[^label]` footnote with no matching `sources[].id` (§5.1)
    * broken internal links (absolute /x.md and relative x.md), including
      bundle-internal `sources[].resource` paths
    * stale draft markers (TODO, TBD, FIXME, XXX, DRAFT, "pending fact-check",
      "before publish")
    * `audience: internal` content in this public-only repository
    * v0.1 residue: a surviving `timestamp` key or `# Citations` body block,
      both superseded in v0.2 (§13.1)

  WARNINGS (do not fail the build):
    * `type` outside the controlled vocabulary
    * a `Reference` missing provenance frontmatter
      (publisher / published / accessed / confidence / scope)
    * a concept past its `stale_after` date (§5.5) — due for review
    * a concept with no `verified` entry (§5.3 "unverified" tier) — informational
    * orphaned documents (no inbound link from any other doc)
    * two `sources` entries whose `resource` differs only by query string
      (e.g. `?hl=en`) — the same page double-counted as two sources
    * external URL not reachable  (only with --check-urls)

Usage:
    python3 okf_verify.py [BUNDLE_DIR] [--check-urls] [--allow-broken-links]
                          [--show-unverified] [--as-of YYYY-MM-DD]
"""
import argparse
import os
import re
import sys
from datetime import date

RESERVED = {"index.md", "log.md"}

# Controlled type vocabulary — keep in sync with docs/OKF-SPEC-SUMMARY.md.
TYPE_VOCAB = {
    "Concept", "Ranking Dimension", "Maps Analysis", "Detection Method",
    "Playbook", "Reference", "Policy", "Report",
}
REFERENCE_PROVENANCE = ("publisher", "published", "accessed", "confidence", "scope")

# Governance artefacts describe the bundle itself rather than external claims,
# so they are exempt from the `sources` requirement.
SOURCES_EXEMPT = {"Policy", "Report"}

STATUS_VALUES = {"draft", "stable", "deprecated"}

# §7 actor convention: human:<id> | process:<id> | <producer>/<version>
ACTOR = re.compile(r"^(?:human:[\w.@-]+|process:[\w.@-]+|[\w.-]+/[\w.:-]+)$")
ISO_DT = re.compile(r"^\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:?\d{2})?)?$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FOOTNOTE_REF = re.compile(r"(?<!\])\[\^([^\]]+)\](?!:)")
STALE_MARKERS = [
    re.compile(r"\bTODO\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"\bXXX\b"),
    re.compile(r"\bDRAFT\b"),       # uppercase only — avoids "draft captions"
    re.compile(r"pending fact-check", re.IGNORECASE),
    re.compile(r"before\s+publish", re.IGNORECASE),
]


# --------------------------------------------------------------------------
# Minimal YAML subset parser.
#
# Deliberately dependency-free. Handles exactly what OKF frontmatter needs:
# scalars, inline flow maps ({ by: x, at: y }), inline flow sequences
# ([a, b]), and block sequences of mappings (the `sources` shape).
# --------------------------------------------------------------------------
def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def _flow_map(s):
    out = {}
    for part in s.strip()[1:-1].split(","):
        k, sep, v = part.partition(":")
        if sep and k.strip():
            out[k.strip()] = _scalar(v)
    return out


def _flow_seq(s):
    return [_scalar(p) for p in s.strip()[1:-1].split(",") if p.strip()]


def parse_frontmatter(text):
    """Return (frontmatter_dict_or_None, body)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")

    fm, key, lst, cur = {}, None, None, None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        stripped = line.strip()
        if line[:1] not in (" ", "\t"):                      # top-level key
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", stripped)
            if not m:
                continue
            key, val = m.group(1), m.group(2)
            lst = cur = None
            if val == "":
                fm[key] = []
                lst = fm[key]
            elif val.startswith("{"):
                fm[key] = _flow_map(val)
            elif val.startswith("["):
                fm[key] = _flow_seq(val)
            else:
                fm[key] = _scalar(val)
        elif stripped.startswith("- "):                      # block sequence item
            item = stripped[2:].strip()
            if lst is None:
                fm[key] = lst = fm[key] if isinstance(fm.get(key), list) else []
            if item.startswith("{"):
                lst.append(_flow_map(item))
                cur = None
            elif ":" in item:
                k, _, v = item.partition(":")
                cur = {k.strip(): _scalar(v)}
                lst.append(cur)
            else:
                lst.append(_scalar(item))
                cur = None
        elif cur is not None and ":" in stripped:            # continuation of a map item
            k, _, v = stripped.partition(":")
            cur[k.strip()] = _scalar(v)
    return fm, body


def collect(bundle):
    """Walk the bundle. Return (docs, file_set). docs is a list of dicts."""
    docs, files = [], set()
    for root, _, names in os.walk(bundle):
        for fn in sorted(names):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, bundle).replace(os.sep, "/")
            files.add(rel)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            docs.append({"rel": rel, "name": fn, "dir": os.path.dirname(rel), "text": text})
    return docs, files


def resolve_link(target, doc_dir):
    """Resolve a markdown link target to a bundle-relative path, or None if external/non-md."""
    t = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not t or t.startswith(("http://", "https://", "mailto:")):
        return None
    if t.endswith("/"):                # directory link -> that directory's index.md
        t += "index.md"
    if t.startswith("/"):
        path = t.lstrip("/")
    else:
        path = os.path.normpath(os.path.join(doc_dir, t)).replace(os.sep, "/")
    return path


def check_actor_event(rel, label, ev, hard):
    """Validate one { by, at } trust event (§5.2 / §7)."""
    if not isinstance(ev, dict):
        hard.append(f"{rel}: {label} must be a mapping with 'by' and 'at'")
        return
    by, at = str(ev.get("by", "")).strip(), str(ev.get("at", "")).strip()
    if not by:
        hard.append(f"{rel}: {label} missing required 'by'")
    elif not ACTOR.match(by):
        hard.append(f"{rel}: {label}.by '{by}' breaks the actor convention "
                    f"(human:<id> | process:<id> | <producer>/<version>)")
    if at and not ISO_DT.match(at):
        hard.append(f"{rel}: {label}.at '{at}' is not an ISO 8601 datetime")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle", nargs="?", default=".")
    ap.add_argument("--check-urls", action="store_true", help="probe external URLs (network)")
    ap.add_argument("--allow-broken-links", action="store_true",
                    help="treat broken internal links as a warning, not a failure")
    ap.add_argument("--show-unverified", action="store_true",
                    help="list documents with no `verified` entry (§5.3 unverified tier)")
    ap.add_argument("--as-of", default=date.today().isoformat(),
                    help="date used for stale_after comparison (default: today)")
    args = ap.parse_args()

    bundle = os.path.abspath(args.bundle)
    docs, files = collect(bundle)

    hard, warn, unverified, stale = [], [], [], []
    inbound = {}                       # rel -> count of inbound links
    external_urls = set()
    # base URL (query string stripped) -> { full resource -> [rel, ...] }
    resource_variants = {}

    for d in docs:
        rel, name, text = d["rel"], d["name"], d["text"]
        is_reserved = name in RESERVED

        # --- frontmatter / type ---
        if is_reserved:
            fm, body = (None, text)
            # only the bundle-root index may carry frontmatter
            if name == "index.md" and text.startswith("---") and rel != "index.md":
                warn.append(f"{rel}: non-root index.md carries frontmatter")
            dtype = None
        else:
            fm, body = parse_frontmatter(text)
            if fm is None:
                hard.append(f"{rel}: missing/unparseable YAML frontmatter")
                continue
            dtype = str(fm.get("type", "")).strip()
            if not dtype:
                hard.append(f"{rel}: frontmatter missing non-empty 'type'")
            elif dtype not in TYPE_VOCAB:
                warn.append(f"{rel}: type '{dtype}' is outside the controlled vocabulary")
            if str(fm.get("audience", "")).strip().lower() == "internal":
                hard.append(f"{rel}: audience 'internal' is forbidden in the public bundle")

            # --- v0.1 residue (§13.1) ---
            if "timestamp" in fm:
                hard.append(f"{rel}: 'timestamp' is superseded by 'generated.at' in v0.2")
            if re.search(r"^#+\s*Citations\b", body, re.MULTILINE):
                hard.append(f"{rel}: '# Citations' body list is superseded by 'sources' in v0.2")

            # --- trust: generated / verified (§5.2) ---
            if "generated" not in fm:
                hard.append(f"{rel}: missing 'generated' ({{ by, at }})")
            else:
                check_actor_event(rel, "generated", fm["generated"], hard)

            ver = fm.get("verified")
            if ver is None:
                unverified.append(rel)
            else:
                # §11: a bare mapping MUST be treated as a one-element list.
                for i, ev in enumerate(ver if isinstance(ver, list) else [ver]):
                    check_actor_event(rel, f"verified[{i}]", ev, hard)

            # --- lifecycle: status / stale_after (§5.4, §5.5) ---
            status = str(fm.get("status", "")).strip()
            if status and status not in STATUS_VALUES:
                hard.append(f"{rel}: status '{status}' not in {sorted(STATUS_VALUES)}")
            sa = str(fm.get("stale_after", "")).strip()
            if sa:
                if not ISO_DATE.match(sa):
                    hard.append(f"{rel}: stale_after '{sa}' must be a plain YYYY-MM-DD date")
                elif args.as_of >= sa:
                    stale.append(f"{rel}: stale since {sa} - due for review")

            # --- provenance: sources (§5.1) ---
            srcs = fm.get("sources") or []
            if not isinstance(srcs, list):
                hard.append(f"{rel}: 'sources' must be a list")
                srcs = []
            if dtype not in SOURCES_EXEMPT and not srcs:
                hard.append(f"{rel}: missing 'sources' provenance")
            seen_ids = set()
            for s in srcs:
                if not isinstance(s, dict):
                    hard.append(f"{rel}: sources entry must be a mapping")
                    continue
                res = str(s.get("resource", "")).strip()
                sid = str(s.get("id", "")).strip()
                if not res:
                    hard.append(f"{rel}: sources entry missing required 'resource'")
                if not sid:
                    hard.append(f"{rel}: sources entry for '{res or '?'}' missing 'id'")
                elif sid in seen_ids:
                    hard.append(f"{rel}: duplicate sources id '{sid}'")
                else:
                    seen_ids.add(sid)
                # bundle-internal source paths must resolve
                if res.startswith("/") and res.endswith(".md"):
                    if res.lstrip("/") not in files:
                        msg = f"{rel}: sources '{sid}' -> missing {res}"
                        (warn if args.allow_broken_links else hard).append(msg)
                    else:
                        inbound[res.lstrip("/")] = inbound.get(res.lstrip("/"), 0) + 1
                elif res.startswith(("http://", "https://")):
                    external_urls.add(res)
                    base = res.split("?", 1)[0]
                    resource_variants.setdefault(base, {}).setdefault(res, []).append(rel)

            # --- per-claim footnotes must join to sources[].id (§5.1) ---
            for label in set(FOOTNOTE_REF.findall(body)):
                if label not in seen_ids:
                    hard.append(f"{rel}: footnote [^{label}] has no matching sources[].id")

            # --- reference provenance ---
            if dtype == "Reference":
                missing = [k for k in REFERENCE_PROVENANCE if not str(fm.get(k, "")).strip()]
                if not str(fm.get("resource", "")).strip():
                    missing.append("resource")
                if missing:
                    warn.append(f"{rel}: Reference missing provenance: {', '.join(missing)}")

        # --- stale draft markers (all non-reserved docs) ---
        if not is_reserved:
            for pat in STALE_MARKERS:
                m = pat.search(body if fm is not None else text)
                if m:
                    hard.append(f"{rel}: stale draft marker '{m.group(0)}'")
                    break

        # --- link extraction (every doc, incl. index/log) ---
        scan = body if (not is_reserved and fm is not None) else text
        for tgt in MD_LINK.findall(scan):
            if tgt.startswith(("http://", "https://")):
                external_urls.add(tgt)
                continue
            path = resolve_link(tgt, d["dir"])
            if path is None:
                continue
            if path not in files:
                msg = f"{rel}: broken internal link -> {tgt}"
                (warn if args.allow_broken_links else hard).append(msg)
            else:
                inbound[path] = inbound.get(path, 0) + 1

    # --- sources resources that differ only by query string (§5.1) ---
    for base, variants in resource_variants.items():
        if len(variants) > 1:
            where = "; ".join(f"{res} ({', '.join(rels)})" for res, rels in sorted(variants.items()))
            warn.append(f"sources resources differ only by query string for {base}: {where}")

    # --- orphan detection (concept/source/governance docs only) ---
    for d in docs:
        rel, name = d["rel"], d["name"]
        if name in RESERVED:
            continue
        if inbound.get(rel, 0) == 0:
            warn.append(f"{rel}: orphaned (no inbound links from any document)")

    # --- external URL probe ---
    if args.check_urls:
        import urllib.request
        import urllib.error
        # Browser-like UA; many sites (e.g. Google support) 404/403 bot HEADs.
        ua = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

        def probe(url, method):
            req = urllib.request.Request(url, method=method, headers={"User-Agent": ua})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status

        print(f"Probing {len(external_urls)} external URLs ...")
        for url in sorted(external_urls):
            try:
                code = probe(url, "HEAD")
            except urllib.error.HTTPError as e:
                code = e.code
            except Exception as e:                      # noqa: BLE001 - try GET before giving up
                code = None
                head_err = e.__class__.__name__
            else:
                head_err = None
            # Many servers mishandle HEAD; confirm a "failure" with a real GET.
            if code is None or code >= 400:
                try:
                    code = probe(url, "GET")
                except urllib.error.HTTPError as e:
                    warn.append(f"URL {e.code}: {url}")
                    continue
                except Exception as e:                  # noqa: BLE001 - report and continue
                    warn.append(f"URL unreachable ({head_err or e.__class__.__name__}): {url}")
                    continue
                if code >= 400:
                    warn.append(f"URL {code}: {url}")

    # --- report ---
    print(f"OKF verify (v0.2): {bundle}")
    print(f"  documents: {len(docs)}  external URLs: {len(external_urls)}")
    print(f"  trust: {len(docs) - len(unverified) - sum(1 for d in docs if d['name'] in RESERVED)}"
          f" verified / {len(unverified)} unverified")

    if stale:
        print(f"\n  STALE ({len(stale)}):")
        for s in stale:
            print(f"    ~ {s}")
    if args.show_unverified and unverified:
        print(f"\n  UNVERIFIED ({len(unverified)}):")
        for u in unverified:
            print(f"    ? {u}")
    if warn:
        print(f"\n  WARNINGS ({len(warn)}):")
        for w in warn:
            print(f"    ! {w}")
    if hard:
        print(f"\n  HARD FAILURES ({len(hard)}):")
        for h in hard:
            print(f"    x {h}")
        print("\nRESULT: FAIL")
        sys.exit(1)
    notes = ", ".join(n for n in (f"{len(warn)} warnings" if warn else "",
                                  f"{len(stale)} stale" if stale else "") if n)
    print("\nRESULT: PASS" + (f"  ({notes})" if notes else "  (clean)"))


if __name__ == "__main__":
    main()
