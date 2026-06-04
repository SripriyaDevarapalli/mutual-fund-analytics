import pandas as pd

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = pd.read_csv(
    "reports/risk_metrics.csv"
)

alpha = pd.read_csv(
    "reports/alpha_beta.csv"
)

dd = pd.read_csv(
    "reports/max_drawdown.csv"
)

df = (
    perf.merge(
        risk,
        on="amfi_code"
    )
    .merge(
        alpha,
        on="amfi_code"
    )
    .merge(
        dd,
        on="amfi_code"
    )
)

df["score"] = (
      0.30 * df["return_3yr_pct"].rank(pct=True)
    + 0.25 * df["Sharpe"].rank(pct=True)
    + 0.20 * df["Alpha"].rank(pct=True)
    + 0.15 * (
        1 -
        df["expense_ratio_pct"]
        .rank(pct=True)
      )
    + 0.10 * (
        1 -
        df["max_drawdown"]
        .rank(pct=True)
      )
) * 100

df = df.sort_values(
    "score",
    ascending=False
)

df.to_csv(
    "reports/fund_scorecard.csv",
    index=False
)

print(
    df[
    [
    "scheme_name",
    "score"
    ]
    ].head()
)