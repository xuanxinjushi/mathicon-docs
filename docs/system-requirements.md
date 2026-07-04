# System requirements

## Runtime

- OS: Linux x86_64
- Python: 3.9+
- Recommended Python: 3.12

## Python dependencies

- matplotlib >= 3.0.0
- numpy >= 1.18.0

These are installed automatically when installing `mathicon`.

## Recommended conda environment

Use conda env `usao` for local verification and documentation figure generation.

```bash
conda activate usao
python -c "import mathicon; print(mathicon.__version__)"
```

Docs illustration assets are generated with:

```bash
conda activate usao
python tools/generate_docs_images.py
```

## Verification commands

```bash
python -c "import mathicon; print(mathicon.__version__)"
python -c "from mathicon import Matrix, draw_vec, render_mindmap; print('OK')"
```
