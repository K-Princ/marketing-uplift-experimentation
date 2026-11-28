
from pathlib import Path

import pandas as pd
import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "hillstrom.csv"

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

BINARY_COLUMNS = [
    "mens",
    "womens",
    "newbie",
    "visit",
    "conversion",
]

EXPECTED_SEGMENTS = {
    "Mens E-Mail",
    "No E-Mail",
    "Womens E-Mail",
}


@pytest.fixture(scope="module")
def df():
    """Load the original dataset once for this test module."""
    if not DATA_PATH.exists():
        pytest.fail(f"Dataset not found: {DATA_PATH}")

    return pd.read_csv(DATA_PATH)


def test_dataset_has_expected_shape(df):
    assert df.shape == (64000, 12)


def test_dataset_has_expected_columns(df):
    assert list(df.columns) == EXPECTED_COLUMNS


def test_dataset_has_no_missing_values(df):
    assert df.isna().sum().sum() == 0


@pytest.mark.parametrize("column", BINARY_COLUMNS)
def test_binary_columns_contain_only_zero_and_one(df, column):
    assert set(df[column].unique()).issubset({0, 1})


def test_experiment_groups_are_valid(df):
    assert set(df["segment"].unique()) == EXPECTED_SEGMENTS


def test_spending_is_non_negative(df):
    assert (df["spend"] >= 0).all()


def test_spending_is_zero_for_non_conversions(df):
    assert (df.loc[df["conversion"] == 0, "spend"] == 0).all()


def test_conversions_have_positive_spending(df):
    assert (df.loc[df["conversion"] == 1, "spend"] > 0).all()


def test_conversions_have_website_visits(df):
    assert (df.loc[df["conversion"] == 1, "visit"] == 1).all()
