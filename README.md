# AMP-GEN Material Passport — Multi-Engine AI Platform

> **AMP-GEN AI/ML Technical Challenge & Platform**  
> Supported by the Google Centre for Climate Technology via Manthan, Office of the Principal Scientific Adviser to the Government of India.

A multi-engine, defensible Python data extraction and Digital Material Passport AI platform built from a scanned 13-page Bill of Quantities (BoQ) for **Central Building Research Institute (CBRI), Roorkee (Principal's Residence — Schedule "A")**.

---

## 🚀 Quick Start (< 5 Minutes)

### 1. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Dev-Zayyan-Shaikh/AMP-GEN-Material-Passport.git
cd AMP-GEN-Material-Passport
pip install -r requirements.txt
```

### 2. Environment Setup (Optional for Live Vision APIs)
Create a `.env` file in the root directory (or use Streamlit Secrets):
```env
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```
*Note: If no API keys are provided, the platform operates seamlessly in **Demo Mode** using persistent pre-cached first-iteration extractions.*

### 3. Launch Interactive Streamlit Web Platform
```bash
streamlit run app.py
```
Open `http://localhost:8501` to access the full multi-engine platform!

### 4. Run Core Pipeline & Validation Suite
```bash
python src/main.py
python src/validate.py
```

---

## 📂 Repository Structure

```text
AMP-GEN-Material-Passport/
├── app.py                      # Interactive Streamlit Web Platform
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules protecting secrets & bytecode
├── input/
│   ├── AMP_Passport_Template.xlsx            # Master 50-column Excel template
│   └── BoQ_CBRI_Principals_Residence.pdf      # Target 13-page BoQ PDF scan
├── output/
│   ├── passport_filled.xlsx                  # Populated 50-column Excel deliverable
│   ├── passport.json                         # Valid JSON dataset (64 records)
│   ├── visualization.png                     # Material category bar chart
│   ├── building_meta.json                    # Extracted Page 1 building metadata
│   └── Presentation_Script_Material_Passport_AI.pdf # Executive 2.5-min PDF presentation
├── scratch/
│   ├── consensus_cache.json                  # First iteration consensus cache
│   ├── openai_cache.json                     # OpenAI candidate extractions
│   ├── gemini_cache.json                     # Gemini candidate extractions
│   └── comparison_cache.json                 # 320-row field comparison matrix
└── src/
    ├── extract.py                            # PDF extraction & 64 item parsing
    ├── normalize.py                          # Unit normalization & dimension handling
    ├── classify.py                           # Material taxonomy & discipline classification
    ├── carbon.py                             # Embodied carbon (A1-A3) & ICE v3.0 mapping
    ├── consensus.py                          # Field-by-field 3-way voting engine
    ├── evidence.py                           # PyMuPDF 300 DPI PDF crop engine
    ├── review.py                             # Human review queue & override handler
    ├── export.py                             # OpenPyXL & JSON output exporter
    ├── visualize.py                          # Dark-themed chart generator
    ├── validate.py                           # Automated validation suite (14 rules)
    ├── main.py                               # Pipeline entrypoint
    └── engines/
        ├── __init__.py
        ├── ocr_engine.py                     # Primary PyMuPDF + EasyOCR engine
        ├── openai_engine.py                  # Live OpenAI Vision engine (gpt-4o)
        └── gemini_engine.py                  # Live Gemini Vision engine (gemini-2.5-flash)
```

---

## 📊 Platform Features & Capabilities

```text
SCANNED PDF ➔ MULTI-ENGINE VISION (OCR + OpenAI + Gemini) ➔ 3-WAY CONSENSUS VOTING
  ➔ BBOX EVIDENCE CROPPING ➔ HUMAN REVIEW QUEUE ➔ CARBON ANALYTICS (40.693 t) ➔ EXCEL + JSON
```

### 1. Multi-Engine Extraction Architecture (`src/engines/`)
* **OCR Engine**: PyMuPDF + EasyOCR baseline extracting spatial bounding boxes (`source_bbox`).
* **OpenAI Vision Engine**: Live `gpt-4o` Vision model handler with prompt engineering for scanned tables.
* **Gemini Vision Engine**: Live `gemini-2.5-flash` Vision model handler with prompt engineering for handwriting.

### 2. 3-Way Majority Voting Consensus (`src/consensus.py`)
Normalizes field values and computes vote ratios (`3/3`, `2/3`, `1/3`). Styled in Tab 2 with 3-state color coding:
* 🟢 **Light Green (`#DCFCE7`)**: 3/3 Full Agreement across all engines.
* 🟡 **Light Yellow (`#FEF9C3`)**: 2/3 Majority Vote consensus.
* 🔴 **Light Red (`#FEE2E2`)**: Disagreement / Needs Human Review.

### 3. Source Evidence BBox Cropping (`src/evidence.py`)
Renders high-resolution 300 DPI PDF page crops cut directly from the scanned document, allowing instant visual verification of item numbers, descriptions, and quantities.

### 4. Human Review Queue (`src/review.py`)
Enables engineers to review flagged items, inspect crop evidence side-by-side with candidate extractions, edit fields, add reviewer audit notes, and mark records `human_reviewed = true`.

### 5. Cradle-to-Gate Embodied Carbon Analytics (`src/carbon.py`)
Calculates embodied carbon ($A1\text{--}A3$) using **ICE Database v3.0** factors—locked at **`40.693 t`** (**`40,693.01 kg CO₂e`**) across 44 material-bearing structural items.

---

## ✅ Automated Validation Suite (`src/validate.py`)

Run `python src/validate.py` to execute all 14 programmatic assertions:
1. Deliverable files exist and are non-empty.
2. JSON parses cleanly with exactly 64 records.
3. Item numbers are contiguous 1 through 64.
4. Zero missing item numbers.
5. Zero duplicate item numbers.
6. All 64 records have valid deterministic GMAP IDs (`AMP-GEN-001`..`AMP-GEN-064`).
7. Original units strictly follow normalized conventions (`cum`, `sqm`, `m`, `kg`, `nos`).
8. Special Case: Item 24 ($3.5 \times 10\text{ dm}^3$) correctly converted to $0.035\text{ m}^3$ (`cum`).
9. Excel `passport_filled.xlsx` opens cleanly via OpenPyXL with 50 columns.
10. Excel sheet contains all 64 populated BoQ records in exact alignment.
11. Building metadata `output/building_meta.json` is complete and valid.
12. Out-of-scope grey columns remain strictly blank per instructions.
13. Carbon Bonus B2 verified with cited material sources (`40.693 t`).
14. Visualization chart `output/visualization.png` generated and verified.

---

## 🎙️ Executive Presentation & PDF

* 📝 **Approach & Methodology**: [`APPROACH.md`](APPROACH.md)

---

## 🛠️ Git Workflow & Deployment

* **Remote Repository**: `https://github.com/Dev-Zayyan-Shaikh/AMP-GEN-Material-Passport`
* **Branch Mapping**: Local `master` pushes to remote `main`:
```bash
git add .
git commit -m "feat: platform updates"
git push origin master:main
```
