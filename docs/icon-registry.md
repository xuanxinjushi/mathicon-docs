# Icon registry

Mathicon maintains a **central icon registry** (`mathicon.common.registry`). Every built-in mindmap icon is registered with metadata: id, display name, category, draw callable, and whether it supports animation.

## Why a registry?

Previously, icon discovery relied on scanning `icon_utils` for `draw_*_icon` functions. The registry:

- Groups icons by domain (`linear_algebra`, `matrix`, `calculus`, `optimization`, `probability`, `stochastics`, `machine_learning`, `distributed_systems`, `neural_network`, `diagram`, `quant`)
- Marks animatable icons (functions with a `phase` parameter or `AnimatableIcon.draw_frame`)
- Powers `mathicon-preview-icons`, the icon GUI, and auto-exports in `mathicon.__init__`
- Connects icons to book chapters via `icon_metadata.json` and `build_book_context`

## Querying icons

```python
from mathicon import get_registered_icons, get_icon_spec, get_icons_by_category

icons = get_registered_icons()
print(len(icons), "registered icons")

spec = get_icon_spec("svd")
print(spec.name, spec.category)

la_icons = get_icons_by_category("linear_algebra")
```

## Registering a custom icon

```python
from mathicon import register_icon, Theme

theme = Theme()

@register_icon("my_icon", "My Custom Icon", "custom", animatable=False)
def draw_my_icon_icon(ax, theme=theme, **kwargs):
    ax.text(0.5, 0.5, "★", ha="center", va="center", fontsize=24)
```

Use the registered `id` as the mindmap `icon` field value.

## Icon lookup in mindmaps

When `render_mindmap` resolves `icon: "qr"`, it checks in order:

1. `custom_icons` dict passed to `render_mindmap`
2. Local `draw_qr_icon` in the caller script
3. Built-in registry / `icon_utils` drawers

The [Icons reference](icons-reference.md) gallery lists all registry ids with previews.

## Matrix icons

Matrix shape icons (`square_matrix`, `diagonal_matrix`, `lower_triangular_matrix`, …) use the book legend color scheme from `chapterx/img/legend.py`. Register with `category="matrix"`; see the **Matrix Icons** section in [icons-reference.md](icons-reference.md).

## Neural network icons

One registered icon, `nn_mlp`, renders a minimal MLP (`2→3→2`, visualtorch graph style).

Install optional dependencies: `pip install mathicon[nn]` (torch + aggdraw).

```bash
mathicon-preview-icons --icons nn_mlp --format png
python tools/generate_gallery.py --icons nn_mlp --force
```

High-resolution doc showcase: `docs/images/nn-mlp.png` (from `tools/generate_docs_images.py`).

## Animated icons

Icons with animation profiles accept a `phase` keyword (0.0–1.0) for static frames, or export as GIF/WebP via `mathicon-preview-icons --animate`. Whitelisted ids are listed in `icon_metadata.json` under `gif_icons`.
