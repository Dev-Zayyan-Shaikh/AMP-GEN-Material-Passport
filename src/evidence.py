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
        # Create a placeholder image if PDF file is not available
        img = Image.new("RGB", (600, 150), color=(241, 245, 249))
        draw = ImageDraw.Draw(img)
        draw.text((20, 60), f"PDF Page {page_num} Region Crop [Demo Mode]", fill=(30, 41, 59))
        return img
        
    try:
        doc = fitz.open(pdf_path)
        page_idx = max(0, min(page_num - 1, len(doc) - 1))
        page = doc.load_page(page_idx)
        
        # Default bounding box if none provided
        if not bbox or len(bbox) < 4:
            bbox = [100, 50, 250, 550]
            
        ymin, xmin, ymax, xmax = bbox
        
        # Convert page to pixmap
        scale = dpi / 72.0
        rect = fitz.Rect(xmin, ymin, xmax, ymax)
        
        # Clip page to bounding box rect with padding
        clip_rect = fitz.Rect(
            max(0, xmin - 10),
            max(0, ymin - 10),
            min(page.rect.width, xmax + 10),
            min(page.rect.height, ymax + 10)
        )
        
        pix = page.get_pixmap(dpi=dpi, clip=clip_rect)
        crop_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return crop_img
    except Exception as e:
        print(f"[Evidence Engine] Error cropping page {page_num}: {e}")
        img = Image.new("RGB", (600, 150), color=(248, 250, 252))
        draw = ImageDraw.Draw(img)
        draw.text((20, 60), f"Page {page_num} Crop Preview (Demo)", fill=(100, 116, 139))
        return img
