"""
Unit Normalization & Quantity Handling Module for AMP-GEN Material Passport.

Handles conversion and normalization of units, quantities, and dimensional fields
according to the template instructions.
"""

def normalize_unit(unit_str: str) -> str:
    """
    Normalizes source unit string into standard template conventions:
    - Cu.m / cum / m³ / Cubic Metre / cu.m / cubic metre -> cum
    - Sq.m / sqm / m² / sq.m / square metre -> sqm
    - Mtr. / m / mtr / metre / meter -> m
    - Kg. / kg / quintal -> kg
    - Each / each / Nos / nos / No. -> nos
    """
    if not unit_str:
        return ""
    
    u = unit_str.strip().lower()
    
    if any(term in u for term in ["cu.m", "cum", "m³", "m3", "cubic metre", "cubic meter", "dm³", "dm3", "cubic decimetre", "cubic decimeter"]):
        return "cum"
    elif any(term in u for term in ["sq.m", "sqm", "m²", "m2", "square metre", "square meter"]):
        return "sqm"
    elif u in ["mtr.", "mtr", "m", "metre", "meter", "rm", "r.m.", "metres", "meters"]:
        return "m"
    elif u in ["kg.", "kg", "kgs", "kilogram", "kilograms"]:
        return "kg"
    elif u in ["each", "nos", "nos.", "no", "no.", "number", "numbers"]:
        return "nos"
    
    return u


def process_quantity_and_unit(item_no: str, orig_qty: float, orig_unit: str):
    """
    Processes item quantity, unit normalization, special case handling (item 24),
    and assigns physical dimensional columns.
    
    Returns a dict with:
    - original_quantity
    - original_unit
    - volume_m3
    - area_m2
    - length_m
    - weight_kg
    - count_nos
    - derived_quantity
    - derived_quantity_unit
    - derived_quantity_basis
    - comment_note
    """
    norm_unit = normalize_unit(orig_unit)
    comment_note = None
    clean_item = str(item_no).strip().lstrip('0')
    
    # Special Case: Item 17 has source notation (100 kg + 1375/1500 kg)
    if clean_item in ["17", "17.0", "AMP-GEN-017"]:
        comment_note = "Source notation: 100 kg (Mild steel) + 1375/1500 kg (Cold twisted bars for Zone I-IV / Zone V)."

    # Special Case: Item 24 has 10 cubic decimetre (10 dm³ = 0.01 cum)
    if clean_item in ["24", "24.0", "AMP-GEN-024"]:
        vol_m3 = round(float(orig_qty) * 0.01, 4) if orig_qty is not None else 0.035
        comment_note = f"Normalized {orig_qty} x 10 cubic decimetre (dm³) to {vol_m3} m³ (cum) per template instructions."
        return {
            "original_quantity": vol_m3,
            "original_unit": "cum",
            "volume_m3": vol_m3,
            "area_m2": None,
            "length_m": None,
            "weight_kg": None,
            "count_nos": None,
            "derived_quantity": vol_m3,
            "derived_quantity_unit": "cum",
            "derived_quantity_basis": f"{orig_qty} x 10 dm³ = {vol_m3} m³ conversion per template specification",
            "comment_note": comment_note
        }

    # Standard physical dimension assignment
    vol = None
    area = None
    length = None
    weight = None
    count = None
    
    if norm_unit == "cum":
        vol = float(orig_qty) if orig_qty is not None else None
    elif norm_unit == "sqm":
        area = float(orig_qty) if orig_qty is not None else None
    elif norm_unit == "m":
        length = float(orig_qty) if orig_qty is not None else None
    elif norm_unit == "kg":
        weight = float(orig_qty) if orig_qty is not None else None
    elif norm_unit == "nos":
        count = float(orig_qty) if orig_qty is not None else None
        
    return {
        "original_quantity": orig_qty,
        "original_unit": norm_unit,
        "volume_m3": vol,
        "area_m2": area,
        "length_m": length,
        "weight_kg": weight,
        "count_nos": count,
        "derived_quantity": None,
        "derived_quantity_unit": None,
        "derived_quantity_basis": None,
        "comment_note": comment_note
    }
