
from pathlib import Path

import pandas as pd


def investigate_dataset(file_path: str | Path) -> None:
    """Investigate duplicate patterns and experimental outcomes."""

    file_path = Path(file_path)
    df = pd.read_csv(file_path)

    print("\n========== DUPLICATE INVESTIGATION ==========")

    # Count rows that have an identical earlier row.
    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows: {duplicate_count}")
    print(
        f"Duplicate percentage: "
        f"{duplicate_count / len(df) * 100:.2f}%"
    )

    # Number of unique row patterns.
    unique_rows = len(df.drop_duplicates())

    print(f"Unique row patterns: {unique_rows}")

    # Check whether duplicate patterns occur across groups.
    duplicate_mask = df.duplicated(keep=False)
    duplicate_records = df.loc[duplicate_mask]

    print("\nDuplicate records by experiment group:")
    print(duplicate_records["segment"].value_counts())

    # Inspect repeated patterns by treatment group.
    print("\n========== TREATMENT OUTCOME ANALYSIS ==========")

    group_summary = (
        df.groupby("segment")
        .agg(
            customers=("conversion", "size"),
            conversions=("conversion", "sum"),
            conversion_rate=("conversion", "mean"),
            visits=("visit", "sum"),
            visit_rate=("visit", "mean"),
            total_spend=("spend", "sum"),
            average_spend=("spend", "mean"),
        )
    )

    print(group_summary.to_string())

    # Examine the relationship between conversion and spending.
    print("\n========== CONVERSION AND SPENDING ==========")

    print(
        df.groupby("conversion")
        .agg(
            customers=("spend", "size"),
            average_spend=("spend", "mean"),
            total_spend=("spend", "sum"),
            median_spend=("spend", "median"),
        )
    )

    # Check logical outcome relationships.
    print("\n========== OUTCOME CONSISTENCY ==========")

    print(
        "Conversions without a website visit:",
        ((df["conversion"] == 1) & (df["visit"] == 0)).sum(),
    )

    print(
        "Non-conversions with positive spending:",
        ((df["conversion"] == 0) & (df["spend"] > 0)).sum(),
    )

    print(
        "Conversions with zero spending:",
        ((df["conversion"] == 1) & (df["spend"] == 0)).sum(),
    )


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]

    dataset_path = (
        project_root / "data" / "raw" / "hillstrom.csv"
    )

    investigate_dataset(dataset_path)
