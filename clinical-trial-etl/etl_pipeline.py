import pandas as pd
import sqlite3

# Load CSVs
patients = pd.read_csv('data/patients.csv')
dosages = pd.read_csv('data/dosages.csv')
outcomes = pd.read_csv('data/outcomes.csv')

# Merge datasets
merged = patients.merge(dosages, on='patient_id').merge(outcomes, on='patient_id')

# Connect to SQLite
conn = sqlite3.connect('clinical_trials.db')
merged.to_sql('trial_data', conn, if_exists='replace', index=False)

print("ETL pipeline completed. Data loaded into SQLite.")
