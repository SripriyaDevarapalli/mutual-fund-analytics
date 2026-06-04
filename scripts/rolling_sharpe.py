import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

funds = nav["amfi_code"].unique()[:5]

plt.figure(figsize=(12,6))

for fund in funds:

    df = nav[
        nav["amfi_code"] == fund
    ].copy()

    df = df.sort_values("date")

    returns = df["nav"].pct_change()

    sharpe = (
        returns
        .rolling(90)
        .mean()
        /
        returns
        .rolling(90)
        .std()
    ) * np.sqrt(252)

    plt.plot(
        df["date"],
        sharpe,
        label=str(fund)
    )

plt.legend()

plt.title(
    "Rolling 90-Day Sharpe Ratio"
)

plt.savefig(
    "reports/rolling_sharpe_chart.png"
)

print("Chart saved")