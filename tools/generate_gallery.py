import sys
import json
from pathlib import Path
import matplotlib.pyplot as plt

# Add mathicon path
sys.path.insert(0, "/home/wukong/math4ai/shared/mathicon/src")
from mathicon.preview_icons import discover_icon_drawers, render_icon_preview, animate_icon_preview

def build_gallery():
    docs_root = Path("/home/wukong/math4ai/shared/mathicon-docs")
    images_dir = docs_root / "docs" / "images" / "icons"
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Load metadata
    metadata_path = Path("/home/wukong/math4ai/shared/mathicon/icon_metadata.json")
    if metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f).get("icons", {})
    else:
        metadata = {}
        
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
    
    animated_icons = {"rotation", "score_field", "scaling", "shear"}
    
    idx = 0
    for name, draw_func in sorted(drawers.items()):
        idx += 1
        print(f"[{idx}/{len(drawers)}] Processing icon: {name}...")
        
        # 1. Render PNG
        png_path = images_dir / f"{name}.png"
        # Always render to ensure it's fresh and uses the latest modularized logic
        render_icon_preview(
            name, draw_func, images_dir, 
            file_format="png", dpi=80, figure_size=(1.8, 1.8), autofit=True
        )
        
        # 2. Render GIF if animated
        gif_str = "Static Only"
        if name in animated_icons:
            gif_path = images_dir / f"{name}.gif"
            animate_icon_preview(
                name, draw_func, images_dir,
                file_format="gif", dpi=80, figure_size=(1.8, 1.8),
                frames=15, fps=10, autofit=True
            )
            gif_str = f"![{name} gif](images/icons/{name}.gif)"
            
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
    print(f"Successfully generated icons reference page at: {reference_path}")

if __name__ == "__main__":
    build_gallery()
