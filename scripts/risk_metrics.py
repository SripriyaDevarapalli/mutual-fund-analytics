import pandas as pd
import numpy as np

RF = 0.065

nav = pd.read_csv(
    "reports/daily_returns.csv"
)

results = []

for fund in nav[
    "amfi_code"
].unique():

    df = nav[
        nav["amfi_code"] == fund
    ]

    r = df["daily_return"]

    annual_return = (
        r.mean() * 252
    )

    annual_std = (
        r.std() * np.sqrt(252)
    )

    sharpe = (
        (annual_return - RF)
        / annual_std
    )

    downside = r[
        r < 0
    ]

    downside_std = (
        downside.std()
        * np.sqrt(252)
    )

    sortino = (
        (annual_return - RF)
        / downside_std
    )

    results.append(
        [
            fund,
            sharpe,
            sortino
        ]
    )

result_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "Sharpe",
        "Sortino"
    ]
)

result_df.to_csv(
    "reports/risk_metrics.csv",
    index=False
)

print(
    result_df.sort_values(
        "Sharpe",
        ascending=False
    ).head()
)