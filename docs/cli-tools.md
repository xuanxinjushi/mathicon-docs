# CLI tools

Mathicon installs two console scripts.

## `mathicon-preview-icons`

Batch-render icon previews from the central registry.

```bash
# List all registered icon ids
mathicon-preview-icons --list

# Render selected icons as PNG
mathicon-preview-icons --icons qr,svd,rotation --format png

# Multi-format export
mathicon-preview-icons --icons gradient,hessian --format png,svg,pdf,webp

# Animated GIF/WebP (icons with animation profiles only)
mathicon-preview-icons --icons rotation,score_field,brownian_motion --animate --format gif
```

Common options:

| Flag | Purpose |
|------|---------|
| `--icons` | Comma-separated icon ids (default: all) |
| `--format` | `png`, `svg`, `pdf`, `webp`, `jpg`, `gif` |
| `--animate` | Use `FuncAnimation` for loopable output |
| `--output-dir` | Destination directory |
| `--dpi`, `--size` | Render resolution and figure size |

PNG output uses transparent trimming when applicable (`mathicon.common.img_utils`).

## `mathicon-gui`

Interactive Tkinter browser for exploring icons:

- Search and filter by category
- Static and animated preview
- Dual-size thumbnail view
- Export to PNG/GIF
- Book chapter excerpts for icons mapped in `icon_metadata.json`

```bash
mathicon-gui
```

## Regenerating the docs gallery

From the `mathicon-docs` repository:

```bash
conda activate usao
python tools/generate_gallery.py --force
```

This refreshes `docs/icons-reference.md` and `docs/images/icons/` from the installed `mathicon` package.
