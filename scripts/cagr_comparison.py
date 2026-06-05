import pandas as pd
import numpy as np

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

results = []

for fund in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == fund
    ].sort_values("date")

    latest_date = df["date"].max()

    row = {
        "amfi_code": fund
    }

    for years in [1, 3, 5]:

        start_date = (
            latest_date -
            pd.DateOffset(years=years)
        )

        subset = df[
            df["date"] >= start_date
        ]

        if len(subset) > 10:

            start_nav = subset.iloc[0]["nav"]
            end_nav = subset.iloc[-1]["nav"]

            cagr = (
                (end_nav/start_nav)
                ** (1/years)
                - 1
            )

            row[f"CAGR_{years}Y"] = cagr

        else:
            row[f"CAGR_{years}Y"] = np.nan

    results.append(row)

pd.DataFrame(results).to_csv(
    "reports/cagr_comparison.csv",
    index=False
)

print("Saved cagr_comparison.csv")