# AMP-GEN Material Passport — Approach & Methodology

## 1. Tools Used & Rationale
- **PyMuPDF (`pymupdf`)**: Selected for high-fidelity PDF rasterization to 300 DPI lossless PNG page images without external binary dependencies.
- **EasyOCR & OpenCV**: Selected for robust, offline OCR text detection and bounding-box extraction across scanned typed and handwritten construction text.
- **OpenPyXL**: Selected to populate `input/AMP_Passport_Template.xlsx` directly while strictly preserving workbook styles, formulas, color-coding, and formatting.
- **Matplotlib**: Selected for generating publication-quality, clean bar charts of material category distributions (`output/visualization.png`).
- **LLMs & Antigravity AI Assistant**: Leveraged for pair-programming, regex parsing architecture, structural validation design, and carbon factor mapping.

## 2. Extraction & Vision Workflow
```text
Scanned PDF (13 Pages) ➔ 300 DPI PNG Rendering ➔ EasyOCR Bounding-Box Extraction
  ➔ Structured Parsing Engine (Item Continuation & Regex) ➔ Visual Image Verification
  ➔ Unit Normalization & Classification ➔ Carbon Mapping ➔ Excel + JSON Export ➔ Validation
```
1. **Document Analysis**: Page 1 contained project metadata; pages 1–13 contained 64 BoQ items formatted in Schedule "A".
2. **Page Continuation Handling**: Items spanning page breaks (Items 14, 26, 32, 45, 50, 55) were detected and concatenated into single unified item records before field parsing.
3. **Visual Validation**: All handwritten numbers and ambiguous DSR codes were visually cross-checked against high-res cropped page images (`scratch/item_crops/`).

## 3. Key Findings: What Worked vs. Challenges
- **What Worked**: 
  - 100% complete 64/64 item extraction with zero duplicates or missing items.
  - Page 1 building metadata extraction (`output/building_meta.json`).
  - Strict unit normalization (`cum`, `sqm`, `m`, `kg`, `nos`) and handling of Item 24 ($10\text{ dm}^3 = 0.01\text{ m}^3$).
  - Carbon Bonus B2: Citing ICE Database v3.0 and Indian LCA literature across 43 material-bearing items.
- **What Required Manual / Hybrid Validation**:
  - Handwritten quantities in scanned tables (e.g., distinguishing $14.4$ vs $14.44$, $90.6$, $1.4\times 100\text{ sqm}$).
  - Composite sub-item quantities (e.g., summing Item 16 formwork sub-items $108+17+19+1+9 = 154\text{ sqm}$, and Item 17 rebar $100+1375 = 1475\text{ kg}$).

## 4. Ambiguity Handling & Data Integrity
- **No Hallucination**: Unsupported attributes (e.g., circularity, detachability, lifespan) were strictly left blank (`None`) per instructions.
- **Preservation of Source**: Original descriptions were fully preserved without truncation; standardized taxonomy was applied separately via `Material Category` and `Classification (Matched)`.
- **Traceability**: All unit conversions and carbon assumptions are documented in the `Comment` field.

## 5. Future Enhancements (With 2 Additional Weeks)
1. **Fine-Tuned Multimodal VLM**: Fine-tune a lightweight Vision-Language Model (e.g., PaliGemma / Donut) specifically on Indian CPWD/DSR BoQ formats for direct end-to-end extraction.
2. **Automated Table Segmentation**: Implement layout analysis (LayoutLMv3) to isolate table cells before OCR to reduce line-merging noise.
3. **Madaster Detachability Pipeline**: Train a graph neural network on architectural CAD drawings to calculate circularity and detachability index scores.

---
*Disclosure: All LLMs, OCR libraries, and python utilities used in this pipeline are fully disclosed per assignment guidelines.*
