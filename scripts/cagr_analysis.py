import pandas as pd

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

    start_nav = df.iloc[0]["nav"]
    end_nav = df.iloc[-1]["nav"]

    years = (
        (df.iloc[-1]["date"] -
         df.iloc[0]["date"]).days
        / 365
    )

    cagr = (
        (end_nav/start_nav)
        ** (1/years)
        - 1
    )

    results.append(
        [fund,cagr]
    )

cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "CAGR"
    ]
)

cagr_df.to_csv(
    "reports/cagr_report.csv",
    index=False
)

print(cagr_df.head())