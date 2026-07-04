# What is Mathicon?

Mathicon is a focused plotting library that sits between raw matplotlib code and full charting frameworks.

Its purpose is to make chapter figures look coherent across an entire technical manuscript.

## Core idea

In math-heavy projects, each figure script is often written at a different time with slightly different style choices. Mathicon reduces style drift by centralizing:

- Colors and themes (`Theme`, shared palette tokens)
- Matrix and vector drawing conventions (`mathicon.common`)
- Mindmap and poster iconography via a central registry
- Figure save behavior and transparent PNG export

## Typical users

- Authors of mathematics and machine learning books
- Educators producing polished lecture diagrams
- Researchers creating consistent figure sets for papers or reports

## Package layout

| Area | Module | Role |
|------|--------|------|
| Core helpers | `mathicon.common` | Colors, matrix/vector vis, figure utils, registry |
| Domain icons | `linear_algebra/`, `stochastics/`, `neural_network/`, … | `drawers.py` per curriculum area |
| High-level renderers | `mindmap.py`, `poster.py` | JSON-driven figures |
| Tooling | `preview_icons.py`, `icon_preview_gui.py` | CLI and GUI exploration |

## Scope

Mathicon is not a general dashboarding or plotting framework. It is a lightweight utility layer on top of matplotlib and numpy for script-based figure pipelines.

For the full public API, see [Python API overview](python-api.md).
