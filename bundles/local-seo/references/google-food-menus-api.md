---
type: Reference
title: Google Business Profile APIs — Update Food Menus
description: The structured Food Menus data model and the API endpoints for reading and writing it.
resource: https://developers.google.com/my-business/content/update-food-menus
publisher: Google (Business Profile APIs)
published: living document
accessed: 2026-08-01
confidence: high
scope: The menu data structure (sections and items, required Name and Price, optional description/nutrition/allergens/cuisines/photo associations) and the getFoodMenus / updateFoodMenus endpoints. Does not establish any AI or vision-based extraction of menu items from photographs — the documentation covers only manual API updates and photo association with already-defined items.
tags: [reference, gbp, api, agentic]
generated: { by: human:craigburton, at: 2026-07-27T00:00:00Z }
verified:  { by: openai/gpt-5.6-sol, at: 2026-08-01T00:00:00Z }
status: stable
stale_after: 2026-11-01
sources:
  - id: google-business-profile-apis-update-food-menus
    resource: https://developers.google.com/my-business/content/update-food-menus
    title: Google Business Profile APIs — Update Food Menus
---

Google's Business Profile APIs reference for the Food Menus content type. Used as the primary source for the structured (non-AI) route to publishing menu items and prices in [Human-in-the-Loop GBP Management](/agentic/hitl-gbp-management.md) and [Agentic Commerce Readiness](/agentic/agentic-commerce-readiness.md).

# What the source establishes

* Menus are structured as menus → sections → items. **Name** and **Price** are required per item; description, nutrition facts, allergens, dietary restrictions, preparation method, portion size, cuisine, and `mediaKeys` photo associations are optional.
* Menu items are updated through the API (`updateFoodMenus`) rather than inferred from images — there is no vision-based extraction of menu content from photos documented anywhere on this page.
