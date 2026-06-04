import pandas as pd

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

first_year = (
    txn.groupby("investor_id")
    ["transaction_date"]
    .min()
    .dt.year
)

txn["cohort"] = txn["investor_id"].map(
    first_year
)

summary = []

for cohort in sorted(
    txn["cohort"].unique()
):

    cohort_df = txn[
        txn["cohort"] == cohort
    ]

    avg_amount = (
        cohort_df["amount_inr"]
        .mean()
    )

    total_invested = (
        cohort_df["amount_inr"]
        .sum()
    )

    top_fund = (
        cohort_df["amfi_code"]
        .value_counts()
        .idxmax()
    )

    summary.append(
        [
            cohort,
            avg_amount,
            total_invested,
            top_fund
        ]
    )

result = pd.DataFrame(
    summary,
    columns=[
        "cohort",
        "avg_amount",
        "total_invested",
        "top_fund_preference"
    ]
)

print(result)

result.to_csv(
    "reports/cohort_analysis.csv",
    index=False
)