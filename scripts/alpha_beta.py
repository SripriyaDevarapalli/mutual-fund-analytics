import pandas as pd
from scipy.stats import linregress

nav = pd.read_csv(
    "reports/daily_returns.csv"
)

# FIX
nav["date"] = pd.to_datetime(
    nav["date"]
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
        "Nifty",
        case=False,
        na=False
    )
]

benchmark = benchmark.sort_values(
    "date"
)

benchmark["benchmark_return"] = (
    benchmark["close_value"]
    .pct_change()
)

results = []

for fund in nav["amfi_code"].unique():

    fund_df = nav[
        nav["amfi_code"] == fund
    ]

    merged = pd.merge(
        fund_df,
        benchmark[
            ["date",
             "benchmark_return"]
        ],
        on="date",
        how="inner"
    ).dropna()

    if len(merged) < 50:
        continue

    reg = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )

    beta = reg.slope

    alpha = (
        reg.intercept * 252
    )

    results.append(
        [
            fund,
            alpha,
            beta
        ]
    )

result_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "Alpha",
        "Beta"
    ]
)

result_df.to_csv(
    "reports/alpha_beta.csv",
    index=False
)

print(result_df.head())
print(
    f"\nFunds analyzed: {len(result_df)}"
)