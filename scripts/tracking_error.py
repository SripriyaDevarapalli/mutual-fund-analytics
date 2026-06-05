import pandas as pd
import numpy as np

returns = pd.read_csv(
    "reports/daily_returns.csv"
)

returns["date"] = pd.to_datetime(
    returns["date"]
)

benchmark = pd.read_csv(
    "data/processed/10_benchmark_indices_clean.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark[
    benchmark["index_name"]
    .str.contains(
        "Nifty 100",
        case=False,
        na=False
    )
]

benchmark["benchmark_return"] = (
    benchmark["close_value"]
    .pct_change()
)

results = []

for fund in returns[
    "amfi_code"
].unique():

    fund_df = returns[
        returns["amfi_code"] == fund
    ]

    merged = pd.merge(
        fund_df,
        benchmark[
            [
                "date",
                "benchmark_return"
            ]
        ],
        on="date"
    ).dropna()

    if len(merged) < 50:
        continue

    tracking_error = (
        (
            merged["daily_return"]
            -
            merged["benchmark_return"]
        ).std()
        * np.sqrt(252)
    )

    results.append(
        [
            fund,
            tracking_error
        ]
    )

pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "tracking_error"
    ]
).to_csv(
    "reports/tracking_error.csv",
    index=False
)

print("Done")