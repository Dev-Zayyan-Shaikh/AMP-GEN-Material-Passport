"""
Consensus Engine Module for BoQ Material Passport Platform.

Performs field-by-field comparison and majority voting across extraction engines
(OCR, OpenAI, Gemini). Computes confidence scores, vote ratios, and highlights
fields requiring human review (NEEDS_REVIEW).
"""

from typing import List, Dict, Any, Tuple
from collections import Counter


def compute_consensus(engine_results: Dict[str, List[Dict[str, Any]]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Computes consensus records across multiple engine extractions.
    
    Args:
        engine_results: Dict mapping engine name ('OCR', 'OpenAI', 'Gemini') to list of canonical items.
        
    Returns:
        Tuple of (consensus_records, comparison_rows)
    """
    engine_names = list(engine_results.keys())
    if not engine_names:
        return [], []
        
    # Number of items from primary engine
    num_items = len(engine_results[engine_names[0]])
    consensus_records = []
    comparison_rows = []
    
    for idx in range(num_items):
        item_no = idx + 1
        
        # Gather candidates for this item index across active engines
        candidates = {eng: engine_results[eng][idx] for eng in engine_names if idx < len(engine_results[eng])}
        primary = candidates[engine_names[0]]
        
        # Consensus item container
        consensus_item = dict(primary)
        consensus_item["human_reviewed"] = False
        consensus_item["engine_candidates"] = {}
        
        item_has_disagreement = False
        
        # Fields to audit via consensus voting
        voting_fields = ["quantity", "unit", "material_category", "discipline", "schedule_item_code"]
        
        field_votes = {}
        for field in voting_fields:
            vals = {}
            for eng, item in candidates.items():
                v = item.get(field)
                # Normalize numeric
                if isinstance(v, (int, float)):
                    v_norm = round(float(v), 2)
                elif isinstance(v, str):
                    v_norm = v.strip().lower()
                else:
                    v_norm = str(v)
                vals[eng] = (v, v_norm)
                
            # Perform majority vote on v_norm
            counts = Counter([pair[1] for pair in vals.values()])
            most_common_norm, vote_count = counts.most_common(1)[0]
            total_engines = len(candidates)
            
            # Select raw value corresponding to most_common_norm
            consensus_val = None
            for eng, (raw, norm) in vals.items():
                if norm == most_common_norm:
                    consensus_val = raw
                    break
                    
            field_votes[field] = {
                "consensus": consensus_val,
                "vote_count": vote_count,
                "total_engines": total_engines,
                "values": {eng: raw for eng, (raw, norm) in vals.items()}
            }

            # Comparison matrix row
            ocr_val = vals.get("OCR", (None, None))[0]
            openai_val = vals.get("OpenAI", (None, None))[0]
            gemini_val = vals.get("Gemini", (None, None))[0]
            
            status = "PASS" if vote_count > 1 or total_engines == 1 else "NEEDS_REVIEW"
            if status == "NEEDS_REVIEW":
                item_has_disagreement = True
                
            comparison_rows.append({
                "boq_item_no": item_no,
                "field": field,
                "OCR": ocr_val,
                "OpenAI": openai_val,
                "Gemini": gemini_val,
                "consensus": consensus_val,
                "vote_ratio": f"{vote_count}/{total_engines}",
                "status": status,
                "page_number": primary.get("page_number", 1),
                "source_bbox": primary.get("source_bbox", [100, 50, 200, 550])
            })

            # Update consensus record field
            consensus_item[field] = consensus_val

        # Overall item confidence determination
        qty_vote = field_votes["quantity"]["vote_count"]
        cat_vote = field_votes["material_category"]["vote_count"]
        tot = len(candidates)
        
        if tot == 1:
            confidence = "HIGH" if primary.get("confidence", 0.95) >= 0.9 else "MEDIUM"
            item_status = "PASS"
        elif qty_vote == tot and cat_vote == tot:
            confidence = "HIGH"
            item_status = "PASS"
        elif qty_vote >= 2 or cat_vote >= 2:
            confidence = "MEDIUM"
            item_status = "PASS" if not item_has_disagreement else "NEEDS_REVIEW"
        else:
            confidence = "LOW / NEEDS REVIEW"
            item_status = "NEEDS_REVIEW"
            
        consensus_item["confidence_level"] = confidence
        consensus_item["status"] = item_status
        consensus_item["field_votes"] = field_votes
        
        consensus_records.append(consensus_item)
        
    return consensus_records, comparison_rows
