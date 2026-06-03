import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

folder = "data/processed"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        table_name = (
            file.replace(".csv", "")
        )

        df = pd.read_csv(
            os.path.join(folder, file)
        )

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(
            f"Loaded {table_name}"
        )

print("\nAll cleaned tables loaded.")