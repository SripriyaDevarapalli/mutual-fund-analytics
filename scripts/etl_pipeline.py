import os

print("STEP 1 - Data Ingestion")
os.system("python scripts/data_ingestion.py")

print("STEP 2 - NAV Fetch")
os.system("python scripts/live_nav_fetch.py")

print("STEP 3 - Cleaning")
os.system("python scripts/clean_nav_history.py")
os.system("python scripts/clean_transactions.py")
os.system("python scripts/clean_scheme_performance.py")

print("STEP 4 - Database Load")
os.system("python scripts/load_cleaned_to_sqlite.py")

print("ETL PIPELINE COMPLETED")