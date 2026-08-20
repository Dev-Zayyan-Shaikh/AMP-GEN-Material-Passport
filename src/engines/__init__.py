"""
Extraction Engines Package for BoQ Material Passport AI Platform.
Supports OCR (EasyOCR/PyMuPDF), OpenAI Vision, and Gemini Vision engines.
"""

from .ocr_engine import extract_with_ocr
from .openai_engine import extract_with_openai
from .gemini_engine import extract_with_gemini

__all__ = ["extract_with_ocr", "extract_with_openai", "extract_with_gemini"]
