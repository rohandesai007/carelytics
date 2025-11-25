"""
encounter.py
-------------
Functions for analyzing patient encounters and admissions data.
Useful for LOS, visit trends, and encounter counts.
"""

import pandas as pd
import numpy as np


class EncounterFrame(pd.DataFrame):
    """Extension of Pandas DataFrame for encounter-level analytics."""

    _metadata = ["encounter_id"]

    @property
    def _constructor(self):
        return EncounterFrame

    def total_encounters(self):
        """Returns the total number of encounters."""
        total = len(self)
        print(f"🧾 Total encounters: {total}")
        return total
        
#Adding new code - code under review/testing
    def encounters_per_patient(self):
        """Returns average number of encounters per patient."""
        if "patient_id" in self.columns:
            avg = self.groupby("patient_id")["encounter_id"].nunique().mean()
            print(f"👥 Avg encounters per patient: {avg:.2f}")
            return avg
        else:
            raise ValueError("patient_id column required.")
            
#Adding new code - code under review/testing
    def average_length_of_stay(self):
        """Calculates mean LOS for encounters."""
        if {"admit_date", "discharge_date"}.issubset(self.columns):
            los = (self["discharge_date"] - self["admit_date"]).dt.days
            mean_los = los.mean()
            print(f"🏨 Average length of stay: {mean_los:.1f} days")
            return mean_los
        else:
            raise ValueError("admit_date and discharge_date columns required.")
