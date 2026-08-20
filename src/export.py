"""
Export Module for AMP-GEN Material Passport.

Generates:
1. output/passport_filled.xlsx (populated openpyxl workbook)
2. output/passport.json (structured JSON export with 64 records)
"""

import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import openpyxl

from src.extract import get_all_64_boq_items
from src.normalize import process_quantity_and_unit
from src.classify import classify_boq_item
from src.carbon import get_carbon_data


def generate_passport_records():
    """
    Combines extraction, normalization, classification, and carbon data
    into 64 standardized dictionary records matching the 50-column template schema.
    """
    raw_items = get_all_64_boq_items()
    records = []
    
    for item in raw_items:
        item_no_int = int(item["boq_item_no"])
        gmap_id = f"AMP-GEN-{item_no_int:03d}"
        
        desc = item["description"]
        orig_qty = item["original_quantity"]
        orig_unit = item["original_unit"]
        dsr_sched = item["dsr_schedule"]
        dsr_code = item["dsr_code"]
        
        # 1. Normalization & Physical Dimensions
        norm_data = process_quantity_and_unit(item["boq_item_no"], orig_qty, orig_unit)
        
        # 2. Classification & Taxonomy
        class_data = classify_boq_item(item_no_int, desc, norm_data["original_unit"])
        
        # 3. Carbon & Density Calculations (Bonus B2)
        carbon_data = get_carbon_data(
            class_data["material_category"],
            class_data["material_product"],
            volume_m3=norm_data["volume_m3"],
            weight_kg=norm_data["weight_kg"]
        )
        
        # 4. Construct Comment string combining notes and carbon citations
        comments = []
        if norm_data["comment_note"]:
            comments.append(norm_data["comment_note"])
        if carbon_data["carbon_comment"]:
            comments.append(carbon_data["carbon_comment"])
            
        final_comment = " ".join(comments) if comments else None
        
        record = {
            "gmap_id": gmap_id,
            "boq_item_no": item["boq_item_no"],
            "article_number": None,
            "external_db_id": None,
            "description": desc,
            "floor_section": class_data["floor_section"],
            "discipline": class_data["discipline"],
            "material_product": class_data["material_product"],
            "all_materials_detected": class_data["all_materials_detected"],
            "material_category": class_data["material_category"],
            "material_confidence": class_data["material_confidence"],
            "grade": class_data["grade"],
            "mix_ratio": class_data["mix_ratio"],
            "original_quantity": norm_data["original_quantity"],
            "original_unit": norm_data["original_unit"],
            "volume_m3": norm_data["volume_m3"],
            "area_m2": norm_data["area_m2"],
            "length_m": norm_data["length_m"],
            "weight_kg": norm_data["weight_kg"],
            "count_nos": norm_data["count_nos"],
            "derived_quantity": norm_data["derived_quantity"],
            "derived_quantity_unit": norm_data["derived_quantity_unit"],
            "derived_quantity_basis": norm_data["derived_quantity_basis"],
            "density_kg_m3": carbon_data["density_kg_m3"],
            "embodied_carbon_a1_a3_kg_co2e": carbon_data["embodied_carbon_a1_a3"],
            "gwp_per_kg": carbon_data["gwp_per_kg"],
            "schedule_dsr_sor": dsr_sched,
            "schedule_item_code": dsr_code,
            "standard_code_reference": "IS : 456 / IS : 269 / DSR 1989" if "1:2:4" in desc or "concrete" in desc.lower() else None,
            "classification_matched": class_data["classification_matched"],
            "pct_reused": None,
            "pct_available_for_reuse": None,
            "assumed_construction_waste": None,
            "waste_codes": None,
            "detachability_connection": None,
            "detachability_connection_detail": None,
            "detachability_accessibility": None,
            "detachability_intersection": None,
            "detachability_product_edge": None,
            "lifespan_years": None,
            "length_mm": None,
            "width_mm": None,
            "height_mm": None,
            "thickness_mm": None,
            "depth_mm": None,
            "diameter_mm": None,
            "unit_rate": None,
            "total_cost": None,
            "currency": "INR",
            "comment": final_comment
        }
        
        records.append(record)
        
    return records


def export_json(records, output_path="output/passport.json"):
    """Saves records to output/passport.json."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(records)} records to {output_path}")


def export_excel(records, template_path="input/AMP_Passport_Template.xlsx", output_path="output/passport_filled.xlsx"):
    """
    Populates openpyxl workbook starting at row 7 (preserving headers & examples)
    and saves to output/passport_filled.xlsx.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wb = openpyxl.load_workbook(template_path)
    sheet = wb["Material Passport"]
    
    start_row = 7 # Rows 4-6 contain template example rows
    
    # Map record dictionary keys to 50 columns order
    column_keys = [
        "gmap_id", "boq_item_no", "article_number", "external_db_id", "description",
        "floor_section", "discipline", "material_product", "all_materials_detected",
        "material_category", "material_confidence", "grade", "mix_ratio",
        "original_quantity", "original_unit", "volume_m3", "area_m2", "length_m",
        "weight_kg", "count_nos", "derived_quantity", "derived_quantity_unit",
        "derived_quantity_basis", "density_kg_m3", "embodied_carbon_a1_a3_kg_co2e",
        "gwp_per_kg", "schedule_dsr_sor", "schedule_item_code", "standard_code_reference",
        "classification_matched", "pct_reused", "pct_available_for_reuse",
        "assumed_construction_waste", "waste_codes", "detachability_connection",
        "detachability_connection_detail", "detachability_accessibility",
        "detachability_intersection", "detachability_product_edge", "lifespan_years",
        "length_mm", "width_mm", "height_mm", "thickness_mm", "depth_mm", "diameter_mm",
        "unit_rate", "total_cost", "currency", "comment"
    ]
    
    for idx, rec in enumerate(records):
        current_row = start_row + idx
        for col_idx, key in enumerate(column_keys, start=1):
            val = rec.get(key)
            cell = sheet.cell(row=current_row, column=col_idx)
            cell.value = val
            
    wb.save(output_path)
    print(f"Exported Excel material passport to {output_path}")


def run_export():
    records = generate_passport_records()
    export_json(records)
    export_excel(records)
    return records


if __name__ == "__main__":
    run_export()
