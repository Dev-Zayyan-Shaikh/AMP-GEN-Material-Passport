"""
Material Classification & Taxonomy Module for AMP-GEN Material Passport.

Provides standard classifications, discipline tags, material categories,
all materials detected, grades, mix ratios, and confidence scores across all 64 BoQ items.
"""

def classify_boq_item(item_no: int, description: str, orig_unit: str):
    """
    Classifies a BoQ item into standard schema attributes.
    Returns dict containing:
    - floor_section
    - discipline
    - material_product
    - all_materials_detected
    - material_category
    - material_confidence
    - grade
    - mix_ratio
    - classification_matched
    """
    desc_lower = description.lower()
    
    # Defaults
    floor_section = "General Building Work"
    discipline = "Civil & Sitework"
    material_product = "Construction Material"
    all_materials_detected = "Various"
    material_category = "Other"
    confidence = "High"
    grade = None
    mix_ratio = None
    classification_matched = "General Construction"
    
    # Determine Mix Ratio if present
    for mr in ["1:5:10", "1:2:4", "1:4:8", "1:3:6", "1:6", "1:3", "1:4", "1:5", "1:2", "3:1", "4:7"]:
        if mr in description or mr in desc_lower:
            mix_ratio = mr
            break
            
    # Determine Grade if present
    for g in ["m-15", "m-20", "m-25", "fe-415", "fe-500", "80/100", "first class", "1st class", "2nd class", "class 50", "class designation 50", "class designation 75"]:
        if g in desc_lower:
            grade = g.upper()
            break

    # 1. Earthwork (Items 1 - 5)
    if item_no in [1, 2, 3, 4, 5]:
        floor_section = "Sub-Head I - Earthwork & Site Preparation"
        discipline = "Civil & Sitework"
        material_category = "Earthwork"
        if item_no == 1:
            material_product = "Earthwork in excavation"
            all_materials_detected = "Soil, Earth"
            classification_matched = "Earthwork excavation"
        elif item_no in [2, 3]:
            material_product = "Plinth & Trench Earth / Sand Filling"
            all_materials_detected = "Excavated Earth, Fine Sand" if item_no == 3 else "Excavated Earth"
            classification_matched = "Earth & Sand Filling"
        elif item_no == 4:
            material_product = "Surface Dressing of Ground"
            all_materials_detected = "Soil"
            classification_matched = "Site Dressing"
        elif item_no == 5:
            material_product = "Chemical Anti-Termite Treatment"
            all_materials_detected = "Aldrin Emulsifiable Concentrate (0.5%), Water"
            classification_matched = "Anti-Termite Chemical Barrier"

    # 2. Concrete Work (PCC: Items 6, 7, 8)
    elif item_no in [6, 7, 8]:
        floor_section = "Sub-Head II - Plain Cement Concrete"
        discipline = "Structural"
        material_category = "Concrete"
        grade = grade or "M-15"
        if mix_ratio == "1:5:10":
            material_product = "Plain Cement Concrete 1:5:10"
            all_materials_detected = "Cement, Fine Sand, Graded Stone Aggregate (40mm)"
            classification_matched = "PCC 1:5:10 (M-15 equivalent)"
        elif mix_ratio == "1:2:4":
            material_product = "Plain Cement Concrete 1:2:4"
            all_materials_detected = "Cement, Coarse Sand, Graded Stone Aggregate (20mm)"
            classification_matched = "PCC 1:2:4"

    # 3. RCC Work & Reinforcement (Items 9 - 18)
    elif item_no in range(9, 19):
        floor_section = "Sub-Head III - RCC & Structural Concrete"
        discipline = "Structural"
        if item_no in [9, 10]:
            material_category = "Waterproofing / Bitumen"
            if item_no == 9:
                material_product = "Damp-Proof Course (DPC) 40mm 1:2:4"
                all_materials_detected = "Cement, Coarse Sand, Stone Aggregate (12.5mm)"
                classification_matched = "DPC Concrete Layer"
            else:
                material_product = "Residual Petroleum Bitumen 80/100"
                all_materials_detected = "Petroleum Bitumen 80/100, Kerosene"
                classification_matched = "Bitumen Damp-Proof Membrane"
        elif item_no in [11, 12, 13, 14, 15, 18]:
            material_category = "Concrete"
            grade = "M-20"
            mix_ratio = mix_ratio or "1:2:4"
            material_product = "Reinforced Cement Concrete 1:2:4"
            all_materials_detected = "Cement, Coarse Sand, Graded Stone Aggregate (20mm)"
            classification_matched = f"RCC 1:2:4 ({'Floors' if item_no==11 else 'Beams/Lintels' if item_no==14 else 'Columns' if item_no==15 else 'Structural Members'})"
        elif item_no == 16:
            material_category = "Wood" # Formwork
            material_product = "Centring & Formwork Shuttering"
            all_materials_detected = "Timber, Steel Props/Clamps, Plywood"
            classification_matched = "Temporary Formwork Shuttering"
        elif item_no == 17:
            material_category = "Reinf"
            grade = "Fe-415 / Fe-500D"
            material_product = "Steel Reinforcement (TMT / Mild Steel)"
            all_materials_detected = "Thermo-Mechanically Treated (TMT) Steel, Binding Wire"
            classification_matched = "Reinforcement Steel Bars"

    # 4. Brick Masonry (Items 19 - 23)
    elif item_no in range(19, 24):
        floor_section = "Sub-Head IV - Brick Masonry Work"
        discipline = "Structural"
        material_category = "Masonry"
        grade = grade or "Class Designation 50 / 75"
        mix_ratio = mix_ratio or ("1:6" if item_no in [19, 20] else "1:3" if item_no == 21 else "1:4")
        material_product = f"Burnt Clay Brick Masonry ({mix_ratio})"
        all_materials_detected = f"Burnt Clay Bricks, Cement Mortar ({mix_ratio})"
        classification_matched = "Clay Brick Masonry"

    # 5. Woodwork & Joinery / Doors / Windows / Aluminium / Steel (Items 24 - 39)
    elif item_no in range(24, 40):
        floor_section = "Sub-Head V - Joinery, Doors, Windows & Hardware"
        discipline = "Architectural & Finishes"
        
        if item_no in [28, 29, 34, 35, 37, 38, 39] or any(k in desc_lower for k in ["steel", "iron frame", "guard flat", "fan clamp", "m.s.", "m.s", "hasp", "ventilator catch"]):
            material_category = "Steel"
            if item_no == 28:
                material_product = "Oxidised MS Fanlight Ventilator Catch"
                all_materials_detected = "Mild Steel (MS), Screws"
                classification_matched = "MS Fanlight Catch Fitting"
            elif item_no == 29:
                material_product = "Oxidised MS Hasp & Staple"
                all_materials_detected = "Mild Steel (MS), Screws"
                classification_matched = "MS Hasp & Staple Fitting"
            else:
                material_product = "Rolled Steel Sections / Iron Frames / Hardware"
                all_materials_detected = "Mild Steel, Priming Coat"
                classification_matched = "Steel Windows & Iron Frame Sections"
        elif any(k in desc_lower for k in ["aluminium", "aluminum"]) or item_no in [30, 31, 32, 33, 36]:
            material_category = "Aluminium"
            material_product = "Extruded Aluminium Section / Hardware"
            all_materials_detected = "Anodised Aluminium Alloy, Steel Screws"
            classification_matched = "Aluminium Fittings & Joinery"
        else: # Wood items: 24, 25, 26, 27
            material_category = "Wood"
            if item_no == 27:
                material_product = "Teak Wood Plugs"
                all_materials_detected = "2nd Class Teak Wood, Cement Mortar 1:3"
                classification_matched = "Teak Wood Plugs in Masonry"
            else:
                material_product = "Timber Wood Frames / Flush Door Shutters"
                all_materials_detected = "Teak/Hardwood Timber, Teak Veneer, Commercial Ply, Glue"
                classification_matched = "Timber Wood Joinery"

    # 6. Flooring & Skirting (Items 40 - 43)
    elif item_no in range(40, 44):
        floor_section = "Sub-Head VI - Flooring & Interior Finishes"
        discipline = "Architectural & Finishes"
        if item_no == 40:
            material_category = "Flooring"
            material_product = "Cement Concrete Flooring 40mm 1:2:4"
            all_materials_detected = "Cement, Coarse Sand, Stone Aggregate (20mm), Neat Cement"
            classification_matched = "40mm CC Flooring"
        elif item_no == 41:
            material_category = "Plaster"
            material_product = "Cement Plaster Skirting 18mm 1:3"
            all_materials_detected = "Cement, Coarse Sand, Neat Cement"
            classification_matched = "Cement Plaster Skirting Render"
        elif item_no == 42:
            material_category = "Flooring"
            material_product = "Marble Chips Terrazzo Flooring 40mm"
            all_materials_detected = "Marble Chips, Cement, Marble Powder, Coarse Sand"
            classification_matched = "Terrazzo Marble Chips Flooring"
        elif item_no == 43:
            material_category = "Flooring"
            material_product = "Glass Strips in Flooring Joints"
            all_materials_detected = "Sheet Glass Strips (40x6mm)"
            classification_matched = "Flooring Divider Strips"

    # 7. Roofing & Waterproofing / Drainage (Items 44 - 51)
    elif item_no in range(44, 52):
        floor_section = "Sub-Head VII - Roofing & Rainwater Drainage"
        if item_no in [49, 50, 51] or any(k in desc_lower for k in ["pipe", "holderbat", "rain water pipe", "accessories"]):
            discipline = "Plumbing & Drainage"
            material_category = "Plumbing"
            if item_no == 49:
                material_product = "Wallface CI Rainwater Pipe"
                all_materials_detected = "Cast Iron (CI), Spun Yarn, Cement Mortar 1:2"
                classification_matched = "CI Rainwater Pipe"
            elif item_no == 51:
                material_product = "Rainwater Pipe Accessories"
                all_materials_detected = "Cast Iron (CI) Plain Head, Shoe, Bend, Cement Mortar 1:2"
                classification_matched = "CI Rainwater Pipe Fittings"
            else:
                material_product = "Cast Iron Holderbat Clamps"
                all_materials_detected = "Mild Steel / Cast Iron, Cement Concrete Blocks"
                classification_matched = "Rainwater Pipe Clamps"
        else:
            discipline = "Architectural & Finishes"
            material_category = "Waterproofing / Bitumen"
            if item_no == 44:
                material_product = "Bitumen Water-Proofing Membrane"
                all_materials_detected = "Petroleum Bitumen 80/100, Coarse Sand"
                classification_matched = "Bituminous Roof Coating"
            elif item_no == 45:
                material_product = "Lime Concrete Terracing 10cm"
                all_materials_detected = "Brick Aggregate (25mm), Lime Mortar 1:2 (Lime Putty, Surkhi), FPS Brick Tiles"
                classification_matched = "Lime Concrete Roof Terracing"
            elif item_no == 46:
                material_product = "Burnt Clay Tile Roof Covering 25mm"
                all_materials_detected = "Burnt Clay Tiles (250x250x25mm), Cement Mortar 1:3"
                classification_matched = "Clay Tile Roof Layer"
            elif item_no == 47:
                material_product = "Cement Concrete Gola 15x15cm"
                all_materials_detected = "Cement Concrete 1:3:6, Brick Tiles, Cement Mortar 1:3"
                classification_matched = "Concrete Roof Gola"
            elif item_no == 48:
                material_product = "Concrete Khurras 45x45cm"
                all_materials_detected = "Cement Concrete 1:2:4, PVC Sheet 400 micron, Cement Plaster 1:3"
                classification_matched = "Roof Drainage Khurras"

    # 8. Plastering, Painting & Finishes (Items 52 - 64)
    elif item_no in range(52, 65):
        floor_section = "Sub-Head VIII - Plastering, Painting & External Works"
        discipline = "Architectural & Finishes"
        if item_no in [52, 53, 54, 55, 56] or "plaster" in desc_lower:
            material_category = "Plaster"
            mix_ratio = mix_ratio or ("1:6" if item_no in [52, 53] else "1:3")
            if item_no == 53:
                material_product = "15 mm Cement Plaster 1:6"
                all_materials_detected = "Cement, Fine Sand"
                classification_matched = "Cement Plaster 15mm Render"
            else:
                material_product = f"Cement Plaster ({mix_ratio})"
                all_materials_detected = "Cement, Fine Sand, Neat Cement Coat"
                classification_matched = "Cement Plaster Render"
        elif item_no in range(57, 64) or any(k in desc_lower for k in ["washing", "primer", "painting", "paint", "polishing"]):
            material_category = "Paint / Finish"
            if "white" in desc_lower:
                material_product = "White Wash (Lime)"
                all_materials_detected = "Lime, Water, Gum"
                classification_matched = "Lime White Wash Coating"
            elif "colour" in desc_lower or "color" in desc_lower:
                material_product = "Colour Wash"
                all_materials_detected = "Lime Wash, Pigment (Green/Blue/Buff)"
                classification_matched = "Pigmented Colour Wash"
            elif "primer" in desc_lower:
                material_product = "Priming Coat Paint (Pink/Gray/Zinc Chromate)"
                all_materials_detected = "Zinc Chromate / Oil-based Primer, Solvent"
                classification_matched = "Surface Priming Paint"
            elif "bitumastic" in desc_lower or "bitumen" in desc_lower:
                material_product = "Bitumastic Paint for CI Pipes"
                all_materials_detected = "Anti-Corrosive Bitumastic Paint"
                classification_matched = "Anti-Corrosive Pipe Coating"
            elif "french" in desc_lower or "spirit" in desc_lower:
                material_product = "French Spirit Wood Polish"
                all_materials_detected = "Spirit, Shellac Wood Filler, Polish"
                classification_matched = "French Spirit Wood Polish"
            else:
                material_product = "Synthetic Enamel Paint"
                all_materials_detected = "Synthetic Enamel Paint, Undercoat Paint"
                classification_matched = "Synthetic Enamel Finish"
        elif item_no == 64:
            floor_section = "Sub-Head IX - External Apron & Plinth Protection"
            discipline = "Civil & Sitework"
            material_category = "Concrete"
            mix_ratio = "1:3:6"
            material_product = "Plinth Protection 50mm CC 1:3:6"
            all_materials_detected = "Cement Concrete 1:3:6, Dry Brick Ballast (40mm), Fine Sand"
            classification_matched = "Plinth Protection Apron"

    return {
        "floor_section": floor_section,
        "discipline": discipline,
        "material_product": material_product,
        "all_materials_detected": all_materials_detected,
        "material_category": material_category,
        "material_confidence": confidence,
        "grade": grade,
        "mix_ratio": mix_ratio,
        "classification_matched": classification_matched
    }
