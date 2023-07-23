# copilot-priority

## Installing environment

Update conda
```bash
conda update -n base -c conda-forge conda
```


Create the conda environment using this file by running the following command in your terminal:
```bash
conda env create -f environment.yaml
```
This will create a new conda environment named my_env with Python 3.8, pip, pandas, and Faker installed. You can activate the environment with the command:
```bash
conda activate copilot_priority
```

To update a conda environment based on an updated environment.yaml file, you can use the following command:
```bash
conda env update --file environment.yaml --prune
```





## Running the synthetic data generation program

```bash
python generate_patients.py 100 --seed 42
```

To get help, run:
```bash 
python generate_patients.py --help
```




## Input data
patient_id, has_high_acuity, has_moderate_acuity, has_severe_disease, has_moderate_disease, needs_stabilization, has_been_triaged

## Prompt

Using DataClasees, write a program to represent hospitals and patients. There are four floors that represent how risky the patient is. The fourth floor is most risky and contains ICU beds, the third floor is less risky with operating rooms, the second floor is less risky than the fourth or third floor and contains hospital beds, and the first floor is the least risky and contains the ER department waiting area for patients who haven't been triaged yet. The level of risk of a patient determines which floor they go to and all must eventually be processed out of the first floor and end up in the second, third, or fourth floor. Create a queue for patients being brought in by ambulance to the emergency room department and let the user specify how many people are initially in the queue. The patients in the waiting area come in with certain variables in a dataset, such as has_high_acuity, has_moderate_acuity, has_severe_disease, has_moderate_disease, needs_stabilization, current_clinical_risk, and has_been_triaged. There needs to be a hierarchy of priorities that the ER doctor can change before triaging all patients in the queue. Keep track of how many patients shift by comparing their new triaged_risk variable (High, Moderate, Low) against their current_clinical_risk (High, Moderate, Low, missing). If they are not the same, that means the shifting count needs to be incremented. There are some constraints in this program that need to be optional for the user to supply, such as shifting_limits that say the maximum number of patients who can receive a triaged_risk that is different from their current_clinical_risk. Other constraints are that the has_high_acuity patients must be triaged as High risk no matter what and the has_moderate_acuity patients must be triaged as Moderate risk no matter what unless they have has_high_acuity too. One last constraint is that the user needs to be able to supply optional target percentages that specify the percentage of patients in the queue that can end up in each floor of the hospital after triage based on their triaged_risk level. The hierarchy needs to be configurable by the user such that the user can change the priority for a given rule to be assessed and the program must enqueue the patients according to those priorities and triage those patients in their order in the queue while following the constraints.

