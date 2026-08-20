"""
Visualization Module for AMP-GEN Material Passport.

Generates a clean, professional building-level material category distribution bar chart
and saves it to output/visualization.png.
"""

import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def generate_material_distribution_chart(json_path="output/passport.json", output_png="output/visualization.png"):
    """
    Reads output/passport.json, aggregates item counts per Material Category,
    and renders a high-quality bar chart saved to output/visualization.png.
    """
    if not os.path.exists(json_path):
        from src.export import run_export
        run_export()
        
    with open(json_path, "r", encoding="utf-8") as f:
        records = json.load(f)
        
    # Aggregate category counts
    cat_counts = {}
    for rec in records:
        cat = rec.get("material_category") or "Unclassified"
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        
    # Sort categories by count descending
    sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
    categories = [x[0] for x in sorted_cats]
    counts = [x[1] for x in sorted_cats]
    
    # Plotting style
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', 
              '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', 
              '#8c564b', '#c49c94']
    
    bars = ax.bar(categories, counts, color=colors[:len(categories)], edgecolor='black', linewidth=0.8, alpha=0.9)
    
    # Value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4),  # 4 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
                    
    # Chart styling
    ax.set_title("CBRI Principal's Residence — Material Category Distribution", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Material Category", fontsize=12, fontweight='bold', labelpad=10)
    ax.set_ylabel("Number of BoQ Line Items", fontsize=12, fontweight='bold', labelpad=10)
    
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.xticks(rotation=35, ha='right', fontsize=10)
    plt.yticks(fontsize=10)

    # Grid & layout optimization
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_png), exist_ok=True)
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Generated visualization chart at {output_png}")


if __name__ == "__main__":
    generate_material_distribution_chart()
