import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = sorted(
    [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]
)

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 70)
    print(f"FILE: {file}")

    path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(path)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\n")