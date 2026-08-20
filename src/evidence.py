"""
Source Evidence Cropping Module for BoQ Material Passport Platform.

Renders high-resolution PDF pages using PyMuPDF and extracts precise bounding-box
crop regions corresponding to extracted BoQ line items for visual verification.
"""

import os
import fitz  # PyMuPDF
from PIL import Image, ImageDraw
import io
from typing import Tuple, Optional, Union


def get_crop_image(
    pdf_path: str = "input/BoQ_CBRI_Principals_Residence.pdf",
    page_num: int = 2,
    bbox: list = None,
    dpi: int = 150
) -> Optional[Image.Image]:
    """
    Extracts and crops the specified bounding box region from a PDF page.
    Returns PIL Image object.
    """
    abs_path = os.path.abspath(pdf_path)
    if not os.path.exists(abs_path):
        # Check fallback to relative input directory
        abs_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "input", "BoQ_CBRI_Principals_Residence.pdf"))
        
    if not os.path.exists(abs_path):
        img = Image.new("RGB", (600, 150), color=(241, 245, 249))
        draw = ImageDraw.Draw(img)
        draw.text((20, 60), f"PDF File Not Found: {pdf_path}", fill=(220, 38, 38))
        return img
        
    try:
        try:
            p_int = int(float(page_num))
        except (ValueError, TypeError):
            p_int = 2
            
        doc = fitz.open(abs_path)
        page_idx = max(0, min(p_int - 1, len(doc) - 1))
        page = doc.load_page(page_idx)
        
        if not bbox or not isinstance(bbox, (list, tuple)) or len(bbox) < 4:
            bbox = [50, 20, 150, 590]
            
        try:
            ymin, xmin, ymax, xmax = [float(b) for b in bbox[:4]]
        except Exception:
            ymin, xmin, ymax, xmax = 50.0, 20.0, 150.0, 590.0

        page_w = float(page.rect.width)
        page_h = float(page.rect.height)

        # Apply generous padding so item text is never clipped at top/bottom/sides
        clip_xmin = max(0.0, xmin - 15.0)
        clip_ymin = max(0.0, ymin - 18.0)
        clip_xmax = min(page_w, xmax + 15.0)
        clip_ymax = min(page_h, ymax + 18.0)
        
        clip_rect = fitz.Rect(clip_xmin, clip_ymin, clip_xmax, clip_ymax)


        
        pix = page.get_pixmap(dpi=dpi, clip=clip_rect)
        crop_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return crop_img
    except Exception as e:
        print(f"[Evidence Engine] Error cropping page {page_num}: {e}")
        img = Image.new("RGB", (600, 150), color=(248, 250, 252))
        draw = ImageDraw.Draw(img)
        draw.text((20, 60), f"Page {page_num} Region Crop Preview", fill=(100, 116, 139))
        return img


def get_crop_bytes(
    pdf_path: str = "input/BoQ_CBRI_Principals_Residence.pdf",
    page_num: int = 2,
    bbox: list = None,
    dpi: int = 150
) -> bytes:
    """
    Extracts and crops specified bounding box region, returning raw PNG bytes
    for 100% reliable rendering in Streamlit Cloud.
    """
    img = get_crop_image(pdf_path, page_num, bbox, dpi)
    if img:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()
    return b""
