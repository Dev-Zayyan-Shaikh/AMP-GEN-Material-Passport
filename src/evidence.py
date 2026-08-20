"""
Source Evidence Cropping Module for BoQ Material Passport Platform.

Renders high-resolution PDF pages using PyMuPDF and extracts precise bounding-box
crop regions corresponding to extracted BoQ line items for visual verification.
"""

import os
import fitz  # PyMuPDF
from PIL import Image, ImageDraw
import io
from typing import Tuple, Optional


def get_crop_image(
    pdf_path: str = "input/BoQ_CBRI_Principals_Residence.pdf",
    page_num: int = 2,
    bbox: list = None,
    dpi: int = 150
) -> Optional[Image.Image]:
    """
    Extracts and crops the specified bounding box region from a PDF page.
    
    Args:
        pdf_path: Path to the scanned PDF file.
        page_num: 1-indexed page number.
        bbox: Bounding box [ymin, xmin, ymax, xmax] in points/pixels.
        dpi: Rendering resolution DPI.
        
    Returns:
        PIL Image crop object.
    """
    if not os.path.exists(pdf_path):
        # Fallback placeholder if PDF path is missing
        img = Image.new("RGB", (600, 150), color=(241, 245, 249))
        draw = ImageDraw.Draw(img)
        draw.text((20, 60), f"PDF File Not Found: {pdf_path}", fill=(220, 38, 38))
        return img
        
    try:
        doc = fitz.open(pdf_path)
        page_idx = max(0, min(page_num - 1, len(doc) - 1))
        page = doc.load_page(page_idx)
        
        # Default bounding box if none provided
        if not bbox or len(bbox) < 4:
            bbox = [50, 20, 150, 590]
            
        ymin, xmin, ymax, xmax = bbox
        
        # Safely clamp rect coordinates to page dimensions
        page_w = page.rect.width
        page_h = page.rect.height
        
        clip_xmin = max(0.0, float(xmin) - 10.0)
        clip_ymin = max(0.0, float(ymin) - 10.0)
        clip_xmax = min(page_w, float(xmax) + 10.0)
        clip_ymax = min(page_h, float(ymax) + 10.0)
        
        clip_rect = fitz.Rect(clip_xmin, clip_ymin, clip_xmax, clip_ymax)
        
        # Render high-resolution pixmap of the clip region
        pix = page.get_pixmap(dpi=dpi, clip=clip_rect)
        crop_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return crop_img
    except Exception as e:
        print(f"[Evidence Engine] Error cropping page {page_num}: {e}")
        img = Image.new("RGB", (600, 150), color=(248, 250, 252))
        draw = ImageDraw.Draw(img)
        draw.text((20, 60), f"Page {page_num} Region Crop Preview", fill=(100, 116, 139))
        return img
