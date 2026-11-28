
from pathlib import Path

import pandas as pd


# Expected columns based on the documented Hillstrom dataset.
EXPECTED_COLUMNS = [
    "recency",
    "history_segment",
    "history",
    "mens",
    "womens",
    "zip_code",
    "newbie",
    "channel",
    "segment",
    "visit",
    "conversion",
    "spend",
]


def inspect_dataset(file_path: str | Path) -> pd.DataFrame:
    """
    Load and inspect the raw Hillstrom dataset.

    This function does not modify the original CSV.

    Args:
        file_path: Path to the raw CSV file.

    Returns:
        Loaded pandas DataFrame.
    """
    file_path = Path(file_path)

    # 1. Check whether the file exists.
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    if file_path.stat().st_size == 0:
        raise ValueError("Dataset file is empty.")

    # 2. Load dataset.
    df = pd.read_csv(file_path)

    print("\n========== DATASET OVERVIEW ==========")

    # 3. Dataset dimensions.
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    # 4. Column names.
    print("\n========== COLUMN NAMES ==========")
    print(df.columns.tolist())

    # 5. Data types.
    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    # 6. Missing values.
    print("\n========== MISSING VALUES ==========")
    missing = df.isnull().sum()

    print(missing)
    print(f"Total missing values: {missing.sum()}")

    # 7. Duplicate records.
    print("\n========== DUPLICATE RECORDS ==========")
    print(f"Duplicate rows: {df.duplicated().sum()}")

    # 8. Numerical statistics.
    print("\n========== NUMERICAL SUMMARY ==========")
    print(df.describe().T)

    # 9. Categorical distributions.
    print("\n========== CATEGORICAL DISTRIBUTIONS ==========")

    for column in df.select_dtypes(
    include=["str", "object", "category", "bool"]
    ).columns:
        print(f"\n{column}:")
        print(df[column].value_counts(dropna=False))

    # 10. Verify expected schema.
    print("\n========== SCHEMA CHECK ==========")

    missing_columns = set(EXPECTED_COLUMNS) - set(df.columns)
    unexpected_columns = set(df.columns) - set(EXPECTED_COLUMNS)

    print(f"Missing expected columns: {sorted(missing_columns)}")
    print(f"Unexpected columns: {sorted(unexpected_columns)}")

    if not missing_columns and not unexpected_columns:
        print("Schema matches the documented 12-column schema.")
    else:
        print("Schema differs from the documented schema.")

    # 11. Experiment group distribution.
    if "segment" in df.columns:
        print("\n========== EXPERIMENT GROUP DISTRIBUTION ==========")
        print(df["segment"].value_counts(dropna=False))

    # 12. Outcome distributions.
    for column in ["visit", "conversion"]:
        if column in df.columns:
            print(f"\n========== {column.upper()} DISTRIBUTION ==========")
            print(df[column].value_counts(dropna=False))

    if "spend" in df.columns:
        print("\n========== SPENDING SUMMARY ==========")
        print(df["spend"].describe())

    print("\n========== INSPECTION COMPLETED ==========\n")

    return df


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]

    dataset_path = (
        project_root / "data" / "raw" / "hillstrom.csv"
    )

    inspect_dataset(dataset_path)
