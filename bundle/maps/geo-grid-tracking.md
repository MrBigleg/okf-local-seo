---
type: Maps Analysis
title: Geo-Grid Rank Tracking
description: Simulate Google Maps searches from multiple GPS coordinates to show ranking variation and compute Share of Local Voice.
tags: [maps, geo-grid, rank-tracking, solv]
tier: 1
timestamp: 2026-06-24T00:00:00Z
---

Geo-grid tracking simulates Maps searches from many GPS coordinates to reveal how rank varies across a geographic area. Requires DataForSEO ([Tier 1+](/maps/capability-tiers.md)).

# Workflow

1. Geocode the business address to a centre lat/lng.
2. Generate grid points (default 7×7, 5km radius) using a Haversine offset.
3. **Display a cost estimate and ask for confirmation before proceeding.**
4. Fire DataForSEO Maps SERP calls with `location_coordinate` per grid point.
5. Find the target business rank at each point.
6. Compute SoLV: `(top_3_count / total_points) * 100`.
7. Render an ASCII heatmap in the output.

# Cost warning (required)

Before every scan, display the keyword, location, grid size, keyword count, and estimated cost, and confirm before consuming DataForSEO credits.

# Citations

[1] [DataForSEO](/references/dataforseo.md)
