---
name: baoyu-article-illustrator
version: "0.2.0"
status: beta
description: Design coherent article illustration systems, placement maps, alt text, and production prompts with IP, accessibility, and factual boundaries.
triggers:
  - article illustration
  - visual plan
  - image prompt
  - 配图
  - 文章插图
do_not_use_for:
  - copying living artist style
  - generating copyrighted character lookalikes
  - factual charting without data audit
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Article Illustrator

## Purpose

Create an illustration plan that clarifies, paces, or emotionally anchors an article. Avoid decorative image spam.

## Required input

Collect or infer:

- Article text or outline.
- Thesis, emotional arc, audience, and publication surface.
- Desired format: hero image, section illustrations, social thumbnail, cover, or prompt pack.
- Visual constraints: brand, accessibility, platform, dimensions, tone, IP restrictions.
- Whether the current ChatGPT surface should generate images or only produce prompts/specs.

If the article is absent, request it or work from a clear summary and label assumptions.

## Web ChatGPT execution boundary

This skill may analyze provided article text, uploaded files, GitHub connector content, and web evidence. It must not claim to generate, inspect, or edit images unless an image tool actually does so. If image generation is unavailable or not requested, return production prompts/specifications only.

## IP and safety boundaries

- Do not copy living artists' styles or ask for deceptive imitation.
- Do not generate copyrighted character lookalikes unless the user has rights and the request is allowed by the current policy.
- Avoid embedding critical text inside generated images; use captions/layout text outside the image when possible.
- For public figures, avoid misleading endorsement or fake documentary framing.
- Use alt text and accessible contrast guidance.

## Workflow

1. Identify thesis, emotional arc, reader, and article structure.
2. Select 3-6 illustration moments that each earn their place.
3. Define one visual system:
   - style family;
   - palette direction;
   - composition logic;
   - recurring motifs;
   - accessibility approach.
4. Build an illustration map with placement, purpose, subject, composition, caption, and alt text.
5. Produce one production-ready prompt per image preserving the shared visual system.

## Output contract

Return:

- **Visual direction**.
- **Illustration map table**: placement, purpose, subject, composition, caption, alt text.
- **Shared visual bible**: palette, motifs, composition, exclusions.
- **Production prompts**.
- **Accessibility notes**.
- **Open risks**: factual, IP, style, platform fit.

## Validation gate

Before finalizing, verify:

- Each illustration supports a specific article function.
- Visual system is consistent across prompts.
- Critical text is not trapped inside images.
- Alt text exists.
- No living-artist imitation or copyrighted character copying.

## Local-agent handoff trigger

Hand off when assets must be generated, edited, exported, inserted into a repository, or tested across layouts. The handoff must include article source, asset count, dimensions, file scope, IP constraints, validation checks, stop conditions, and final output format.
