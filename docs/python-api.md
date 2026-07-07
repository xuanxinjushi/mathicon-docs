# Python API overview

Main package import:

```python
import mathicon
```

Most users import specific symbols:

```python
from mathicon import Matrix, draw_vec, save_figure, render_mindmap
```

Implementation modules live under `mathicon.common` (colors, matrix/vector helpers, registry). Top-level shims such as `matrix_vis.py` re-export the same API for backward compatibility.

## API groups

## 1. Color constants

- `plane_color`
- `point_x_color`
- `foot_x_bar_color`
- `distance_line_color`
- `normal_vector_color`
- `right_angle_indicator_color`

See [Colors](colors.md).

## 2. Matrix visualization

Class:

- `Matrix`

Functions:

- `draw_dashed_row`, `draw_dashed_col`
- `draw_column_indices`, `draw_row_indices`
- `draw_piercing_row`, `draw_piercing_col`
- `draw_brace`, `draw_curved_label`
- `color_row_col`, `finalize`

Source: `mathicon.common.matrix_vis`

See [Matrix visualization](matrix-visualization.md).

## 3. Vector visualization

- `draw_affine_grid`
- `draw_vec`
- `arrow`

Source: `mathicon.common.vector_vis`

See [Vector visualization](vector-visualization.md).

## 4. Figure utilities

- `configure_math_fonts`
- `customize_3d_grid`
- `customize_2d_grid`
- `save_figure_to_script_dir`
- `save_figure`
- `save_mindmap_thumbnail`

Source: `mathicon.common.figure_utils`

See [Figure utilities](figure-utilities.md).

## 5. Mindmaps and posters

- `render_mindmap(caller_file, custom_icons=None)` — reads `mindmap.json` beside the caller script
- `render_poster(caller_file)` — reads `poster.json` beside the caller script

See [Mindmaps](mindmaps.md), [Posters](posters.md), and [Mindmap JSON format](mindmap-json-format.md).

## 6. Icon registry and theme

Mathicon registers every built-in mindmap icon in a central registry. Registry icons are also exported at package top level as `draw_<id>_icon` callables.

- `Theme` — shared color tokens for icon drawing
- `register_icon` — decorator to register custom icons
- `get_registered_icons()` — all `MathIconSpec` entries keyed by icon id
- `get_icon_spec(id)` — lookup one icon
- `get_icons_by_category(category)` — filter by domain (`linear_algebra`, `stochastics`, `legend`, …)
- `MathIcon`, `AnimatableIcon` — base classes for class-based icons
- `build_book_context`, `BookContext` — map icons to textbook chapter excerpts (used by the GUI)

See [Icon registry](icon-registry.md) and [Icons reference](icons-reference.md).

## 7. Poster decorative icons

- `POSTER_ICON_DRAWERS`
- `draw_lightbulb_icon`, `draw_star_icon`, `draw_clipboard_icon`, `draw_checkmark_icon`, `draw_shield_icon`, `draw_gauge_icon`, `draw_magnifier_icon`

## 8. Optional neural-network icons

With the optional extra `pip install mathicon[nn]`:

- `nn_mlp` — minimal MLP graph icon (2→3→2, visualtorch graph style)

Requires PyTorch and `aggdraw`.

## 9. Command-line tools

Installed console scripts:

```bash
mathicon-preview-icons --list
mathicon-preview-icons --icons qr,svd,rotation --format png,svg,gif
mathicon-gui
```

`mathicon-preview-icons` discovers icons from the registry and can export PNG, SVG, PDF, WebP, JPG, and loopable GIF/WebP for animated icons.

See [CLI tools](cli-tools.md).

## Dynamic icon exports

`from mathicon import *` (or explicit imports) can pull in every registered `draw_*_icon` function. Use `get_registered_icons()` or `mathicon-preview-icons --list` for the authoritative name list.
