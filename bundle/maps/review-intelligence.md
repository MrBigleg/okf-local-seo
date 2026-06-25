---
type: Maps Analysis
title: Review Intelligence
description: Cross-platform review velocity, sentiment, rating distribution, and fake-review detection.
tags: [maps, reviews, velocity, sentiment]
tier: 1
timestamp: 2026-06-24T00:00:00Z
---

Cross-platform review analysis across Google, Tripadvisor, and Trustpilot. Extends the on-page view in [reviews & reputation](/local-seo/reviews-reputation.md) with platform data.

# Workflow

1. Fetch Google reviews via the DataForSEO Reviews API (newest first).
2. Calculate review velocity: reviews per month over the last 6 months.
3. Check the **18-day rule** (Sterling Sky): any 3-week gap = ranking risk.
4. Analyse rating distribution: healthy = bell curve skewed to 5-star.
5. Calculate owner response rate: responses / total reviews.
6. Fetch Tripadvisor and Trustpilot reviews if available.
7. Build a cross-platform comparison table.

# Fake-review detection

Flag reviews matching 2+ of: uniform timing; reviewer accounts with limited history; geographic inconsistencies; exclusively 5-star velocity spikes; near-identical text; sudden volume spikes without corresponding marketing activity.

# Citations

[1] [Sterling Sky](/references/sterling-sky.md)
[2] [DataForSEO](/references/dataforseo.md)
