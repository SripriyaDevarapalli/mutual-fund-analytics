import pandas as pd

holdings = pd.read_csv(
    "data/processed/09_portfolio_holdings_clean.csv"
)

results = []

for scheme in holdings[
    "amfi_code"
].unique():

    df = holdings[
        holdings["amfi_code"]
        == scheme
    ]

    hhi = (
        (df["weight_pct"]/100)**2
    ).sum()

    results.append(
        [
            scheme,
            hhi
        ]
    )

pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "HHI"
    ]
).to_csv(
    "reports/sector_hhi.csv",
    index=False
)

print("Done")