# Mindmaps

Mindmap rendering is provided by:

```python
from mathicon import render_mindmap
```

## Entry point

```python
render_mindmap(caller_file, custom_icons=None)
```

- `caller_file`: usually `__file__`
- `custom_icons`: optional dict that maps icon names to drawing functions

The renderer reads `mindmap.json` from the same directory as `caller_file`.

## Minimal usage

```python
from mathicon import get_registered_icons, render_mindmap

registry_icons = {spec.id: spec.draw_func for spec in get_registered_icons().values()}
render_mindmap(__file__, custom_icons=registry_icons)
```

Or pass only the overrides you need; built-in resolution checks `custom_icons`, caller globals, then `icon_utils.draw_{id}_icon`.

Rendered example:

![Rendered mindmap example](images/mindmap-sample.png)

This image is generated from [tools/mindmap-sample.json](../tools/mindmap-sample.json).

## JSON structure

Typical top-level keys:

- `canvas`
- `nodes`
- `extra_links`

For the complete schema and field-by-field reference, see [Mindmap JSON format](mindmap-json-format.md).

Minimal example:

```json
{
  "canvas": {
    "figsize": [12.0, 7.5],
    "xlim": [0.0, 14.5],
    "ylim": [1.5, 10.5],
    "font_size": 13
  },
  "nodes": [
    {"id": "root", "label": "Mathicon", "pos": [7.0, 9.0], "color": "#2563eb", "is_branch": true},
    {"id": "la", "parent": "root", "label": "Linear Algebra", "pos": [4.0, 6.5], "icon": "svd"}
  ],
  "extra_links": []
}
```

## Local custom icons

Renderer lookup order for icon `name`:

1. `custom_icons["name"]`
2. `custom_icons["draw_name_icon"]`
3. local function `draw_name_icon` in caller script
4. built-in registry icon (exported as `draw_name_icon` from `mathicon`)

The authoritative list of built-in icon ids is in the [Icons reference](icons-reference.md) gallery, or via `get_registered_icons()` / `mathicon-preview-icons --list`. See [Icon registry](icon-registry.md) for registration and categories.
