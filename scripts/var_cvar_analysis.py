import pandas as pd
import numpy as np

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

results = []

for scheme in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == scheme
    ].copy()

    df = df.sort_values("date")

    returns = df["nav"].pct_change().dropna()

    if len(returns) < 30:
        continue

    var95 = np.percentile(
        returns,
        5
    )

    cvar95 = returns[
        returns <= var95
    ].mean()

    results.append(
        [
            scheme,
            var95,
            cvar95
        ]
    )

result_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)

result_df.to_csv(
    "reports/var_cvar_report.csv",
    index=False
)

print(result_df.head())