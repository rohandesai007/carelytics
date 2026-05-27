# Auto-generated analytics helper - 2026-05-27
# Carelytics - Healthcare Analytics Platform

import datetime
import statistics
from typing import List, Dict, Optional

MODULE_VERSION = "2.0.3"
GENERATED_DATE = "2026-05-27"

def calculate_patient_risk_score(vitals: Dict[str, float]) -> float:
    """
    Calculate a normalized patient risk score from vital signs.
    Returns a score between 0.0 (low risk) and 1.0 (high risk).
    """
    score = 0.0
    weights = {
        "heart_rate": 0.25,
        "blood_pressure_systolic": 0.30,
        "oxygen_saturation": 0.25,
        "temperature": 0.20
    }
    thresholds = {
        "heart_rate": (60, 100),
        "blood_pressure_systolic": (90, 140),
        "oxygen_saturation": (95, 100),
        "temperature": (97.0, 99.5)
    }
    for key, weight in weights.items():
        if key in vitals:
            low, high = thresholds[key]
            val = vitals[key]
            if val < low or val > high:
                score += weight
    return round(min(score, 1.0), 4)

def aggregate_metrics(data: List[float]) -> Dict[str, float]:
    """Aggregate a list of numeric health metrics."""
    if not data:
        return {}
    return {
        "mean": round(statistics.mean(data), 4),
        "median": round(statistics.median(data), 4),
        "stdev": round(statistics.stdev(data), 4) if len(data) > 1 else 0.0,
        "min": min(data),
        "max": max(data),
        "count": len(data)
    }

def format_report_timestamp() -> str:
    """Return a formatted timestamp for analytics reports."""
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

if __name__ == "__main__":
    sample_vitals = {
        "heart_rate": 88.0,
        "blood_pressure_systolic": 135.0,
        "oxygen_saturation": 97.0,
        "temperature": 98.6
    }
    print(f"Risk Score: {calculate_patient_risk_score(sample_vitals)}")
    print(f"Report Time: {format_report_timestamp()}")
