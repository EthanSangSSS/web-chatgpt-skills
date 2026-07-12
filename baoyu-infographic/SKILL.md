---
name: baoyu-infographic
version: "0.2.0"
status: stable
description: Convert verified information into clear infographic specifications with source, denominator, uncertainty, visual hierarchy, and misleading-chart checks.
triggers:
  - infographic
  - visual summary
  - comparison graphic
  - timeline
  - 信息图
  - 可视化
do_not_use_for:
  - decorative chart
  - unsourced statistics
  - misleading scale choices
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Infographic Designer

## Purpose

Create an infographic plan that answers one question with verified information. The goal is fast comprehension without misleading scale, source, or certainty.

## Required input

Collect or infer:

- Single question the graphic answers.
- Intended audience and surface: web, article, slide, PDF, social, print.
- Data or claims to visualize.
- Sources, dates, units, denominators, uncertainty, and comparison basis.
- Required output: wireframe, data table, prompt, or production spec.

If source/data provenance is missing, ask for it or mark the graphic as conceptual and avoid numeric claims.

## Web ChatGPT execution boundary

This skill may design a wireframe/specification from provided evidence, uploaded files, GitHub connector data, and web search. It must not claim to render, inspect, or export final graphics unless a tool actually does so.

## Data audit

For each data point or claim, record:

- source and date;
- unit and denominator;
- geography/timeframe;
- uncertainty or margin of error if known;
- whether comparisons are apples-to-apples;
- evidence strength.

Do not use unsourced statistics as factual infographic content.

## Layout selection

Choose based on the question:

- comparison;
- timeline;
- process;
- hierarchy;
- map;
- scorecard;
- dashboard;
- decision tree.

Avoid decorative charts and 3D effects.

## Misleading-chart checks

Watch for:

- truncated axes without disclosure;
- area/volume encoding exaggeration;
- inconsistent denominators;
- missing baselines;
- cherry-picked time windows;
- unclear uncertainty;
- ranking volatility;
- overloaded legends;
- text too small for target surface.

## Output contract

Return:

- **Question answered**.
- **Data/claim audit table**.
- **Recommended layout** and why.
- **Wireframe**.
- **Visual hierarchy**: title, one takeaway, primary data, supporting detail, source note.
- **Style guide**.
- **Production prompt/spec**.
- **Alt text**.
- **Risks and caveats**.

## Validation gate

Before finalizing, verify:

- Every number/claim has a source or is labeled conceptual.
- Units and denominators are visible.
- Comparisons are valid.
- Uncertainty is stated when interpretation changes.
- The graphic answers one question.
- Accessibility is considered.

## Local-agent handoff trigger

Hand off when final assets must be generated/exported, data processed by scripts, layout tested, or files committed. Include data source, file scope, output dimensions, forbidden distortions, validation checks, stop conditions, and final output format.
