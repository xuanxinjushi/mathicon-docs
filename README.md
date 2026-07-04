# Mathicon documentation

Public documentation for **Mathicon** — a Python plotting toolkit for mathematics and machine learning figures.

- Documentation site: https://mathicon.readthedocs.io/
- Package: `pip install mathicon`

This repository contains **Markdown docs only**. Runtime source lives in the `mathicon` package repository.

## Edit workflow

1. Change behavior or copy in `shared/mathicon` (source of truth).
2. Update pages under `docs/` in this repo when the public API or workflows change.
3. Regenerate assets when icons change:

```bash
conda activate usao
cd shared/mathicon-docs
python tools/generate_gallery.py --force
python tools/generate_docs_images.py
```

Key shared modules in `mathicon`:

| Module | Docs page |
|--------|-----------|
| `mathicon.common` (colors, matrix, vector, figure utils) | colors.md, matrix-visualization.md, … |
| `mathicon.common.registry` | icon-registry.md |
| `mindmap.py`, `poster.py` | mindmaps.md, posters.md |
| `preview_icons.py`, `icon_preview_gui.py` | cli-tools.md |

If pages and API differ, prefer the installed `mathicon` package and `get_registered_icons()` as source of truth.
