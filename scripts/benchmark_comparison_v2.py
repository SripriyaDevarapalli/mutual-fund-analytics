import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Top 5 Funds
# -----------------------------

scorecard = pd.read_csv(
    "reports/fund_scorecard.csv"
)

top_funds = (
    scorecard
    .sort_values("score", ascending=False)
    .head(5)["amfi_code"]
    .tolist()
)

# -----------------------------
# Load NAV Data
# -----------------------------

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

# Last 3 years only
latest_date = nav["date"].max()

start_date = (
    latest_date -
    pd.DateOffset(years=3)
)

nav = nav[
    nav["date"] >= start_date
]

# -----------------------------
# Load Benchmark Data
# -----------------------------

benchmark = pd.read_csv(
    "data/processed/10_benchmark_indices_clean.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark[
    benchmark["date"] >= start_date
]

# -----------------------------
# Create Chart
# -----------------------------

plt.figure(figsize=(14,8))

# Plot Top 5 Funds
for fund in top_funds:

    df = nav[
        nav["amfi_code"] == fund
    ].copy()

    df = df.sort_values("date")

    # Normalize to 100
    df["normalized"] = (
        df["nav"] /
        df["nav"].iloc[0]
    ) * 100

    plt.plot(
        df["date"],
        df["normalized"],
        label=f"Fund {fund}"
    )

# Plot Nifty 50
nifty50 = benchmark[
    benchmark["index_name"]
    .str.contains(
        "Nifty 50",
        case=False,
        na=False
    )
].copy()

if len(nifty50) > 0:

    nifty50 = nifty50.sort_values("date")

    nifty50["normalized"] = (
        nifty50["close_value"] /
        nifty50["close_value"].iloc[0]
    ) * 100

    plt.plot(
        nifty50["date"],
        nifty50["normalized"],
        linewidth=3,
        label="Nifty 50"
    )

# Plot Nifty 100
nifty100 = benchmark[
    benchmark["index_name"]
    .str.contains(
        "Nifty 100",
        case=False,
        na=False
    )
].copy()

if len(nifty100) > 0:

    nifty100 = nifty100.sort_values("date")

    nifty100["normalized"] = (
        nifty100["close_value"] /
        nifty100["close_value"].iloc[0]
    ) * 100

    plt.plot(
        nifty100["date"],
        nifty100["normalized"],
        linewidth=3,
        label="Nifty 100"
    )

plt.title(
    "Top 5 Funds vs Nifty 50 & Nifty 100 (3 Years)"
)

plt.xlabel("Date")
plt.ylabel("Normalized Growth (Base = 100)")
plt.legend()
plt.grid(True)

plt.savefig(
    "reports/benchmark_comparison_v2.png",
    bbox_inches="tight"
)

plt.show()

print(
    "Saved -> reports/benchmark_comparison_v2.png"
)