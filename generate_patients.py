"""
generate_patients.py

This script generates a fake dataset of patients for
the priority triage system.

Using numpy.random.choice, we can generate a random like so:

"has_high_acuity": np.random.choice([True, False], p=[0.1, 0.9]),
"has_moderate_acuity": np.random.choice([True, False], p=[0.2, 0.8]),
"has_severe_disease": np.random.choice([True, False], p=[0.05, 0.95]),
"has_moderate_disease": np.random.choice([True, False], p=[0.15, 0.85]),
"""

import click
import pandas as pd
import random
from faker import Faker
from typing import Optional

@click.command()
@click.argument('n', type=int)
@click.option('--seed', default=None, type=int, help='Random seed for reproducibility')
def create_patient_dataframe(n: int, seed: Optional[int]):
    faker = Faker()
    Faker.seed(seed)
    random.seed(seed)

    patient_data = {
        "patient_name": [faker.name() for _ in range(n)],
        "patient_id": [faker.unique.random_number(digits=9, fix_len=True) for _ in range(n)],
        "patient_age": [faker.random_int(min=1, max=100) for _ in range(n)],
        "patient_gender": [faker.random_element(elements=('Male', 'Female')) for _ in range(n)],
        "current_clinical_risk": [faker.random_element(elements=('High', 'Moderate', 'Low', '')) for _ in range(n)],
        "has_high_acuity": [faker.boolean(chance_of_getting_true=10) for _ in range(n)],
        "has_moderate_acuity": [faker.boolean(chance_of_getting_true=25) for _ in range(n)],
        "has_severe_disease": [faker.boolean(chance_of_getting_true=10) for _ in range(n)],
        "has_moderate_disease": [faker.boolean(chance_of_getting_true=25) for _ in range(n)],
        "needs_stabilization": [faker.boolean(chance_of_getting_true=25) for _ in range(n)],
    }

    df = pd.DataFrame(patient_data)
    df.to_parquet("data/patients.parquet", index=False)
    
    # Here we are writing out as a deltaleake file:
    df.to_parquet("data/patients.delta", index=False)

if __name__ == "__main__":
    create_patient_dataframe()