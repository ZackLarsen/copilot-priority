"""
triage_patients.py

This script takes a dataset of patients and enqueues them, 
defines a hierarchy to enforce, and then triages them.
"""

from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
from pprint import pprint

import pandas as pd

from priority_classes import Hospital, Patient


# Define inputs here

risk_hierarchy = {
    "has_high_acuity": 1,
    "has_moderate_acuity": 2,
    "has_severe_disease": 3,
    "has_moderate_disease": 4
}

risk_change_limit = 100

risk_level_percentages = {
    "High": 0.1,
    "Moderate": 0.3,
    "Low": 0.6
}


# Load data here and summarize it

print('*'*50, '\n'*2, 'Patient data summary:', '\n'*2, '*'*50)

patient_data = pd.read_parquet('data/patients.parquet', 
                               columns=['current_clinical_risk', 'has_high_acuity', 'has_moderate_acuity', 'has_severe_disease', 'has_moderate_disease'])

print(patient_data['current_clinical_risk'].value_counts(dropna=False, normalize=True))

print(patient_data[['has_high_acuity', 'has_moderate_acuity', 'has_severe_disease', 'has_moderate_disease']].sum())

print('*'*50, '\n'*2, 'Enqueuing patients from dataset:', '\n'*2, '*'*50)

def create_patients_from_parquet(file_path: str) -> list[Patient]:
    df = pd.read_parquet(file_path)
    patients = [Patient(**row.to_dict()) for _, row in df.iterrows()]
    return patients

patients = create_patients_from_parquet("data/patients.parquet")

print(f"# of patients to triage: {len(patients)}", '\n'*2)



# Enqueue patients here using the risk_hierarchy by 
# calling the put method on the patient_priority_queue
# and assigning the minimum risk value as the priority
# if the patient has a value of True for that risk

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

patient_priority_queue = PriorityQueue(
    maxsize=len(patients)
)

for patient in patients:
    patient_priorities = [max(risk_hierarchy.values())+1] # This is a hack to ensure that patients with no risk factors are triaged last
    for risk in risk_hierarchy:
        if getattr(patient, risk) == True:
            patient_priorities.append(risk_hierarchy[risk])
    patient_priority_queue.put(PrioritizedItem(min(patient_priorities), patient))


# print(patient_priority_queue.get())




# Triage patients here

hospital = Hospital()

while not patient_priority_queue.empty():
    patient = patient_priority_queue.get()
    hospital.triage_patient(patient.item)


# Summarize results here
print("# Patients in operating rooms:", len([patient.patient_id for patient in hospital.operating_rooms]))
print("# Patients in private rooms:", len([patient.patient_id for patient in hospital.private_rooms]))
print("# Patients in waiting area:", len([patient.patient_id for patient in hospital.waiting_area]))
