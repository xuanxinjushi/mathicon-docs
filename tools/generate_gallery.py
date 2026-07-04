import sys
import json
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

TOOLS_DIR = Path(__file__).resolve().parent
DOCS_ROOT = TOOLS_DIR.parent
MATHICON_ROOT = DOCS_ROOT.parent / "mathicon"
MATHICON_SRC = MATHICON_ROOT / "src"

sys.path.insert(0, str(MATHICON_SRC))
from mathicon.preview_icons import (
    discover_icon_drawers,
    render_icon_preview,
    animate_icon_preview,
    supported_animated_icons,
)


DEFAULT_GIF_WHITELIST = {
    "rotation",
    "scaling",
    "shear",
    "score_field",
}

DEFAULT_RENDER = {
    "dpi": 80,
    "figure_size": (1.8, 1.8),
    "size_scale": 1.0,
}

# 4.0 in × 150 dpi → 600×600 px (matches mathicon-preview-icons --animate defaults).
DEFAULT_GIF_RENDER = {
    "dpi": 150,
    "figure_size": (4.0, 4.0),
    "frames": 30,
    "fps": 15,
}


def _render_kwargs_for_icon(name: str) -> dict:
    return dict(DEFAULT_RENDER)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Mathicon gallery with PNG for all icons and GIF for a selected whitelist."
    )
    parser.add_argument(
        "--gif-icons",
        nargs="*",
        default=None,
        help="Icon keys that should also generate loopable GIFs.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-render existing PNG/GIF files instead of skipping them.",
    )
    parser.add_argument(
        "--icons",
        nargs="*",
        default=None,
        help="Only render these icon ids (default: all).",
    )
    return parser.parse_args()


def _desc_for_icon(name: str, meta: dict, metadata_payload: dict) -> str:
    desc = meta.get("description")
    if desc:
        return desc
    title = meta.get("title", name.replace("_", " ").title())
    template = metadata_payload.get("description_template")
    if template:
        return template.format(title=title, title_lower=title.lower())
    return "No description provided."


def build_gallery(gif_icons=None, force=False, icon_filter=None):
    docs_root = DOCS_ROOT
    images_dir = docs_root / "docs" / "images" / "icons"
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Load metadata
    metadata_path = MATHICON_ROOT / "icon_metadata.json"
    if metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata_payload = json.load(f)
            metadata = metadata_payload.get("icons", {})
    else:
        metadata_payload = {}
        metadata = {}

    metadata_gif_icons = {
        str(icon).strip() for icon in metadata_payload.get("gif_icons", []) if str(icon).strip()
    }
        
    all_drawers = discover_icon_drawers()
    if icon_filter:
        missing = sorted(set(icon_filter) - set(all_drawers))
        if missing:
            print(f"Warning: unknown icon ids (skipped): {', '.join(missing)}")
        render_drawers = {k: v for k, v in all_drawers.items() if k in icon_filter}
    else:
        render_drawers = all_drawers
    print(f"Discovered {len(all_drawers)} mathicon drawers; rendering {len(render_drawers)}.")
    
    # We will build categories for the gallery
    # 1. Main Icons (those with metadata in icon_metadata.json)
    # 2. Matrix Icons (category == matrix)
    # 3. Others
    
    main_rows = []
    matrix_rows = []
    neural_network_rows = []
    other_rows = []
    
    animated_icons = set(gif_icons) if gif_icons is not None else (metadata_gif_icons or set(DEFAULT_GIF_WHITELIST))
    supported_icons = supported_animated_icons()
    unsupported_requested = sorted(animated_icons - supported_icons)
    if unsupported_requested:
        print(
            "Requested GIF icons without animation profiles (will be static): "
            + ", ".join(unsupported_requested)
        )

    print(f"GIF whitelist size: {len(animated_icons)}")
    print(f"GIF supported profiles: {len(supported_icons)}")
    print(f"Force re-render: {force}")

    png_rendered = 0
    png_skipped = 0
    gif_rendered = 0
    gif_skipped = 0
    gif_unsupported = 0
    
    idx = 0
    for name, draw_func in sorted(render_drawers.items()):
        idx += 1
        print(f"[{idx}/{len(render_drawers)}] Processing icon: {name}...")
        
        # 1. Render PNG
        png_path = images_dir / f"{name}.png"
        render_kw = _render_kwargs_for_icon(name)
        if force or not png_path.exists():
            render_icon_preview(
                name, draw_func, images_dir,
                file_format="png", autofit=True, **render_kw,
            )
            png_rendered += 1
        else:
            png_skipped += 1
        
        # 2. Render GIF if animated
        gif_str = "Static Only"
        if name in animated_icons and name in supported_icons:
            gif_path = images_dir / f"{name}.gif"
            if force or not gif_path.exists():
                animate_icon_preview(
                    name, draw_func, images_dir,
                    file_format="gif", autofit=True, **DEFAULT_GIF_RENDER,
                )
                gif_rendered += 1
            else:
                gif_skipped += 1
            gif_str = f"![{name} gif](images/icons/{name}.gif)"
        elif name in animated_icons:
            gif_unsupported += 1
            
        plt.close("all")  # Prevent warning about too many figures open

    for name in sorted(all_drawers):
        meta = metadata.get(name, {})
        title = meta.get("title", name.replace("_", " ").title())
        desc = _desc_for_icon(name, meta, metadata_payload)
        
        # Determine group
        gif_str = "Static Only"
        if name in animated_icons and name in supported_icons:
            gif_path = images_dir / f"{name}.gif"
            if gif_path.exists():
                gif_str = f"![{name} gif](images/icons/{name}.gif)"
        img_str = f"![{name}](images/icons/{name}.png)"
        row = f"| **{name}**<br>*{title}* | {img_str} | {gif_str} | {desc} |\n"

        from mathicon import get_icon_spec

        try:
            category = get_icon_spec(name).category
        except KeyError:
            category = ""

        if category == "neural_network":
            neural_network_rows.append(row)
        elif category == "matrix":
            matrix_rows.append(row)
        elif name in metadata:
            main_rows.append(row)
        else:
            other_rows.append(row)

    # Compile the final Markdown file
    md_content = """# Icons reference gallery

Welcome to the complete Mathicon gallery. This reference page is automatically compiled, showcasing all built-in static and animated icons.

## Mathematical Primitives & Core Topics
These icons represent specific mathematical topics and are matched to the chapters of the *Mathematics for AI* textbook.

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
""" + "".join(main_rows) + """
## Matrix Icons
Matrix shapes and layouts using the book legend color scheme (`chapterx/img/legend.py`). Use these ids in mindmaps for consistent matrix taxonomy.

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
""" + "".join(matrix_rows) + """
## Neural Network Icons
Architecture diagrams rendered with [visualtorch](https://github.com/willyfh/visualtorch). Requires `pip install mathicon[nn]` (torch + aggdraw).

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
""" + "".join(neural_network_rows) + """
## Other Miscellaneous Icons

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
""" + "".join(other_rows) + "\n"

    reference_path = docs_root / "docs" / "icons-reference.md"
    reference_path.write_text(md_content, encoding="utf-8")
    print(
        "Render summary: "
        f"PNG rendered={png_rendered}, PNG skipped={png_skipped}, "
        f"GIF rendered={gif_rendered}, GIF skipped={gif_skipped}, "
        f"GIF unsupported={gif_unsupported}"
    )
    print(f"Successfully generated icons reference page at: {reference_path}")

if __name__ == "__main__":
    args = parse_args()
    build_gallery(
        gif_icons=args.gif_icons,
        force=args.force,
        icon_filter=args.icons,
    )
