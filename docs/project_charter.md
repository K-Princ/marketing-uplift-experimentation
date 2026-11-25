# Project Charter: Marketing Uplift Modeling and Experiment Analysis

## 1. Project Overview

This project aims to develop a machine learning system that estimates the incremental impact of marketing campaigns on individual customers.

The system will use causal inference and uplift modeling techniques to identify customers whose purchasing behavior is likely to change because of a marketing intervention.

## 2. Business Problem

Traditional marketing campaigns often target customers based on their probability of purchasing.

However, customers who are already likely to purchase may not need marketing incentives.

This can result in wasted marketing expenditure.

The proposed system will estimate incremental treatment effects to help marketing teams identify customers who are most likely to respond positively to a campaign.

## 3. Business Objectives

- Estimate the average treatment effect of marketing campaigns.
- Estimate conditional treatment effects across customer segments.
- Identify customers with positive estimated uplift.
- Rank customers based on estimated incremental response.
- Estimate incremental conversions and revenue.
- Compare uplift-based targeting against conventional targeting strategies.

## 4. Dataset and Experimental Design

Initial dataset: Hillstrom Email Marketing Dataset.

Initial experiment:

- Treatment group: Mens E-Mail.
- Control group: No E-Mail.
- Primary outcome: Conversion.
- Secondary outcome: Customer spending.

The Womens E-Mail group will initially be excluded from the binary-treatment experiment.

These assumptions will be verified during data acquisition and exploration.

## 5. Machine Learning Objectives

- Develop conventional response prediction baselines.
- Implement S-Learner and T-Learner approaches.
- Explore additional uplift modeling algorithms.
- Evaluate uplift ranking performance.
- Compare models using causal and business-oriented metrics.

## 6. Evaluation Metrics

### Statistical and ML Metrics

- Average Treatment Effect (ATE)
- Confidence intervals
- Conditional Average Treatment Effect (CATE)
- Area Under the Uplift Curve (AUUC)
- Qini coefficient

### Business Metrics

- Incremental conversions
- Incremental revenue
- Incremental profit
- Campaign cost
- Return on Investment (ROI)

## 7. Engineering Objectives

- Modular Python application architecture.
- Reproducible model training.
- Automated data validation.
- Experiment tracking.
- REST API for model inference.
- Interactive Streamlit dashboard.
- Automated testing.
- Docker-based deployment.
- GitHub Actions CI/CD.

## 8. Project Scope

Included:
- Experimental data analysis.
- Causal inference.
- Uplift modeling.
- Model evaluation.
- Campaign targeting recommendations.
- API and dashboard development.

Excluded from the initial version:
- Live integration with an advertising platform.
- Automated sending of marketing emails.
- Real-time customer event streaming.

## 9. Expected Deliverables

- Documented GitHub repository.
- Reproducible data processing pipeline.
- Statistical experiment analysis.
- Trained uplift models.
- Model evaluation reports.
- Interactive application.
- REST API.
- Automated tests.
- Docker deployment configuration.
- Technical documentation.

## 10. Limitations

Historical experimental results may not generalize to future campaigns or different customer populations.

Model estimates must be interpreted with appropriate statistical uncertainty.

Prospective experimentation is required before using model-driven targeting in a real marketing campaign.
