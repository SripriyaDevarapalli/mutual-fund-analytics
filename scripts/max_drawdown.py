import pandas as pd

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

results = []

for fund in nav[
    "amfi_code"
].unique():

    df = nav[
        nav["amfi_code"] == fund
    ].copy()

    running_max = (
        df["nav"]
        .cummax()
    )

    drawdown = (
        df["nav"]
        / running_max
        - 1
    )

    mdd = drawdown.min()

    results.append(
        [
            fund,
            mdd
        ]
    )

pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
).to_csv(
    "reports/max_drawdown.csv",
    index=False
)

print("Done")