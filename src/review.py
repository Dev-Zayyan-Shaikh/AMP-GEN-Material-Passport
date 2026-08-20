"""
Human Review Queue Module for BoQ Material Passport Platform.

Provides review queue filtering, candidate value inspection, human field override,
and dataset updates with human_reviewed=true audit tracking.
"""

from typing import List, Dict, Any


def get_review_queue(consensus_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Returns list of items requiring human review (NEEDS_REVIEW status or low confidence).
    """
    queue = []
    for item in consensus_records:
        status = item.get("status", "")
        conf = item.get("confidence_level", "")
        reviewed = item.get("human_reviewed", False)
        
        if (status == "NEEDS_REVIEW" or "NEEDS REVIEW" in conf) and not reviewed:
            queue.append(item)
    return queue


def apply_human_override(
    consensus_records: List[Dict[str, Any]],
    item_no: int,
    field_updates: Dict[str, Any],
    reviewer_notes: str = ""
) -> List[Dict[str, Any]]:
    """
    Applies human reviewer override to a specific BoQ item, updating canonical values
    and marking human_reviewed = True.
    """
    updated_records = []
    for item in consensus_records:
        rec = dict(item)
        if rec.get("boq_item_no") == item_no:
            for field, val in field_updates.items():
                rec[field] = val
            rec["human_reviewed"] = True
            rec["status"] = "PASS (Human Verified)"
            rec["confidence_level"] = "HIGH (Human Reviewed)"
            if reviewer_notes:
                old_comment = rec.get("comment") or ""
                rec["comment"] = f"{old_comment} [Human Reviewer Note: {reviewer_notes}]".strip()
        updated_records.append(rec)
    return updated_records
