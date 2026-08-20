"""
Carbon & Density Calculation Module (Bonus B2) for AMP-GEN Material Passport.

Populates Density (kg/m³), GWP / kg (kg CO₂e/kg), and total Embodied Carbon A1-A3 (kg CO₂e)
with explicit, peer-reviewed, and ICE Database v3.0 sources documented in the Comment field.
"""

def get_carbon_data(material_category: str, material_product: str, volume_m3: float = None, weight_kg: float = None):
    """
    Determines Density, GWP/kg, and calculated Embodied Carbon A1-A3 based on material classification
    and physical quantities.
    
    Returns dict:
    - density_kg_m3
    - gwp_per_kg
    - embodied_carbon_a1_a3
    - carbon_comment
    """
    cat = (material_category or "").lower()
    prod = (material_product or "").lower()
    
    # 1. Earthwork / Labour / Pure Services -> Excluded
    if "earthwork" in cat or "earth work" in prod or "excavated" in prod:
        return {
            "density_kg_m3": None,
            "gwp_per_kg": None,
            "embodied_carbon_a1_a3": None,
            "carbon_comment": "[EXCLUDED] Earthwork and site excavation involve pure machinery/labour services without permanent material embodied carbon."
        }
        
    # 2. Reinforcement Steel / TMT Bars / Steel MS hardware
    if "reinf" in cat or "steel" in cat or "steel" in prod or "tmt" in prod or "reinforcement" in prod or "ms" in prod:
        density = 7850.0 # kg/m³
        gwp = 2.363 # kg CO2e/kg (ICE v3.0 Steel Rebar / Structural Steel)
        
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": "GWP: 2.363 kg CO2e/kg, Density: 7850 kg/m³ | Source: ICE Database v3.0 (Steel - Rebar / Rod / Structural)."
        }
        
    # 3. Plumbing / Cast Iron Pipes & Fittings
    if "plumbing" in cat or "cast iron" in prod or "ci " in prod or "pipe" in prod:
        density = 7150.0 # kg/m³
        gwp = 2.030 # kg CO2e/kg (ICE v3.0 Cast Iron)
        
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": "GWP: 2.030 kg CO2e/kg, Density: 7150 kg/m³ | Source: ICE Database v3.0 (Cast Iron / Drainage Pipework)."
        }

    # 4. Concrete (Plain or Reinforced)
    if "concrete" in cat or "pcc" in prod or "rcc" in prod or "cement concrete" in prod:
        if "1:4:8" in prod or "m-15" in prod or "plain" in prod:
            density = 2350.0
            gwp = 0.130 # kg CO2e/kg
            source = "ICE Database v3.0 (Concrete 15/20 MPa)"
        else:
            density = 2400.0
            gwp = 0.155 # kg CO2e/kg
            source = "ICE Database v3.0 (Concrete 25/30 MPa)"
            
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": f"GWP: {gwp} kg CO2e/kg, Density: {density} kg/m³ | Source: {source}."
        }
        
    # 5. Brick Masonry
    if "masonry" in cat or "brick" in prod:
        density = 1900.0 # kg/m³
        gwp = 0.240 # kg CO2e/kg
        
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": "GWP: 0.240 kg CO2e/kg, Density: 1900 kg/m³ | Source: ICE Database v3.0 / Indian LCA literature (Burnt Clay Bricks & Mortar)."
        }
        
    # 6. Wood / Timber
    if "wood" in cat or "timber" in prod or "teak" in prod or "woodwork" in prod:
        density = 650.0 # kg/m³
        gwp = 0.450 # kg CO2e/kg
        
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": "GWP: 0.450 kg CO2e/kg, Density: 650 kg/m³ | Source: ICE Database v3.0 (Sawn Timber, fossil GWP A1-A3)."
        }
        
    # 7. Aluminium
    if "aluminium" in cat or "aluminum" in prod or "aluminum" in cat:
        density = 2700.0 # kg/m³
        gwp = 8.90 # kg CO2e/kg
        
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": "GWP: 8.90 kg CO2e/kg, Density: 2700 kg/m³ | Source: ICE Database v3.0 (Extruded Aluminium)."
        }

    # 8. Plaster / Finish / Mortar
    if "plaster" in cat or "mortar" in prod or "rendering" in prod:
        density = 2000.0 # kg/m³
        gwp = 0.180 # kg CO2e/kg
        
        calc_weight = weight_kg
        if calc_weight is None and volume_m3 is not None:
            calc_weight = volume_m3 * density
            
        emb_carbon = round(calc_weight * gwp, 2) if calc_weight is not None else None
        
        return {
            "density_kg_m3": density,
            "gwp_per_kg": gwp,
            "embodied_carbon_a1_a3": emb_carbon,
            "carbon_comment": "GWP: 0.180 kg CO2e/kg, Density: 2000 kg/m³ | Source: ICE Database v3.0 (Cement Mortar / Plaster)."
        }

    # Default fallback when material carbon data is uncertain or not defensively applicable
    return {
        "density_kg_m3": None,
        "gwp_per_kg": None,
        "embodied_carbon_a1_a3": None,
        "carbon_comment": "Material-specific carbon factors excluded due to composite or specialized scope."
    }
