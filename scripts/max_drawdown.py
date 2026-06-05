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
    ].copy()

    df = df.sort_values("date")

    running_max = df["nav"].cummax()

    drawdown = (
        df["nav"] /
        running_max - 1
    )

    worst_idx = drawdown.idxmin()

    results.append(
        [
            fund,
            drawdown.min(),
            df.loc[
                worst_idx,
                "date"
            ]
        ]
    )

pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown",
        "worst_date"
    ]
).to_csv(
    "reports/max_drawdown.csv",
    index=False
)

print("Done")