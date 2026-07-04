# Posters

Mathicon can render **educational posters** from JSON, similar to mindmaps.

## Entry point

```python
from mathicon import render_poster

if __name__ == "__main__":
    render_poster(__file__)
```

The renderer reads `poster.json` from the same directory as `caller_file` and writes a PNG beside the script.

## JSON-driven layout

`poster.json` describes sections, text blocks, optional images, and decorative icons. Poster-specific drawers (`draw_lightbulb_icon`, `draw_star_icon`, `draw_clipboard_icon`, etc.) are available via `POSTER_ICON_DRAWERS`.

Theme colors (background, header, accent, box fill, text) can be overridden in the JSON `theme` object.

## Relation to mindmaps

| Feature | Mindmap | Poster |
|---------|---------|--------|
| Config file | `mindmap.json` | `poster.json` |
| Renderer | `render_mindmap` | `render_poster` |
| Primary use | Chapter concept trees | One-page summaries, cheat sheets |
| Icons | Registry mindmap icons | Registry + poster decorative icons |

For mindmap schema details, see [Mindmap JSON format](mindmap-json-format.md).
