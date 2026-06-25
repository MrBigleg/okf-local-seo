---
type: Reference
title: Google — Maps grounding for AI (full, Lite, place summaries)
description: Google's developer documentation for grounding AI models with Google Maps data, including Grounding Lite and Places API AI summaries.
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps
publisher: Google (Google Cloud / Google Maps Platform)
published: living document
accessed: 2026-06-25
confidence: high
scope: Developer-product capabilities for Maps grounding. Does NOT establish that every consumer Maps answer uses these API paths.
tags: [reference, google-maps, ai, grounding, developer]
timestamp: 2026-06-25T00:00:00Z
---

The Google developer documentation underpinning the [Grounding with Google Maps](/agentic/grounding-google-maps.md) concept doc. Three related products:

# Full Maps grounding

Enabled as a grounding tool in the Gemini Enterprise Agent Platform / Vertex AI Studio. Documented to draw on **more than 250 million places**. Responses carry Maps sources in REST field `groundingMetadata.groundingChunks` (SDKs may use snake_case). Source attribution is a display requirement. The current documentation contains no "widget context token" or "Contextual View"; those earlier-draft claims are not retained.

# Maps Grounding Lite

A Google Maps Platform service with Model Context Protocol (MCP) support, exposing tools for place search, current/forecast weather, and driving/walking route distance and duration. It does **not** provide turn-by-turn directions, real-time traffic or navigation.

# Places API (New) AI summaries

`generativeSummary` returns brief (~100-character) place overviews in Place Details, Text Search and Nearby Search, requiring a "Summarized with Gemini" disclosure. As of 25 June 2026, documented for supported place types in English in India and the United States; not guaranteed for every place.

# Citations

[1] [Google Cloud — Grounding with Google Maps](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps)

[2] [Google Maps Platform — Maps Grounding Lite](https://developers.google.com/maps/ai/grounding-lite)

[3] [Google Maps Platform — AI-powered place summaries](https://developers.google.com/maps/documentation/places/web-service/place-summaries)
