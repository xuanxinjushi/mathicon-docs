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
from mathicon.manim_icons import MANIM_ICON_SCENES, render_manim_icon_preview
from mathicon import get_icon_spec


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

# 2.0 in × 150 dpi → 300×300 px
DEFAULT_GIF_RENDER = {
    "dpi": 150,
    "figure_size": (2.0, 2.0),
    "frames": 30,
    "fps": 15,
    "pad_frac": 0.05,
}

# Registry category → gallery section (order preserved).
CATEGORY_SECTIONS = [
    (
        "linear_algebra",
        "Linear Algebra",
        "Vectors, linear maps, subspaces, and decompositions used throughout the book.",
    ),
    (
        "matrix",
        "Matrix Icons",
        "Matrix shapes and layouts using the book legend color scheme (`chapterx/img/legend.py`).",
    ),
    (
        "calculus",
        "Calculus",
        "Derivatives, gradients, and multivariate calculus primitives.",
    ),
    (
        "optimization",
        "Optimization",
        "Loss landscapes, gradient methods, and variational objectives.",
    ),
    (
        "probability",
        "Probability",
        "Distributions, information measures, and probabilistic building blocks.",
    ),
    (
        "stochastics",
        "Stochastics",
        "SDEs, diffusion, sampling, and stochastic-process sample paths.",
    ),
    (
        "neural_network",
        "Neural Network Icons",
        "Architecture diagrams; `nn_mlp` uses a Manim forward-pass flow animation (GIF + MP4).",
    ),
]


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


def _md_table_cell(text: str) -> str:
    """Escape ``|`` so conditional bars in math do not split markdown table rows."""
    return text.replace("|", r"\|")


def _gif_cell(name: str, animated_icons: set, supported_icons: set) -> str:
    if name in animated_icons and name in supported_icons:
        return f"![{name} gif](images/icons/{name}.gif)"
    return "—"


def _mp4_cell(name: str, manim_icons: set) -> str:
    if name in manim_icons:
        # MkDocs rewrites markdown image paths but not raw HTML; use a path that
        # resolves from docs/icons-reference.md (../images/...).
        return (
            f'<video src="../images/icons/{name}.mp4" width="200" height="200" '
            f'autoplay loop muted playsinline></video>'
        )
    return "—"


def build_gallery(gif_icons=None, force=False, icon_filter=None):
    docs_root = DOCS_ROOT
    images_dir = docs_root / "docs" / "images" / "icons"
    images_dir.mkdir(parents=True, exist_ok=True)

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
    metadata_manim_icons = {
        str(icon).strip() for icon in metadata_payload.get("manim_icons", []) if str(icon).strip()
    }
    if not metadata_manim_icons:
        metadata_manim_icons = set(MANIM_ICON_SCENES)

    all_drawers = discover_icon_drawers()
    if icon_filter:
        missing = sorted(set(icon_filter) - set(all_drawers))
        if missing:
            print(f"Warning: unknown icon ids (skipped): {', '.join(missing)}")
        render_drawers = {k: v for k, v in all_drawers.items() if k in icon_filter}
    else:
        render_drawers = all_drawers
    print(f"Discovered {len(all_drawers)} mathicon drawers; rendering {len(render_drawers)}.")

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
    manim_rendered = 0
    manim_skipped = 0

    idx = 0
    for name, draw_func in sorted(render_drawers.items()):
        idx += 1
        print(f"[{idx}/{len(render_drawers)}] Processing icon: {name}...")

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

        # matplotlib GIF (unchanged): the existing loopable animation.
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
        elif name in animated_icons and name not in metadata_manim_icons:
            gif_unsupported += 1

        # Manim MP4 (additive): an extra, richer video option. Does NOT replace
        # the matplotlib GIF above; only writes the .mp4 asset.
        if name in metadata_manim_icons:
            mp4_path = images_dir / f"{name}.mp4"
            if force or not mp4_path.exists():
                render_manim_icon_preview(
                    name, images_dir, force=force, write_mp4=True, write_gif=False,
                )
                manim_rendered += 1
            else:
                manim_skipped += 1

        plt.close("all")

    category_rows: dict[str, list[str]] = {cat: [] for cat, _, _ in CATEGORY_SECTIONS}
    uncategorized_rows: list[str] = []

    for name in sorted(all_drawers):
        meta = metadata.get(name, {})
        title = meta.get("title", name.replace("_", " ").title())
        desc = _desc_for_icon(name, meta, metadata_payload)
        img_str = f"![{name}](images/icons/{name}.png)"
        gif_str = _gif_cell(name, animated_icons, supported_icons)
        mp4_str = _mp4_cell(name, metadata_manim_icons)
        row = (
            f"| **{name}**<br>*{title}* | {img_str} | {gif_str} | {mp4_str} "
            f"| {_md_table_cell(desc)} |\n"
        )

        spec = get_icon_spec(name)
        category = spec.category if spec else ""
        if category in category_rows:
            category_rows[category].append(row)
        else:
            uncategorized_rows.append(row)

    md_parts = [
        "# Icons reference gallery\n",
        "\nWelcome to the complete Mathicon gallery. Icons are grouped by registry category. "
        "This reference page is automatically compiled, showcasing all built-in static and animated icons.\n",
    ]

    table_header = (
        "\n| Key / Title | Static Image | Loopable GIF | MP4 | Concept & Role |\n"
        "| :--- | :---: | :---: | :---: | :--- |\n"
    )

    for cat_id, cat_title, cat_blurb in CATEGORY_SECTIONS:
        rows = category_rows.get(cat_id, [])
        if not rows:
            continue
        md_parts.append(f"\n## {cat_title}\n\n{cat_blurb}\n")
        md_parts.append(table_header)
        md_parts.extend(rows)

    if uncategorized_rows:
        md_parts.append("\n## Other Icons\n\nIcons without a registry category.\n")
        md_parts.append(table_header)
        md_parts.extend(uncategorized_rows)

    md_parts.append("\n")

    reference_path = docs_root / "docs" / "icons-reference.md"
    reference_path.write_text("".join(md_parts), encoding="utf-8")
    print(
        "Render summary: "
        f"PNG rendered={png_rendered}, PNG skipped={png_skipped}, "
        f"GIF rendered={gif_rendered}, GIF skipped={gif_skipped}, "
        f"GIF unsupported={gif_unsupported}, "
        f"Manim rendered={manim_rendered}, Manim skipped={manim_skipped}"
    )
    print(f"Successfully generated icons reference page at: {reference_path}")


if __name__ == "__main__":
    args = parse_args()
    build_gallery(
        gif_icons=args.gif_icons,
        force=args.force,
        icon_filter=args.icons,
    )
