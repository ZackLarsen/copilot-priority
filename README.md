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
- patient_id
- current_clinical_risk
- has_high_acuity
- has_moderate_acuity
- has_severe_disease
- has_moderate_disease
- needs_stabilization
- has_been_triaged

## input hierarchy

Add numeric priorities to each indicator variable. The lower the number, the higher the priority. The triage_patients.py script will use this hierarchy to determine the priority of each patient. If the patient doesn't have any of the supplied indicators, they will be assigned a priority of one higher than the highest priority in the hierarchy. For example, if the highest priority is 3, and the patient doesn't have any of the indicators, they will be assigned a priority of 4.

```python
risk_hierarchy = {
    "has_high_acuity": 1,
    "has_moderate_acuity": 2,
    "has_severe_disease": 3,
    "has_moderate_disease": 4
}
```