# Carelytics – Healthcare Data Analytics Library

[![PyPI Version](https://img.shields.io/pypi/v/carelytics?color=blue&label=PyPI%20Version)](https://pypi.org/project/carelytics/)
[![Downloads](https://img.shields.io/pypi/dm/carelytics?color=brightgreen&label=Downloads)](https://pypistats.org/packages/carelytics)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)

*A modular Python package for healthcare data cleaning, validation, interoperability, and revenue cycle insights.*

---

## Overview

**Carelytics** is a Python library designed to simplify **data analytics, interoperability, and automation in the healthcare domain**, especially focusing on **Revenue Cycle Management (RCM)** and **FHIR-based data exchange**.

It provides functions to:

* Validate and clean large healthcare datasets  
* Analyze patient encounters, lab data, and vitals  
* Map and export data to FHIR-compliant JSON bundles  
* Perform semantic and integrity checks on healthcare resources  
* Support predictive modeling such as readmission and denial prediction  

Built with **Pandas**, **NumPy**, and **Scikit-learn**, Carelytics empowers analysts, researchers, and developers to derive actionable insights from healthcare data quickly and securely.

---

## Compliance & Data Privacy

* Carelytics adheres to key data governance principles:
* PHI de-identification and masking via `carelytics.utils.deid`
* HIPAA-friendly workflows for analytics and interoperability
* Strict handling of schema validation to ensure secure data exchange


## Package Architecture

```
carelytics/
│
├── data/                     # (Placeholder for sample data or CSVs)
│
├── fhir/                     # Handles healthcare interoperability (FHIR parsing)
│   ├── parser.py             # Parse and normalize HL7/FHIR data
│   ├── validator.py          # Validate resource structure and schema
│   ├── fhir_mapper.py        # NEW: Map raw data to FHIR-compliant JSON
│   └── fhir_analyzer.py      # NEW: Analyze FHIR bundles for data quality & insights
│
├── models/                   # Predictive models for healthcare analytics
│   ├── denial_prediction.py
│   └── readmission.py
│
├── utils/                    # Utility functions for data processing
│   ├── cleaner.py
│   ├── deid.py               # De-identification utilities for PHI data
│   ├── validator.py          # Schema and datatype validation
│   └── __init__.py
│
├── claims.py                 # Claim-level metrics and KPIs
├── encounter.py              # Patient encounter analytics
├── lab.py                    # Lab result standardization
├── patient.py                # Patient-level summaries
└── vitals.py                 # Vital signs normalization and aggregation
```

Each module is reusable and can be independently imported.

---

## ⚙️ Core Functionalities

### 1. `carelytics.utils.validator`
Performs schema and datatype validation for healthcare datasets.

```python
from carelytics.utils.validator import validate_columns, validate_datatypes

validate_columns(df, ["patient_id", "age", "diagnosis"])
validate_datatypes(df, {"age": "int64", "diagnosis": "object"})
```

---

### 2. `carelytics.utils.cleaner`
Includes data cleaning utilities such as missing value handling, normalization, and column renaming.

```python
from carelytics.utils.cleaner import fill_missing

df = fill_missing(df, strategy="median")
```

---

### 3. `carelytics.models.denial_prediction`
Predicts claim denial probabilities based on payer data, CPT/ICD codes, and historical denials.

```python
from carelytics.models.denial_prediction import predict_denials
pred = predict_denials(df)
print(pred.head())
```

---

### 4. `carelytics.models.readmission`
Predicts hospital readmission likelihood using patient demographics and vitals.

---

### 5. `carelytics.fhir.fhir_mapper`
Maps raw hospital or claims data to **FHIR-compliant JSON** resources such as `Patient`, `Observation`, and `Claim`.  
This enables seamless interoperability with healthcare systems.

```python
from carelytics.fhir.fhir_mapper import FHIRMapper

mapper = FHIRMapper()
patient = mapper.map_patient({
    "patient_id": "P123",
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "birth_date": "1980-03-10"
})
observation = mapper.map_observation({
    "observation_id": "O1",
    "patient_id": "P123",
    "value": 98.6,
    "unit": "°F"
})
mapper.export_bundle([patient], [observation])
```

---

### 6. `carelytics.fhir.fhir_analyzer`
Analyzes FHIR bundles for **data quality, missing attributes, and statistical summaries**.  
Helps verify completeness and correctness of clinical or claims data.

```python
from carelytics.fhir.fhir_analyzer import FHIRAnalyzer

analyzer = FHIRAnalyzer("fhir_bundle.json")
analyzer.generate_report()
```

---

### 7. `carelytics.claims`
Analyzes RCM metrics such as:

* Average AR days  
* Net collection rate  
* Denial rates  

---

### 8. `carelytics.lab` & `carelytics.vitals`
Standardizes and normalizes lab values and patient vitals for analysis.

---

### 9. `carelytics.utils.deid`
Supports data anonymization to remove or mask PHI (Protected Health Information) before analysis.

---

## Example Workflow

```python
import pandas as pd
from carelytics.utils import validator, cleaner
from carelytics.models import denial_prediction
from carelytics.fhir import FHIRMapper, FHIRAnalyzer

# Load your healthcare dataset
df = pd.read_csv("claims.csv")

# Validate structure
validator.validate_columns(df, ["claim_id", "payer", "amount", "denial_flag"])

# Clean and prepare
df = cleaner.fill_missing(df, "median")

# Run prediction
pred = denial_prediction.predict_denials(df)

# Map data to FHIR and analyze
mapper = FHIRMapper()
patient = mapper.map_patient({"patient_id": "P123", "first_name": "John", "last_name": "Doe", "gender": "male"})
obs = mapper.map_observation({"observation_id": "O1", "patient_id": "P123", "value": 98.7, "unit": "°F"})
mapper.export_bundle([patient], [obs])

analyzer = FHIRAnalyzer("fhir_bundle.json")
analyzer.generate_report()
```

---

## Key Use Cases

| Use Case | Description |
| --------- | ------------ |
| Hospital Analytics | Clean and validate EHR data for performance dashboards |
| RCM Optimization | Predict denials, track collection efficiency |
| Clinical Research | Analyze patient lab results and vitals |
| Data Interoperability | Map to FHIR standards for data exchange |
| FHIR Quality Auditing | Detect missing fields and summarize resource quality |
| PHI Handling | Built-in de-identification for HIPAA compliance |

---

## Dependencies

* Python ≥ 3.7  
* pandas  
* numpy  
* scikit-learn  

Install all dependencies with:

```bash
pip install carelytics
```

---

## Authors & Contributors

**Rohan Desai**  
Dallas, Texas, USA  
Email: [rohan.acme@gmail.com](mailto:rohan.acme@gmail.com)  
GitHub: [https://github.com/rohan-desai](https://github.com/rohan-desai)  
LinkedIn: [https://www.linkedin.com/in/rohandesai07/](https://www.linkedin.com/in/rohandesai07/)  

**Vaishnavi Gadve**  
Irving, Texas, USA  
Email: [vaishnavigadve143@gmail.com](mailto:vaishnavigadve143@gmail.com)  
GitHub: [https://github.com/vaish2412](https://github.com/vaish2412)  
LinkedIn: [https://www.linkedin.com/in/vaishnavi-gadve-4b577512a/](https://www.linkedin.com/in/vaishnavi-gadve-4b577512a/)  

---

## 🧪 License

MIT License  
© 2025 Rohan Desai & Vaishnavi Sanjay Gadve

