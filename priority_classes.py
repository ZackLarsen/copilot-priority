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
    has_been_triaged: bool = False
    triaged_risk: Optional[RiskLevel] = None

class Hospital:
    def __init__(self):
        self.operating_rooms = []
        self.private_rooms = []
        self.waiting_area = []
        self.waiting_patients = []

    def triage_patient(self, patient: Patient):
        if patient.has_severe_disease:
            self.operating_rooms.append(patient)
        elif patient.has_moderate_disease:
            self.private_rooms.append(patient)
        elif len(self.operating_rooms) < 10:
            self.operating_rooms.append(patient)
        elif len(self.private_rooms) < 25:
            self.private_rooms.append(patient)
        elif len(self.waiting_area) < 50:
            self.waiting_area.append(patient)
        else:
            self.waiting_patients.append(patient)

    def process_patients(self, patients: List[Patient]):
        for patient in patients:
            self.triage_patient(patient)
