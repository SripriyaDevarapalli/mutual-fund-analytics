import pandas as pd
import os

files = [
"01_fund_master.csv",
"03_aum_by_fund_house.csv",
"04_monthly_sip_inflows.csv",
"05_category_inflows.csv",
"06_industry_folio_count.csv",
"09_portfolio_holdings.csv",
"10_benchmark_indices.csv"
]

for file in files:

    df = pd.read_csv(
        f"data/raw/{file}"
    )

    if "date" in df.columns:
        df["date"] = pd.to_datetime(
            df["date"]
        )

    if "month" in df.columns:
        df["month"] = pd.to_datetime(
            df["month"]
        )

    if "launch_date" in df.columns:
        df["launch_date"] = pd.to_datetime(
            df["launch_date"]
        )

    if file == "04_monthly_sip_inflows.csv":

        df["yoy_growth_pct"] = (
            df["yoy_growth_pct"]
            .fillna(0)
        )

    name = (
        file.replace(".csv", "")
        + "_clean.csv"
    )

    df.to_csv(
        f"data/processed/{name}",
        index=False
    )

    print(name)