---
type: Reference
title: Google — Maps grounding for AI (full, Lite, place summaries)
description: Google's developer documentation for grounding AI models with Google Maps data, including Grounding Lite and Places API AI summaries.
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps
publisher: Google (Google Cloud / Google Maps Platform)
published: living document
accessed: 2026-08-01
confidence: high
scope: Developer-product capabilities for Maps grounding. Does NOT establish that every consumer Maps answer uses these API paths.
tags: [reference, google-maps, ai, grounding, developer]
generated: { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
verified:  { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
status: stable
stale_after: 2026-11-01
sources:
  - id: google-cloud-grounding-with-google-maps
    resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps
    title: Google Cloud — Grounding with Google Maps
  - id: google-maps-platform-maps-grounding-lite
    resource: https://developers.google.com/maps/ai/grounding-lite
    title: Google Maps Platform — Maps Grounding Lite
  - id: google-maps-platform-ai-powered-place
    resource: https://developers.google.com/maps/documentation/places/web-service/place-summaries
    title: Google Maps Platform — AI-powered place summaries
---

The Google developer documentation underpinning the [Grounding with Google Maps](/agentic/grounding-google-maps.md) concept doc. Three related products:

# Full Maps grounding

Enabled as a grounding tool in the Gemini Enterprise Agent Platform / Vertex AI Studio. Documented to draw on **more than 250 million places**. In REST responses, Maps sources appear under `groundingMetadata.groundingChunks[].maps`; documented fields include `uri`, `title`, `placeId` and `placeAnswerSources.reviewSnippets` (SDKs may use snake_case). Source attribution is a display requirement. The current documentation contains no "widget context token" or "Contextual View"; those earlier-draft claims are not retained.

The documentation now also describes **Find Directions**, which returns structured travel metadata, and **Search Along Route**, which finds places convenient to a planned journey and returns metadata for both the route and the places found.

# Maps Grounding Lite

A Google Maps Platform service with Model Context Protocol (MCP) support, exposing tools for place search, current/forecast weather, and driving/walking route distance and duration. It does **not** provide turn-by-turn directions, real-time traffic or navigation.

Its separate experimental Resolution API provides `ResolveNames` and `ResolveMapsUrls` endpoints for resolving batches of unstructured names, addresses and Maps URLs to stable Place IDs. Google labels both endpoints pre-GA.

# Places API (New) AI summaries

`generativeSummary` returns brief (~100-character) place overviews in Place Details, Text Search and Nearby Search, requiring a "Summarized with Gemini" disclosure. As of 1 August 2026, documented for supported place types in English in India and the United States; not guaranteed for every place.
