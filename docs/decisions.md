# Technical Decision Log

## Project: Marketing Uplift Modeling and Experiment Analysis

This document records important technical, statistical, architectural and business decisions made during project development.

Decisions may be updated as new evidence becomes available.

---

## TD-001: Dataset Selection

**Status:** Proposed

**Decision:** Use the Hillstrom Email Marketing Dataset.

**Context:**

Uplift modeling requires experimental data containing treatment assignment and observed outcomes.

The Hillstrom dataset provides customer-level observations from an email marketing experiment with treatment and control groups.

**Alternatives considered:**

- Synthetic marketing datasets.
- Observational customer transaction datasets.
- Other randomized marketing experiments.

**Reason for selection:**

The dataset provides a suitable starting point for learning randomized experiment analysis and uplift modeling.

**Trade-offs and limitations:**

- Historical experimental data may not represent current customer behavior.
- The original experiment's population and intervention may limit generalization.
- Dataset availability and field definitions must be verified before implementation.

---

## TD-002: Initial Treatment and Control Definition

**Status:** Proposed

**Decision:**

- Treatment: Mens E-Mail.
- Control: No E-Mail.
- Womens E-Mail: Excluded from the initial binary-treatment analysis.

**Context:**

The initial project will investigate the causal effect of one specific marketing intervention.

**Reason for selection:**

A binary treatment-control design simplifies the initial statistical analysis and model implementation.

**Trade-offs:**

The initial analysis will not estimate the effects of the Womens E-Mail intervention.

---

## TD-003: Outcome Variable Selection

**Status:** Proposed

**Decision:**

- Primary outcome: Conversion.
- Secondary outcome: Spending.

**Context:**

Marketing effectiveness should be measured through customer response as well as financial outcomes.

**Reason for selection:**

Conversion supports binary treatment-effect estimation, while spending enables additional business impact analysis.

**Validation required:**

Verify the definitions, units, distributions and relationship between conversion and spending during data exploration.

---

## TD-004: Programming Language

**Status:** Accepted

**Decision:** Python 3.11.

**Reason:**

Python provides a mature ecosystem for machine learning, statistical analysis, causal inference, data engineering and API development.

**Alternatives considered:**

- R.
- Julia.

**Trade-off:**

Python provides broad engineering and deployment support, while R offers particularly strong statistical analysis capabilities.

---

## TD-005: Machine Learning Framework

**Status:** Proposed

**Decision:** Use Scikit-learn for preprocessing and baseline machine learning models.

Explore CausalML and EconML for uplift modeling and causal effect estimation.

**Reason:**

These libraries provide reusable components for model development and causal machine learning.

**Validation required:**

Compare supported estimators, API compatibility, maintenance status and evaluation functionality before final dependency selection.

---

## TD-006: Model Evaluation Strategy

**Status:** Proposed

**Decision:** Evaluate uplift models using:

- AUUC.
- Qini coefficient.
- Uplift at K.
- Incremental conversions.
- Incremental revenue and profit.

**Reason:**

Traditional classification metrics alone do not measure the quality of treatment-effect ranking.

**Additional consideration:**

Use experimental holdout data and appropriate uncertainty estimation when evaluating model-driven targeting policies.

---

## TD-007: Application Architecture

**Status:** Proposed

**Decision:**

- FastAPI for model inference.
- Streamlit for the interactive application.
- Docker for reproducible deployment.
- MLflow for experiment tracking.
- Pytest for automated testing.

**Reason:**

This separation allows model development, serving, user interaction and testing to evolve independently.

---

## TD-008: Version Control

**Status:** Accepted

**Decision:** Git and GitHub.

**Reason:**

Version control supports collaboration, change tracking, reproducibility and portfolio presentation.

**Data policy:**

Raw customer-level data should not be committed to the public repository unless its licensing and redistribution permissions explicitly allow it.

---

## TD-009: Development Methodology

**Status:** Accepted

**Decision:** Iterative, phase-based development.

**Reason:**

Each development phase must have:

1. Defined objectives.
2. Documented technical decisions.
3. Implementation tasks.
4. Validation procedures.
5. Review and approval.

The next phase begins only after the current phase meets its acceptance criteria.

---

## Decision Review Policy

Technical decisions are not permanent simply because they have been documented.

They should be reconsidered when:

- New data becomes available.
- Experimental assumptions are invalidated.
- A technical limitation is discovered.
- A better alternative is identified.
- Business requirements change.

Every significant change should be documented with its rationale and consequences.
