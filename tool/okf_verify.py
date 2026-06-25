#!/usr/bin/env python3
"""
okf_verify.py — a strict, dependency-free quality gate for an OKF bundle.

Goes beyond tool/okf_build.py conformance. Checks, per bundle:

  HARD failures (exit 1):
    * missing / unparseable YAML frontmatter
    * empty or missing `type`
    * broken internal links (absolute /x.md and relative x.md)
    * missing `# Citations` block in a concept doc
    * non-sequential citation numbering ([1], [2], ... with no gaps/dupes)
    * stale draft markers (TODO, TBD, FIXME, XXX, DRAFT, "pending fact-check",
      "before publish")

  WARNINGS (do not fail the build):
    * `type` outside the controlled vocabulary
    * a `Reference` missing provenance frontmatter
      (publisher / published / accessed / confidence / scope)
    * orphaned documents (no inbound link from any other doc)
    * external URL not reachable  (only with --check-urls)

Usage:
    python3 okf_verify.py [BUNDLE_DIR] [--check-urls] [--allow-broken-links]
"""
import argparse
import os
import re
import sys

RESERVED = {"index.md", "log.md"}

# Controlled type vocabulary — keep in sync with docs/OKF-SPEC-SUMMARY.md.
TYPE_VOCAB = {
    "Concept", "Ranking Dimension", "Maps Analysis", "Detection Method",
    "Playbook", "Reference", "Policy", "Report",
}
REFERENCE_PROVENANCE = ("publisher", "published", "accessed", "confidence", "scope")

# Concept docs are expected to carry a Citations block. These governance/source
# types are exempt from the *body* citations requirement (References cite inline;
# Policy/Report are governance artefacts).
CITATIONS_EXEMPT = {"Reference", "Policy", "Report"}

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CITATION_MARK = re.compile(r"^\[(\d+)\]", re.MULTILINE)
STALE_MARKERS = [
    re.compile(r"\bTODO\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"\bXXX\b"),
    re.compile(r"\bDRAFT\b"),       # uppercase only — avoids "draft captions"
    re.compile(r"pending fact-check", re.IGNORECASE),
    re.compile(r"before\s+publish", re.IGNORECASE),
]


def parse_frontmatter(text):
    """Return (frontmatter_dict_or_None, body). Minimal YAML: key: value / key: [a, b]."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",") if v.strip()]
        else:
            fm[key] = val.strip('"').strip("'")
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle", nargs="?", default=".")
    ap.add_argument("--check-urls", action="store_true", help="probe external URLs (network)")
    ap.add_argument("--allow-broken-links", action="store_true",
                    help="treat broken internal links as a warning, not a failure")
    args = ap.parse_args()

    bundle = os.path.abspath(args.bundle)
    docs, files = collect(bundle)

    hard, warn = [], []
    inbound = {}                       # rel -> count of inbound links
    external_urls = set()

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

            # --- reference provenance ---
            if dtype == "Reference":
                missing = [k for k in REFERENCE_PROVENANCE if not str(fm.get(k, "")).strip()]
                if not str(fm.get("resource", "")).strip():
                    missing.append("resource")
                if missing:
                    warn.append(f"{rel}: Reference missing provenance: {', '.join(missing)}")

            # --- citations block + numbering ---
            if dtype not in CITATIONS_EXEMPT and not re.search(r"^#+\s*Citations\b", body, re.MULTILINE):
                hard.append(f"{rel}: missing '# Citations' block")
            nums = [int(n) for n in CITATION_MARK.findall(body)]
            if nums and nums != list(range(1, len(nums) + 1)):
                hard.append(f"{rel}: citation numbering not sequential 1..n -> {nums}")

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
    print(f"OKF verify: {bundle}")
    print(f"  documents: {len(docs)}  external URLs: {len(external_urls)}")
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
    print("\nRESULT: PASS" + ("  (warnings only)" if warn else "  (clean)"))


if __name__ == "__main__":
    main()
