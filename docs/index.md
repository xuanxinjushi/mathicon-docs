# Mathicon

**Mathicon** is a Python toolkit for creating publication-ready mathematics and machine learning figures with a consistent visual language.

It is designed for long-form projects (books, lecture notes, technical reports) where figure style consistency matters across dozens or hundreds of scripts.

## What Mathicon provides

- Shared color tokens for geometric and algebraic diagrams
- Matrix drawing primitives with row/column/diagonal highlighting
- Vector helpers for arrows and affine grids
- Figure output helpers aligned with chapter-script workflows
- JSON-driven mindmap and poster rendering with built-in and local custom icons
- Central icon registry (~180 icons) for linear algebra, optimization, probability, stochastics, and legend matrix types
- CLI tools: `mathicon-preview-icons`, `mathicon-icon-gui`
- Multi-format icon export (PNG, SVG, PDF, WebP, GIF)

## Quick install

```bash
pip install mathicon
```

Sanity check:

```bash
python -c "from mathicon import plane_color; print(plane_color)"
```

## Visual output examples

### Matrix highlighting

![Matrix highlight example](images/matrix-highlight.png)

### Vector and affine grid

![Vector grid example](images/vector-grid.png)

### Mindmap rendering

![Mindmap example](images/mindmap-sample.png)

### Neural network MLP icon

![Neural network MLP icon](images/nn-mlp.png)

## Documentation map

| Section | Contents |
|---|---|
| [What is Mathicon?](what-is-mathicon.md) | Scope, goals, and design principles |
| [Installation](installation.md) | PyPI and editable install |
| [Quick start](quickstart.md) | Minimal working examples |
| [Python API overview](python-api.md) | Public API categories |
| [Colors](colors.md) | Shared color constants |
| [Matrix visualization](matrix-visualization.md) | `Matrix` class and helper functions |
| [Vector visualization](vector-visualization.md) | Grid and arrow drawing helpers |
| [Figure utilities](figure-utilities.md) | Save and styling helpers |
| [Mindmaps](mindmaps.md) | `mindmap.json` schema and rendering |
| [Posters](posters.md) | `poster.json` educational poster layout |
| [Icon registry](icon-registry.md) | Central registry, categories, custom icons |
| [Icons reference](icons-reference.md) | Built-in icon gallery for mindmaps |
| [CLI tools](cli-tools.md) | `mathicon-preview-icons`, `mathicon-icon-gui` |
| [System requirements](system-requirements.md) | Platform, Python, and dependencies |
