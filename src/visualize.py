"""
Visualization Module for AMP-GEN Material Passport.

Generates a polished, dark-themed horizontal bar chart of material category
distribution and saves it to output/visualization.png.
"""

import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import numpy as np


def generate_material_distribution_chart(
    json_path: str = "output/passport.json",
    output_png: str = "output/visualization.png",
) -> None:
    """
    Reads output/passport.json, aggregates BoQ item counts per Material Category,
    and renders a premium dark-themed horizontal bar chart to output/visualization.png.
    """
    if not os.path.exists(json_path):
        from src.export import run_export
        run_export()

    with open(json_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    # ── Aggregate category counts ──────────────────────────────────────────────
    cat_counts: dict[str, int] = {}
    for rec in records:
        cat = rec.get("material_category") or "Unclassified"
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    # Sort ascending so longest bar is on top in horizontal chart
    sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1])
    categories = [x[0] for x in sorted_cats]
    counts = [x[1] for x in sorted_cats]
    n = len(categories)

    # ── Colour palette (blue → teal gradient across bars) ────────────────────
    palette = [
        "#1E3A5F", "#1A4F7F", "#17649F", "#1479BF",
        "#118FDD", "#0EA5E9", "#38BDF8", "#7DD3FC",
        "#BAE6FD", "#E0F2FE", "#CFFAFE", "#A5F3FC",
    ]
    bar_colors = [palette[int(i * (len(palette) - 1) / max(n - 1, 1))] for i in range(n)]

    # ── Figure & dark background ──────────────────────────────────────────────
    BG        = "#0F172A"
    PANEL_BG  = "#1E293B"
    TEXT_COL  = "#E2E8F0"
    GRID_COL  = "#334155"
    ACCENT    = "#38BDF8"

    fig, ax = plt.subplots(figsize=(14, 7), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PANEL_BG)

    # ── Horizontal bars ───────────────────────────────────────────────────────
    y_pos = np.arange(n)
    bars = ax.barh(y_pos, counts, color=bar_colors, height=0.65,
                   edgecolor="none", zorder=3)

    # Value label inside / outside each bar
    # Reinforcement bar: light label (dark bar). All others: black.
    for idx, (bar, val, cat) in enumerate(zip(bars, counts, categories)):
        x_end = bar.get_width()
        x_max = max(counts)
        inside = x_end > x_max * 0.25
        is_reinf = "reinf" in cat.lower() or "steel" in cat.lower()
        if is_reinf:
            label_color = TEXT_COL if inside else ACCENT
        else:
            label_color = "#000000"
        ax.text(
            x_end - (0.3 if inside else -0.3),
            bar.get_y() + bar.get_height() / 2,
            str(int(val)),
            va="center",
            ha="right" if inside else "left",
            fontsize=11,
            fontweight="bold",
            color=label_color,
        )

    # ── Axes styling ─────────────────────────────────────────────────────────
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=11, color=TEXT_COL)
    ax.tick_params(axis="x", colors=TEXT_COL, labelsize=10)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlim(0, max(counts) * 1.15)
    ax.xaxis.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)

    # ── Labels & title ────────────────────────────────────────────────────────
    ax.set_xlabel("Number of BoQ Line Items", fontsize=12, color=TEXT_COL,
                  labelpad=10, fontweight="600")

    ax.set_title(
        "CBRI Principal's Residence — Material Category Distribution",
        fontsize=15, fontweight="bold", color=TEXT_COL, pad=18, loc="left",
    )
    ax.text(
        0, 1.01,
        "64 BoQ items • Schedule \"A\" • AMP-GEN Material Passport",
        transform=ax.transAxes,
        fontsize=9, color="#64748B",
    )

    plt.tight_layout(pad=2.5)

    os.makedirs(os.path.dirname(output_png) if os.path.dirname(output_png) else ".", exist_ok=True)
    plt.savefig(output_png, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close()

    print(f"Generated visualization chart at {output_png}")


if __name__ == "__main__":
    generate_material_distribution_chart()

