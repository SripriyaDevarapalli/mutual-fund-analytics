import pandas as pd

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

txn = txn[
    txn["transaction_type"]
    == "Sip"
]

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

results = []

for inv, group in txn.groupby(
    "investor_id"
):

    if len(group) < 6:
        continue

    group = group.sort_values(
        "transaction_date"
    )

    gaps = (
        group["transaction_date"]
        .diff()
        .dt.days
        .dropna()
    )

    avg_gap = gaps.mean()

    status = (
        "At-Risk"
        if avg_gap > 35
        else "Healthy"
    )

    results.append(
        [
            inv,
            avg_gap,
            status
        ]
    )

pd.DataFrame(
    results,
    columns=[
        "investor_id",
        "avg_gap",
        "status"
    ]
).to_csv(
    "reports/sip_continuity.csv",
    index=False
)

print("Done")