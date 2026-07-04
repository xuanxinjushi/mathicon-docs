import sys
import json
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

# Add mathicon path
sys.path.insert(0, "/home/wukong/math4ai/shared/mathicon/src")
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
    return parser.parse_args()


def build_gallery(gif_icons=None, force=False):
    docs_root = Path("/home/wukong/math4ai/shared/mathicon-docs")
    images_dir = docs_root / "docs" / "images" / "icons"
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Load metadata
    metadata_path = Path("/home/wukong/math4ai/shared/mathicon/icon_metadata.json")
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
        
    drawers = discover_icon_drawers()
    print(f"Discovered {len(drawers)} mathicon drawers.")
    
    # We will build categories for the gallery
    # 1. Main Icons (those with metadata in icon_metadata.json)
    # 2. Legend Icons (those starting with legend_)
    # 3. Base Matrix Shapes (diagonal, upper, lower, row, col, tall, wide, etc.)
    # 4. Others
    
    main_rows = []
    legend_rows = []
    matrix_rows = []
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
    for name, draw_func in sorted(drawers.items()):
        idx += 1
        print(f"[{idx}/{len(drawers)}] Processing icon: {name}...")
        
        # 1. Render PNG
        png_path = images_dir / f"{name}.png"
        if force or not png_path.exists():
            render_icon_preview(
                name, draw_func, images_dir,
                file_format="png", dpi=80, figure_size=(1.8, 1.8), autofit=True
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
                    file_format="gif", dpi=80, figure_size=(1.8, 1.8),
                    frames=15, fps=10, autofit=True
                )
                gif_rendered += 1
            else:
                gif_skipped += 1
            gif_str = f"![{name} gif](images/icons/{name}.gif)"
        elif name in animated_icons:
            gif_unsupported += 1
            
        plt.close("all")  # Prevent warning about too many figures open
        
        # Look up metadata
        meta = metadata.get(name, {})
        title = meta.get("title", name.replace("_", " ").title())
        desc = meta.get("description", "No description provided.")
        
        # Determine group
        img_str = f"![{name}](images/icons/{name}.png)"
        row = f"| **{name}**<br>*{title}* | {img_str} | {gif_str} | {desc} |\n"
        
        if name in metadata:
            main_rows.append(row)
        elif name.startswith("legend_"):
            legend_rows.append(row)
        elif any(m in name for m in ["_matrix", "_vector", "row", "col", "tall", "wide"]):
            matrix_rows.append(row)
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
## Base Matrix Shapes & Basic Layouts
These utility icons are used to represent standard matrix patterns (like upper triangular, row/column vectors, etc.) in mathematical diagrams.

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
""" + "".join(matrix_rows) + """
## Legend Matrix Styles
These stylized icons are used to render key legends and specialized color codings in matrix diagrams.

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
""" + "".join(legend_rows) + """
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
    selected_gif_icons = args.gif_icons
    build_gallery(gif_icons=selected_gif_icons, force=args.force)
