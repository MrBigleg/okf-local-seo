#!/usr/bin/env python3
"""
okf_build.py — validate an OKF v0.2 bundle and generate a self-contained viz.html.

Usage:
    python3 okf_build.py [BUNDLE_DIR] [--name "Display Name"] [--out viz.html]

No third-party dependencies. Re-run it any time the bundle grows.
"""
import argparse
import html
import json
import os
import re
import sys

# The v0.2 frontmatter families (`sources`, `generated`, `verified`) are nested,
# so both tools share one YAML-subset parser. They always ship together.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from okf_verify import parse_frontmatter  # noqa: E402

RESERVED = {"index.md", "log.md"}
LINK_RE = re.compile(r"\[([^\]]+)\]\((/[^)]+\.md)\)")  # bundle-relative links to concepts


def trust_tier(fm):
    """Derive the §5.3 trust tier from `verified`, lowest to highest."""
    ver = fm.get("verified")
    if not ver:
        return "unverified"
    events = ver if isinstance(ver, list) else [ver]
    if any(str(e.get("by", "")).startswith("human:") for e in events if isinstance(e, dict)):
        return "human-reviewed"
    return "machine-confirmed"


def collect(bundle):
    concepts, errors, reserved = [], [], set()
    for root, dirs, files in os.walk(bundle):
        dirs.sort()
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, bundle).replace(os.sep, "/")
            with open(path, encoding="utf-8") as f:
                text = f.read()
            if fn in RESERVED:
                # reserved navigation files (index.md, log.md): valid link targets,
                # but not knowledge nodes. Record the id so links to them resolve.
                reserved.add(rel[:-3])
                continue
            fm, body = parse_frontmatter(text)
            if fm is None:
                errors.append(f"{rel}: missing/!parseable YAML frontmatter")
                continue
            if not fm.get("type"):
                errors.append(f"{rel}: frontmatter missing required 'type'")
            cid = rel[:-3]  # strip .md
            links = [m.group(2)[1:-3] for m in LINK_RE.finditer(body)]  # strip leading '/' and '.md'
            srcs = [s for s in (fm.get("sources") or []) if isinstance(s, dict)]
            # `sources` entries pointing into the bundle are provenance edges too,
            # so the graph keeps the citation links it used to read from
            # the v0.1 "# Citations" body block.
            links += [str(s["resource"])[1:-3] for s in srcs
                      if str(s.get("resource", "")).startswith("/")
                      and str(s.get("resource", "")).endswith(".md")]
            concepts.append({
                "id": cid,
                "type": fm.get("type", "Concept"),
                "title": fm.get("title", os.path.basename(cid).replace("-", " ").title()),
                "description": fm.get("description", ""),
                "resource": fm.get("resource", ""),
                "tags": fm.get("tags", []) if isinstance(fm.get("tags", []), list) else [fm.get("tags")],
                "body": body,
                "links": links,
                "sources": srcs,
                "trust": trust_tier(fm),
                "status": fm.get("status", "stable"),
                "stale_after": fm.get("stale_after", ""),
            })
    return concepts, errors, reserved


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__NAME__ — OKF</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
*{box-sizing:border-box}body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:#1a1a2e}
header{padding:14px 20px;background:#0f3460;color:#fff;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
header h1{font-size:18px;margin:0;font-weight:600}
header input,header select{padding:6px 10px;border-radius:6px;border:1px solid #2a4a7a;background:#16213e;color:#fff;font-size:13px}
#wrap{display:flex;height:calc(100vh - 52px)}
#cy{flex:1;background:#f4f6fb}
#panel{width:420px;max-width:46vw;overflow:auto;padding:22px 26px;border-left:1px solid #dde3ee;background:#fff}
#panel h2{margin:0 0 4px;font-size:20px}
.meta{color:#5a6b8c;font-size:13px;margin-bottom:14px}
.tag{display:inline-block;background:#e8eefb;color:#0f3460;border-radius:12px;padding:2px 9px;font-size:11px;margin:2px 4px 2px 0}
.trust{display:inline-block;border-radius:12px;padding:2px 9px;font-size:11px;margin:2px 4px 2px 0;border:1px solid}
.trust.human-reviewed{background:#e6f7ef;color:#1b7a4f;border-color:#a8dcc3}
.trust.machine-confirmed{background:#eef2fb;color:#3a5a94;border-color:#c2d0ea}
.trust.unverified{background:#f4f5f7;color:#6b7280;border-color:#d5d9e0}
.trust.stale{background:#fdf0e6;color:#a4501a;border-color:#f0c9a8}
.trust.status{background:#fdf6e3;color:#8a6d1f;border-color:#e8d9a8}
.sources{border-top:1px solid #eef1f7;margin-top:14px;padding-top:10px;font-size:13px}
.sources ol{margin:6px 0 0;padding-left:20px}
.sources li{margin:3px 0}
.body{border-top:1px solid #eef1f7;margin-top:14px;padding-top:14px}
.body table{border-collapse:collapse;width:100%;margin:10px 0}.body th,.body td{border:1px solid #dde3ee;padding:5px 8px;font-size:13px;text-align:left}
.body code{background:#f4f6fb;padding:1px 5px;border-radius:4px;font-size:12px}
.body pre{background:#16213e;color:#e8eefb;padding:12px;border-radius:8px;overflow:auto}
.body pre code{background:none;color:inherit}
.backlinks{margin-top:18px;font-size:13px}.backlinks a{display:block;color:#0f3460;margin:3px 0;cursor:pointer}
a.xlink{color:#0f3460;cursor:pointer;text-decoration:underline}
a.navlink{color:#5a6b8c;cursor:default;text-decoration:none}
.hint{color:#8a98b5;font-size:13px}
</style></head><body>
<header>
  <h1>__NAME__</h1>
  <input id="search" placeholder="Search title, id, tag…" size="22">
  <select id="typeFilter"></select>
  <select id="layout">
    <option value="cose">cose</option><option value="concentric">concentric</option>
    <option value="breadthfirst">breadthfirst</option><option value="circle">circle</option><option value="grid">grid</option>
  </select>
  <span class="hint">__COUNT__ concepts · click a node</span>
</header>
<div id="wrap"><div id="cy"></div>
<div id="panel"><p class="hint">Select a concept in the graph to read it here.</p></div></div>
<script>
const DATA = __DATA__;
const byId = {}; DATA.forEach(c => byId[c.id] = c);
const palette = {};
const colors = ["#0f3460","#e94560","#16a085","#8e44ad","#d35400","#2980b9","#27ae60","#c0392b","#7f8c8d"];
DATA.forEach(c => { if(!(c.type in palette)) palette[c.type] = colors[Object.keys(palette).length % colors.length]; });

const TODAY = new Date().toISOString().slice(0,10);
const TRUST_LABEL = {"human-reviewed":"human-reviewed","machine-confirmed":"machine-confirmed","unverified":"unverified"};

const elements = [];
DATA.forEach(c => elements.push({data:{id:c.id,label:c.title,type:c.type,trust:c.trust,
  stale:(c.stale_after&&TODAY>=c.stale_after)?1:0}}));
const seen = new Set();
DATA.forEach(c => c.links.forEach(t => { if(byId[t]){const k=c.id+"->"+t; if(!seen.has(k)){seen.add(k);elements.push({data:{id:k,source:c.id,target:t}});}}}));

const cy = cytoscape({container:document.getElementById("cy"),elements,
  style:[
    {selector:"node",style:{"background-color":ele=>palette[ele.data("type")]||"#888","label":"data(label)","font-size":"10px","color":"#1a1a2e","text-wrap":"wrap","text-max-width":"110px","text-valign":"bottom","text-margin-y":"3px","width":"22px","height":"22px"}},
    {selector:"edge",style:{"width":1.2,"line-color":"#b8c4dd","target-arrow-color":"#b8c4dd","target-arrow-shape":"triangle","curve-style":"bezier","arrow-scale":0.8}},
    {selector:".faded",style:{"opacity":0.15}},
    // §5.3 trust tiers: unverified reads as hollow, stale gets an amber ring.
    {selector:'node[trust="unverified"]',style:{"border-width":2,"border-color":"#9aa8c4","border-opacity":0.9,"background-opacity":0.35}},
    {selector:"node[stale=1]",style:{"border-width":3,"border-color":"#d35400"}},
    {selector:".sel",style:{"border-width":3,"border-color":"#e94560"}}
  ],
  layout:{name:"cose",animate:false,padding:30}});

const tf = document.getElementById("typeFilter");
tf.innerHTML = '<option value="">all types</option>' + Object.keys(palette).map(t=>`<option>${t}</option>`).join("");

function render(c){
  let b = marked.parse(c.body);
  b = b.replace(/href="(\\/[^"]+)\\.md"/g,'class="xlink" data-id="$1" href="javascript:void(0)"').replace(/data-id="\\//g,'data-id="');
  const backlinks = DATA.filter(o=>o.links.includes(c.id));
  document.getElementById("panel").innerHTML =
    `<h2>${c.title}</h2><div class="meta"><span class="tag" style="background:${palette[c.type]};color:#fff">${c.type}</span> ${c.id}</div>`+
    `<div class="meta"><span class="trust ${c.trust}">${TRUST_LABEL[c.trust]||c.trust}</span>`+
      (c.status&&c.status!=="stable"?`<span class="trust status">${c.status}</span>`:"")+
      (c.stale_after&&TODAY>=c.stale_after?`<span class="trust stale">stale since ${c.stale_after}</span>`:"")+
    `</div>`+
    (c.description?`<p>${c.description}</p>`:"")+
    (c.resource?`<p class="hint">resource: <a href="${c.resource}" target="_blank">${c.resource}</a></p>`:"")+
    (c.tags&&c.tags.length?`<div>${c.tags.map(t=>`<span class="tag">${t}</span>`).join("")}</div>`:"")+
    `<div class="body">${b}</div>`+
    (c.sources&&c.sources.length?`<div class="sources"><strong>Sources</strong><ol>`+
      c.sources.map(s=>{const r=String(s.resource||"");
        const inner = r.startsWith("/")&&r.endsWith(".md")
          ? `<a class="xlink" data-id="${r.slice(1,-3)}">${s.title||r}</a>`
          : `<a href="${r}" target="_blank">${s.title||r}</a>`;
        return `<li>${inner}${s.note?` — ${s.note}`:""}</li>`;}).join("")+
      `</ol></div>`:"")+
    (backlinks.length?`<div class="backlinks"><strong>Cited by</strong>${backlinks.map(o=>`<a class="xlink" data-id="${o.id}">${o.title}</a>`).join("")}</div>`:"");
  document.querySelectorAll(".xlink").forEach(a=>{const id=a.getAttribute("data-id");
    if(byId[id]){a.onclick=()=>select(id);}
    else{a.classList.remove("xlink");a.classList.add("navlink");}});  // reserved/non-node target
}
function select(id){cy.nodes().removeClass("sel");const n=cy.getElementById(id);n.addClass("sel");if(byId[id])render(byId[id]);}
cy.on("tap","node",e=>select(e.target.id()));

document.getElementById("search").oninput=e=>{const q=e.target.value.toLowerCase();cy.nodes().forEach(n=>{const c=byId[n.id()];const hit=!q||c.title.toLowerCase().includes(q)||c.id.toLowerCase().includes(q)||(c.tags||[]).join(" ").toLowerCase().includes(q);n.toggleClass("faded",!hit);});};
tf.onchange=e=>{const t=e.target.value;cy.nodes().forEach(n=>n.toggleClass("faded",t&&byId[n.id()].type!==t));};
document.getElementById("layout").onchange=e=>cy.layout({name:e.target.value,animate:false,padding:30}).run();
</script></body></html>"""


def build_html(concepts, name):
    keys = ("id", "type", "title", "description", "resource", "tags", "body", "links",
            "sources", "trust", "status", "stale_after")
    data = json.dumps([{k: c[k] for k in keys} for c in concepts])
    return (HTML_TEMPLATE
            .replace("__NAME__", html.escape(name))
            .replace("__COUNT__", str(len(concepts)))
            .replace("__DATA__", data))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle", nargs="?", default=".")
    ap.add_argument("--name", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    bundle = os.path.abspath(args.bundle)
    name = args.name or os.path.basename(bundle.rstrip("/"))
    out = args.out or os.path.join(bundle, "viz.html")

    concepts, errors, reserved = collect(bundle)
    print(f"OKF bundle: {bundle}")
    print(f"  concepts: {len(concepts)}")
    types = {}
    for c in concepts:
        types[c["type"]] = types.get(c["type"], 0) + 1
    for t, n in sorted(types.items()):
        print(f"    - {t}: {n}")

    # broken-link report (soft — OKF tolerates these).
    # Reserved navigation files are valid targets even though they aren't nodes.
    ids = {c["id"] for c in concepts} | reserved
    broken = [(c["id"], l) for c in concepts for l in c["links"] if l not in ids]
    if broken:
        print(f"  broken links (allowed, FYI): {len(broken)}")
        for src, tgt in broken:
            print(f"    {src} -> {tgt}")

    if errors:
        print("\nCONFORMANCE ERRORS:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    print("  conformance: OK (OKF v0.2)")

    with open(out, "w", encoding="utf-8") as f:
        f.write(build_html(concepts, name))
    print(f"  wrote: {out}")


if __name__ == "__main__":
    main()
