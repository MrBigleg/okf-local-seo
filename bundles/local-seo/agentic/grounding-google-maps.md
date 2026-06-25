---
type: Concept
title: Grounding with Google Maps
description: Google's developer method for connecting Gemini output to Maps place, route, and review context with source metadata.
tags: [google-maps, ai, grounding, developer]
timestamp: 2026-06-25T00:00:00Z
---

> **Draft — pending fact-check & citation URLs.**

Grounding with Google Maps is Google's developer-facing method for tying Gemini output to Google Maps place, route, and review context, returning structured source metadata. The primary surface is in Vertex AI, where grounded responses can draw on Maps geospatial data across a large global place index.

# How it works

* In Vertex AI, a `googleMaps` grounding tool sits alongside Google Search grounding and private-data grounding in the same API family.
* Grounded responses return source metadata (place and review sources, URIs, place IDs, review IDs) so answers are auditable.
* With widget support enabled, the API can return a context token that powers an embeddable contextual map view.

# Where it sits

* **Grounding with Google Maps** — the full grounded-response workflow in Vertex AI.
* **Grounding Lite** — a lighter, tool-call surface for place, weather, and route lookups.
* **Places API (New) AI summaries** — Gemini-generated place/review synthesis directly in standard Maps API responses.

# Why it matters

It turns Maps data into auditable model context — relevant to local recommendation agents, travel assistants, and any app needing location-aware answers with source visibility. It's the developer plumbing beneath consumer features like [Ask Maps](/agentic/ask-maps.md).

# Citations

[1] Google Cloud — Grounding with Google Maps, Vertex AI (confirm URL).
[2] Vertex AI grounding API reference (confirm URL).
