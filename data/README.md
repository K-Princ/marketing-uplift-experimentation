# Data Documentation

## 1. Project Dataset

**Dataset Name:** Hillstrom Email Marketing Dataset

**Domain:** E-commerce Marketing

**Dataset Type:** Randomized Marketing Experiment

**Purpose:** Analyze the incremental impact of email marketing campaigns using statistical experiment analysis and uplift modeling.

## 2. Dataset Description

The Hillstrom dataset contains customer-level observations from an email marketing experiment.

The experiment includes three groups:

- Mens E-Mail
- Womens E-Mail
- No E-Mail (Control)

For the initial project implementation, we will use:

- Treatment group: Mens E-Mail
- Control group: No E-Mail
- Excluded group: Womens E-Mail

## 3. Target Variables

| Variable | Description | Role |
|---|---|---|
| Conversion | Whether a customer made a purchase | Primary outcome |
| Spending | Customer spending | Secondary outcome |
| Segment | Marketing treatment assignment | Treatment indicator |

Actual column names, data types, units and definitions must be verified against the downloaded dataset before implementation.

## 4. Data Directory Structure

```text
data/
│
├── raw/
│   └── Original downloaded dataset
│
├── processed/
│   └── Cleaned and transformed datasets
│
└── README.md
```

### Raw Data

Contains original downloaded data.

Rules:

- Never modify original files directly.
- Preserve the original dataset.
- Document the source and acquisition date.
- Validate file integrity before processing.

### Processed Data

Contains datasets generated through preprocessing and feature engineering.

Rules:

- Processed data must be reproducible.
- Document transformation steps.
- Avoid overwriting raw data.
- Maintain consistent data schemas.

## 5. Data Acquisition

The dataset source, download procedure, licensing information and redistribution permissions will be verified during Phase 1.

No dataset should be committed to the public repository until its licensing and data-sharing permissions have been checked.

## 6. Data Quality Requirements

The dataset will be checked for:

- Missing values.
- Duplicate records.
- Invalid data types.
- Unexpected categorical values.
- Invalid treatment assignments.
- Invalid outcome values.
- Inconsistent numerical values.
- Potential data leakage.

## 7. Data Handling Policy

- Do not commit sensitive customer information.
- Do not expose personally identifiable information.
- Keep large datasets outside Git where appropriate.
- Use `.gitignore` for local data files.
- Document dataset versions and processing procedures.

## 8. Reproducibility

Data processing must be reproducible using documented scripts and configurations.

The following information should be recorded:

- Dataset source.
- Acquisition date.
- Dataset version or checksum, where available.
- Processing configuration.
- Transformation logic.
- Output schema.

## 9. Current Status

**Status:** Documentation prepared; dataset not yet acquired or validated.

Dataset acquisition and detailed schema verification will be completed in Phase 1.
