---
type: Concept
title: Grounding with Google Maps
description: Google's developer services for adding Google Maps place, route, weather and review context to AI applications.
tags: [google-maps, ai, grounding, developer]
generated: { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
verified:  { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
status: stable
stale_after: 2026-09-01
sources:
  - id: google-cloud-grounding-with-google-maps
    resource: /references/google-maps-grounding.md
    title: Google Cloud — Grounding with Google Maps
  - id: google-maps-platform-maps-grounding-lite
    resource: /references/google-maps-grounding.md
    title: Google Maps Platform — Maps Grounding Lite
  - id: google-maps-platform-ai-powered-place
    resource: /references/google-maps-grounding.md
    title: Google Maps Platform — AI-powered place summaries
---

Grounding with Google Maps connects Gemini models to Google Maps geospatial data. Google states that the service can use information on **more than 250 million places** and can be combined with Google Search grounding or private data sources.

# Full Maps grounding

In the Gemini Enterprise Agent Platform and Vertex AI Studio workflow, a developer enables Google Maps as a grounding tool. In REST responses, Google Maps sources appear under `groundingMetadata.groundingChunks[].maps`; documented fields include `uri`, `title`, `placeId` and `placeAnswerSources.reviewSnippets`. Client libraries may expose equivalent snake-case names.

Maps source chunks can contain:

* a Google Maps URI and title;
* a place ID;
* place-answer sources; and
* review snippets and review identifiers where available.

Source attribution is part of the product's display requirements. The current documentation does not describe the earlier draft's widget context token or a product named “Contextual View”, so those claims are not retained.

The current full-grounding documentation also describes route-aware capabilities. **Find Directions** returns travel information backed by structured metadata, while **Search Along Route** finds places that are convenient to a planned journey and returns metadata for both the route and the places found.

# Maps Grounding Lite

Maps Grounding Lite is a Google Maps Platform service with Model Context Protocol support. Its MCP server exposes tools to:

* search for places;
* look up current and forecast weather; and
* compute driving or walking route distance and duration.

It does not provide turn-by-turn directions, real-time traffic or navigation.

A separate experimental Resolution API can resolve batches of free-form place names, addresses and Google Maps URLs to stable Place IDs. Google labels its `ResolveNames` and `ResolveMapsUrls` endpoints pre-GA.

# Places API AI summaries

Places API (New) can return AI-powered place summaries through `generativeSummary` in Place Details, Text Search and Nearby Search responses. Google describes these as brief, 100-character overviews and requires a “Summarized with Gemini” disclosure. On 1 August 2026, place summaries were documented for supported place types in English in India and the United States and were not guaranteed for every place.

# Why it matters

These services let developers build location-aware applications with identifiable source material instead of relying only on a model's internal knowledge. They are developer products, not evidence that every consumer Maps answer uses the same API path. See [Ask Maps](/agentic/ask-maps.md).

Source provenance for these products lives in the reference page [Google — Maps grounding for AI](/references/google-maps-grounding.md).
