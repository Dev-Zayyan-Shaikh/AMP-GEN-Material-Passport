# AMP-GEN Material Passport Pipeline

> **AMP-GEN AI/ML Intern Technical Assignment**  
> Supported by the Google Centre for Climate Technology via Manthan, Office of the Principal Scientific Adviser to the Government of India.

A reproducible, defensible Python data extraction and material passport pipeline built from a scanned 13-page Bill of Quantities (BoQ) for **Central Building Research Institute (CBRI), Roorkee (Principal's Residence — Schedule "A")**.

---

## 🚀 Quick Start (< 5 Minutes)

### Prerequisites
- Python 3.10+ (Tested on Python 3.13)
- `pip` package manager

### Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/your-username/AMP-GEN-Material-Passport.git
cd AMP-GEN-Material-Passport
pip install -r requirements.txt
```

### Execution (Core Pipeline)
Run the end-to-end extraction, normalization, export, visualization, and validation pipeline:
```bash
python src/main.py
```

### Interactive Web App Dashboard (Bonus B1)
Launch the interactive Streamlit material passport dashboard locally:
```bash
streamlit run app.py
```

---

## 📂 Repository Structure

```text
AMP-GEN-Material-Passport/
├── input/
│   ├── AMP_Passport_Template.xlsx            # Original Excel template (UNTOUCHED)
│   └── BoQ_CBRI_Principals_Residence.pdf      # Original scanned BoQ PDF (UNTOUCHED)
├── output/
│   ├── passport_filled.xlsx                  # Populated 50-column Excel Material Passport
│   ├── passport.json                         # Valid JSON dataset (64 records)
│   ├── visualization.png                     # Material category bar chart
│   └── building_meta.json                    # Extracted Page 1 building metadata
├── src/
│   ├── extract.py                            # PDF extraction & 64 item parsing
│   ├── normalize.py                          # Unit normalization & dimension handling
│   ├── classify.py                           # Material taxonomy & discipline classification
│   ├── carbon.py                             # Embodied carbon (A1-A3) & ICE v3.0 mapping
│   ├── export.py                             # OpenPyXL & JSON output exporter
│   ├── visualize.py                          # Matplotlib chart generator
│   ├── validate.py                           # Automated validation suite (14 rules)
│   └── main.py                               # Pipeline entrypoint
├── app.py                                    # Interactive Streamlit Web App (Bonus B1)
├── APPROACH.md                               # 1-page methodology & technical reflection
├── README.md                                 # Project documentation & quickstart
└── requirements.txt                          # Python dependencies list
```

---

## 📊 Pipeline Architecture & Deliverables

```text
SCANNED PDF ➔ OCR / VISION EXTRACTION ➔ STRUCTURED PARSING ➔ VALIDATION ➔ EXCEL + JSON ➔ STREAMLIT DASHBOARD
```

| Output File | Description | Status |
| :--- | :--- | :---: |
| `output/passport_filled.xlsx` | 50-column Excel sheet populated for all 64 BoQ items preserving template structure | ✅ Complete |
| `output/passport.json` | Clean JSON export with 64 records and deterministic GMAP IDs (`AMP-GEN-001` .. `064`) | ✅ Complete |
| `output/visualization.png` | Building-level Material Category distribution bar chart | ✅ Complete |
| `output/building_meta.json` | Extracted Page 1 metadata (Plinth Area, Foundation Depth, Seismic Zone, etc.) | ✅ Complete |
| `app.py` | Interactive Streamlit Web Application for dataset exploration & carbon analytics | ✅ Complete |

---

## ✅ Automated Validation Suite

The pipeline automatically runs 14 programmatic assertions upon execution:
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
12. Out-of-scope grey columns remain strictly blank per template rules.
13. Carbon Bonus B2 verified with cited material sources.
14. Visualization chart `output/visualization.png` generated and verified.

---

## 🎁 Bonuses Completed

1. **Bonus B1 — Interactive Dashboard App**: Built with `Streamlit` & `Plotly` (`app.py`), enabling multi-parameter filtering, item searching, Plotly carbon graphs, building metadata viewer, and single-click Excel/JSON downloads.
2. **Bonus B2 — Mass & Carbon**: Populated Density, GWP/kg, and Embodied Carbon A1-A3 ($\text{kg CO}_2\text{e}$) for 43 material-bearing items with cited sources (ICE Database v3.0 / Indian LCA literature) in `Comment`.
3. **Bonus B3 — Building Metadata**: Extracted from Page 1 into `output/building_meta.json`.
4. **Bonus B4 — Walkthrough Video Script**: Detailed 3-minute video presentation checklist and transcript below.

---

## 🎬 Bonus B4: Walkthrough Presentation Script & Checklist

### 3-Minute Video Structure

- **0:00 - 0:45: Project Overview & Extraction Pipeline**
  - Show the scanned 13-page CBRI Principal's Residence BoQ PDF.
  - Explain the 64-item extraction strategy combining EasyOCR, PyMuPDF, and visual validation of handwritten quantities.
  - Highlight special continuation handling across pages (Items 14, 26, 32, 45, 50, 55).

- **0:45 - 1:30: Unit Normalization & Data Integrity**
  - Demonstrate unit normalization to standard set (`cum`, `sqm`, `m`, `kg`, `nos`).
  - Explain Item 24 special case: $3.5 \times 10\text{ dm}^3 \rightarrow 0.035\text{ m}^3$ (`cum`).
  - Show deterministic GMAP IDs (`AMP-GEN-001` to `AMP-GEN-064`).

- **1:30 - 2:15: Material Passport Outputs & Streamlit Dashboard**
  - Open `output/passport_filled.xlsx` in Excel showing all 50 columns populated starting at row 7.
  - Show `app.py` Streamlit dashboard with interactive Plotly carbon charts and live filters.
  - Point out Embodied Carbon A1-A3 values with ICE Database v3.0 citations in `Comment`.

- **2:15 - 3:00: Visualization & Programmatic Validation**
  - Display `output/visualization.png` showing the distribution of items by Material Category.
  - Run `python src/main.py` in the terminal to demonstrate all 14 programmatic validation checks passing cleanly in real-time.

---

## 🛠️ Tools & Disclosures

- **Tools Used**: Python 3.13, EasyOCR, PyMuPDF, OpenPyXL, Matplotlib, Streamlit, Plotly, OpenCV, Git.
- **LLM / AI Disclosure**: Generative AI assistants were used for pair programming, regex architecture design, and carbon factor mapping. All source extractions were visually validated against original PDF page scans.
- **Honest Hours-Spent Estimate**: ~5.5 hours total (Phase 1 discovery & setup: 0.5h, Phase 2 extraction & visual OCR verification: 2h, Phase 3 schema, normalization & validation: 1.5h, Phase 4 visualization & carbon bonus: 0.5h, Phase 5 Streamlit web app & documentation: 1h).

---

## ⚠️ Known Limitations & Out-of-Scope Items
- **Grey Columns**: Circularity, detachability, and lifespan columns are left blank per instructions as they require specialist domain training.
- **Labor/Earthwork**: Earthwork and excavation items are marked `[EXCLUDED]` for material carbon as they represent pure machinery/labour services.
