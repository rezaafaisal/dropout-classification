import pandas as pd


df = pd.read_csv("cleaned.csv")

curricular_units_2nd_sem_approved = df["Curricular_units_2nd_sem_approved"].unique()
curricular_units_1st_sem_approved = df["Curricular_units_1st_sem_approved"].unique()
tuition_fees_up_to_date = df["Tuition_fees_up_to_date"].unique()
scholarship_holder = df["Scholarship_holder"].unique()
curricular_units_2nd_sem_enrolled = df["Curricular_units_2nd_sem_enrolled"].unique()
curricular_units_2nd_sem_evaluations = df["Curricular_units_2nd_sem_evaluations"].unique()
curricular_units_1st_sem_enrolled = df["Curricular_units_1st_sem_enrolled"].unique()
displaced = df["Displaced"].unique()