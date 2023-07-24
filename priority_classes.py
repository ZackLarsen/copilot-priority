"""
priority_classes.py

This class implements a priority triage system for a hospital.
It is based on the following rules:

"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class RiskLevel(Enum):
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"

@dataclass
class Patient:
    patient_name: str
    patient_id: int
    patient_age: int
    patient_gender: str
    current_clinical_risk: Optional[str]
    has_high_acuity: bool
    has_moderate_acuity: bool
    has_severe_disease: bool
    has_moderate_disease: bool
    needs_stabilization: bool
    has_been_triaged: bool = False
    triaged_risk: Optional[RiskLevel] = None

class Hospital:
    def __init__(self):
        self.icu_beds = []
        self.operating_rooms = []
        self.private_rooms = []
        self.waiting_area = []
        self.exceptions = [
            "needs_stabilization",
            "has_been_triaged"
        ]
        self.risk_change_count = 0

    def triage_patient(self, patient: Patient):
        """
        This method triages a patient based on the 
        dynamic risk level hierarchy

        This function needs to allow for deterministic 
        rules that can be changed by the hospital as well
        as exceptions to the rules that remove a patient
        from the queue and place them in a specific location
        """
        if patient.has_high_acuity:
            patient.triaged_risk = RiskLevel.HIGH
            patient.has_been_triaged = True
            if patient.current_clinical_risk != "High":
                self.risk_change_count += 1
        elif patient.has_moderate_acuity:
            patient.triaged_risk = RiskLevel.MODERATE
            patient.has_been_triaged = True
            if patient.current_clinical_risk != "Moderate":
                self.risk_change_count += 1
        else:
            if patient.needs_stabilization:
                patient.triaged_risk = patient.current_clinical_risk
                patient.has_been_triaged = True
            # At this point, once we have gone through the high and moderate acuity patients,
            # and we have removed the patients that need stabilization, we can now
            # triage the patients based on the risk level hierarchy.
            # We need to check which priority level of the hierarchy the patient is in
            # so that we can enforce the shifting limits and target percentages at the
            # correct stage.

            # Check if the current priority level is higher than 
            # the priority level of the shifting limits and target percentages

            #else:
                #break
                # elif patient.has_severe_disease:
                #     self.operating_rooms.append(patient)
                # elif patient.has_moderate_disease:
                #     self.private_rooms.append(patient)
                # elif len(self.operating_rooms) < 10:
                #     self.operating_rooms.append(patient)
                # elif len(self.private_rooms) < 25:
                #     self.private_rooms.append(patient)
                # elif len(self.waiting_area) < 50:
                #     self.waiting_area.append(patient)
                # else:
                #     self.waiting_area.append(patient)

    def process_patients(self, patients: List[Patient]):
        for patient in patients:
            self.triage_patient(patient)
