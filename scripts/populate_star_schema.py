import pandas as pd
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

# -------------------
# DIM FUND
# -------------------

fund = pd.read_csv(
    "data/processed/01_fund_master_clean.csv"
)

dim_fund = fund[
[
"amfi_code",
"fund_house",
"scheme_name",
"category",
"sub_category",
"plan",
"risk_category"
]
]

dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="append",
    index=False
)

# -------------------
# DIM DATE
# -------------------

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

dates = pd.DataFrame(
{
    "full_date":
    nav["date"].unique()
}
)

dates["full_date"] = pd.to_datetime(
    dates["full_date"]
)

dates["year"] = dates["full_date"].dt.year
dates["month"] = dates["full_date"].dt.month
dates["quarter"] = dates["full_date"].dt.quarter

dates.to_sql(
    "dim_date",
    conn,
    if_exists="append",
    index=False
)

# -------------------
# FACT NAV
# -------------------

fact_nav = nav.rename(
    columns={"date":"full_date"}
)

fact_nav.to_sql(
    "fact_nav",
    conn,
    if_exists="append",
    index=False
)

# -------------------
# FACT TRANSACTIONS
# -------------------

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

txn[
[
"investor_id",
"amfi_code",
"transaction_date",
"transaction_type",
"amount_inr",
"state",
"city",
"kyc_status"
]
].to_sql(
    "fact_transactions",
    conn,
    if_exists="append",
    index=False
)

# -------------------
# FACT PERFORMANCE
# -------------------

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

perf[
[
"amfi_code",
"return_1yr_pct",
"return_3yr_pct",
"return_5yr_pct",
"expense_ratio_pct",
"alpha",
"beta",
"sharpe_ratio"
]
].to_sql(
    "fact_performance",
    conn,
    if_exists="append",
    index=False
)

# -------------------
# FACT AUM
# -------------------

aum = pd.read_csv(
    "data/processed/03_aum_by_fund_house_clean.csv"
)

aum = aum.rename(
    columns={"date":"full_date"}
)

aum[
[
"fund_house",
"full_date",
"aum_crore",
"num_schemes"
]
].to_sql(
    "fact_aum",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print("Star schema populated successfully")