import pandas as pd

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

if risk.lower() == "low":

    filtered = df[
        df["risk_grade"]
        == "Low"
    ]

elif risk.lower() == "moderate":

    filtered = df[
        df["risk_grade"]
        == "Moderate"
    ]

else:

    filtered = df[
        df["risk_grade"]
        .isin(
            [
                "High",
                "Very High"
            ]
        )
    ]

recommend = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    recommend[
    [
    "scheme_name",
    "fund_house",
    "sharpe_ratio"
    ]
    ]
)