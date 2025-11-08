"""
fhir/validator.py
-----------------
Validates FHIR bundles and checks for required fields or schema errors.
"""

import json


def validate_fhir_structure(bundle_path):
    """
    Validates FHIR bundle structure to ensure compliance with FHIR format.
    """
    with open(bundle_path, "r") as f:
        data = json.load(f)

    if "resourceType" not in data or data["resourceType"] != "Bundle":
        raise ValueError("Invalid FHIR bundle: missing or incorrect 'resourceType'.")

    if "entry" not in data:
        raise ValueError("Invalid FHIR bundle: missing 'entry' section.")

    print(f"✅ FHIR bundle {bundle_path} passed basic validation.")
    return True
