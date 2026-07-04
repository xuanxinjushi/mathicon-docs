# System requirements

## Runtime

- OS: Linux x86_64
- Python: 3.9–3.13
- Recommended Python: 3.12

## Python dependencies

Core (installed with `pip install mathicon`):

- matplotlib >= 3.0.0
- numpy >= 1.18.0
- Pillow >= 9.0.0

Optional `[nn]` extra:

- torch >= 2.0.0
- aggdraw >= 13.14

## Recommended conda environment

Use conda env `usao` for local verification and documentation figure generation.

```bash
conda activate usao
python -c "import mathicon; print(mathicon.__version__)"
```

## Regenerating documentation assets

From the `mathicon-docs` repository:

```bash
conda activate usao
# Tutorial screenshots (matrix, vector, mindmap examples)
python tools/generate_docs_images.py

# Neural-network gallery thumbnail only
python tools/generate_gallery.py --icons nn_mlp --force

# Full icon gallery (~180 registry icons)
python tools/generate_gallery.py --force
```

Requires an editable or installed `mathicon` package on `PYTHONPATH`.

## Verification commands

```bash
python -c "import mathicon; print(mathicon.__version__)"
python -c "from mathicon import Matrix, draw_vec, render_mindmap, get_registered_icons; print(len(get_registered_icons()), 'icons')"
mathicon-preview-icons --list | head
```
