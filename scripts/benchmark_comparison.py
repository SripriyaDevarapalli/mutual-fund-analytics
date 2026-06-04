import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

funds = (
    nav["amfi_code"]
    .unique()[:5]
)

plt.figure(
    figsize=(12,6)
)

for fund in funds:

    df = nav[
        nav["amfi_code"]
        == fund
    ]

    plt.plot(
        df["date"],
        df["nav"],
        label=str(fund)
    )

plt.legend()

plt.title(
    "Top Funds Benchmark Comparison"
)

plt.savefig(
    "reports/benchmark_comparison.png"
)

print("Chart saved")