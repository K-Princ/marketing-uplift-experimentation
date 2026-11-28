# Data Dictionary — Hillstrom Email Marketing Dataset

## Dataset overview

| Property | Value |
|---|---|
| Dataset | Hillstrom Email Marketing Dataset |
| Observations | 64,000 |
| Features/columns | 12 |
| Experiment groups | Mens E-Mail, No E-Mail, Womens E-Mail |
| Primary outcome | `conversion` |
| Secondary outcomes | `visit`, `spend` |
| Raw file | `data/raw/hillstrom.csv` |
| Raw file policy | Do not commit the raw dataset to Git |

## Column definitions

| Column | Observed type | Provisional description | Notes |
|---|---|---|---|
| `recency` | Integer | Recency-related customer attribute | Exact unit and reference period to verify |
| `history_segment` | String | Categorical customer purchase-history segment | Seven observed categories |
| `history` | Float | Numeric customer purchase-history measure | Exact definition and currency to verify |
| `mens` | Integer | Binary indicator associated with mens merchandise | Values observed: 0 and 1 |
| `womens` | Integer | Binary indicator associated with womens merchandise | Values observed: 0 and 1 |
| `zip_code` | String | Customer geographic category | Values include `Surburban`, `Urban`, `Rural`; preserve raw spelling |
| `newbie` | Integer | Binary indicator associated with customer status | Exact definition to verify |
| `channel` | String | Customer channel category | Web, Phone, Multichannel |
| `segment` | String | Assigned email experiment group | Mens E-Mail, No E-Mail, Womens E-Mail |
| `visit` | Integer | Website visit outcome indicator | Values observed: 0 and 1 |
| `conversion` | Integer | Purchase/conversion outcome indicator | Primary project outcome; values observed: 0 and 1 |
| `spend` | Float | Recorded customer spending outcome | Zero for non-converters in this dataset |

## Experiment group definitions

| Raw segment value | Initial project role |
|---|---|
| `Mens E-Mail` | Treatment (`T = 1`) |
| `No E-Mail` | Control (`T = 0`) |
| `Womens E-Mail` | Excluded from the initial binary comparison |

The initial experiment compares Mens E-Mail with No E-Mail. The Womens E-Mail group is retained in the raw dataset but excluded from this first comparison.

## Initial observed outcome summary

| Group | Customers | Visits | Visit rate | Conversions | Conversion rate | Total spend |
|---|---:|---:|---:|---:|---:|---:|
| Mens E-Mail | 21,307 | 3,894 | 18.276% | 267 | 1.253% | $30,311.69 |
| No E-Mail | 21,306 | 2,262 | 10.617% | 122 | 0.573% | $13,908.33 |
| Womens E-Mail | 21,387 | 3,238 | 15.140% | 189 | 0.884% | $23,038.11 |

These are descriptive statistics, not yet final causal estimates.

## Data quality observations

- 64,000 rows and 12 columns.
- No missing values were observed.
- 6,562 rows were identified as exact full-row duplicates using `DataFrame.duplicated()`.
- No customer ID is present in the inspected columns; duplicate rows cannot be assumed to represent duplicate customers.
- No duplicate rows will be removed without further evidence.
- `Surburban` is the observed raw spelling. Do not silently change it in the raw data.
- `visit`, `conversion`, `mens`, `womens`, and `newbie` are represented as integer columns with binary values.
- All observed conversions had a website visit and positive spending.
- All observed non-conversions had zero spending.

## Documentation caveat

Descriptions marked provisional are inferred from column names or observed values. Verify exact definitions, units, timing, and experiment assignment details against the original dataset documentation before treating them as authoritative.
