import pandas as pd

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

nav = nav.sort_values(
    ["amfi_code","date"]
)

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

returns = nav.dropna()

print(
    returns["daily_return"].describe()
)

returns.to_csv(
    "reports/daily_returns.csv",
    index=False
)

print("Saved daily_returns.csv")