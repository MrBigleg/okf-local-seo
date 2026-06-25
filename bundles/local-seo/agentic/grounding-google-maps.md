---
type: Reference
title: Grounding with Google Maps
description: Google's developer services for adding Google Maps place, route, weather and review context to AI applications.
tags: [google-maps, ai, grounding, developer]
timestamp: 2026-06-25T00:00:00Z
---

Grounding with Google Maps connects Gemini models to Google Maps geospatial data. Google states that the service can use information on **more than 250 million places** and can be combined with Google Search grounding or private data sources.

# Full Maps grounding

In the Gemini Enterprise Agent Platform and Vertex AI Studio workflow, a developer enables Google Maps as a grounding tool. Responses can include Google Maps sources in REST field `groundingMetadata.groundingChunks`; client libraries may expose equivalent snake-case names such as `grounding_metadata` and `grounding_chunks`.

Maps source chunks can contain:

* a Google Maps URI and title;
* a place ID;
* place-answer sources; and
* review snippets and review identifiers where available.

Source attribution is part of the product's display requirements. The current documentation does not describe the earlier draft's widget context token or a product named “Contextual View”, so those claims are not retained.

# Maps Grounding Lite

Maps Grounding Lite is a Google Maps Platform service with Model Context Protocol support. Its MCP server exposes tools to:

* search for places;
* look up current and forecast weather; and
* compute driving or walking route distance and duration.

It does not provide turn-by-turn directions, real-time traffic or navigation.

# Places API AI summaries

Places API (New) can return AI-powered place summaries through `generativeSummary` in Place Details, Text Search and Nearby Search responses. Google describes these as brief, 100-character overviews and requires a “Summarized with Gemini” disclosure. On 25 June 2026, place summaries were documented for supported place types in English in India and the United States and were not guaranteed for every place.

# Why it matters

These services let developers build location-aware applications with identifiable source material instead of relying only on a model's internal knowledge. They are developer products, not evidence that every consumer Maps answer uses the same API path. See [Ask Maps](/agentic/ask-maps.md).

# Citations

[1] [Google Cloud — Grounding with Google Maps](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps)

[2] [Google Maps Platform — Maps Grounding Lite](https://developers.google.com/maps/ai/grounding-lite)

[3] [Google Maps Platform — AI-powered place summaries](https://developers.google.com/maps/documentation/places/web-service/place-summaries)
