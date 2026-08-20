"""
Master Pipeline Entrypoint for AMP-GEN Material Passport.

Runs extraction, normalization, classification, carbon calculation,
export to Excel & JSON, building metadata creation, visualization, and validation.
"""

import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from src.export import run_export
from src.extract import get_building_metadata
from src.visualize import generate_material_distribution_chart
from src.validate import validate_all

def main():
    print("==================================================")
    print("   STARTING AMP-GEN MATERIAL PASSPORT PIPELINE    ")
    print("==================================================\n")
    
    # 1. Save Building Metadata (Bonus B3)
    meta = get_building_metadata()
    os.makedirs("output", exist_ok=True)
    meta_path = "output/building_meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
    print(f"Saved building metadata to {meta_path}")
    
    # 2. Run Export (Generates passport.json and passport_filled.xlsx)
    records = run_export()
    
    # 3. Generate Visualization (Generates visualization.png)
    generate_material_distribution_chart()
    
    # 4. Run Automated Validation Suite
    validate_all()
    
    print("==================================================")
    print("  PIPELINE EXECUTION COMPLETED SUCCESSFULLY!      ")
    print("==================================================")

if __name__ == "__main__":
    main()
