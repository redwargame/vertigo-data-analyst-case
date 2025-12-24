# Task 2 – Exploratory Data Analysis

## Objective

The goal of Task 2 is to explore user behavior patterns and uncover meaningful segments and trends using the provided daily player activity dataset. The analysis focuses on engagement, retention behavior, and monetization outcomes, supported by statistical summaries and visualizations.

---

## Dataset Overview

The dataset contains daily aggregated user-level data describing in-game and monetization activity. Each row represents a single user’s activity on a given day.

Key fields include:

- User attributes: platform, country, install date  
- Engagement metrics: session count, session duration, match activity  
- Performance metrics: victories, defeats, server connection errors  
- Monetization metrics: in-app purchase (IAP) revenue and ad revenue  

---

## Data Preparation & Assumptions

- Event dates and install dates were converted to datetime format.
- A derived feature, `days_since_install`, was created as:

    days_since_install = event_date − install_date

- Rows where `days_since_install = 0` represent Day-1 activity, not uninstall behavior.
- A small percentage of users have missing country values; these were retained as they do not materially affect the analysis.
- Revenue distributions are highly right-skewed, which is typical for free-to-play games.

---

## Analysis 1 – Day-1 Engagement Segmentation

### Methodology

Users were segmented based on their Day-1 total session duration using percentile-based cutoffs:

- Low engagement (bottom ~33%)
- Medium engagement (middle ~33%)
- High engagement (top ~34%)

Day-1 engagement is used as an early indicator of user intent and long-term value.

### Findings

- Engagement is evenly distributed across the three segments.
- High-engagement users already show:
- More sessions on Day-1
- Higher match participation
- Early engagement strongly correlates with future activity and revenue potential.

---

## Analysis 2 – Session Duration Trend Over Time

### Question

Do users spend more or less time in the game as time since install increases?

### Findings

- Average session duration increases steadily during the first ~20 days after install.
- After this initial growth period, session duration stabilizes around ~2,000 seconds with minor fluctuations.
- No long-term decline in session duration is observed among retained users.

### Interpretation

This trend suggests an early onboarding and learning phase, followed by stable engagement among core users who remain active over time.

---

## Analysis 3 – Monetization by Day-1 Engagement Segment

### Methodology

Total user revenue was calculated as the sum of IAP revenue and ad revenue over the observed period. Revenue was then analyzed by Day-1 engagement segment.

### Findings

- High Day-1 engagement users generate significantly higher average revenue.
- Revenue distributions are heavily right-skewed:
- A small fraction of users account for a disproportionate share of total revenue.
- Low and Medium engagement segments contribute relatively limited revenue on average.

### Business Implication

Improving early user engagement is likely to yield the highest return on investment in terms of monetization, retention, and long-term user value.

---

## Key Takeaways

- Day-1 engagement is a strong predictor of long-term user behavior.
- Session duration grows early and stabilizes, indicating healthy engagement patterns.
- Monetization is driven primarily by highly engaged users, emphasizing the importance of early user experience optimization.

---

## Project Structure

task2_eda/
├── eda.ipynb
├── figures/
└── README.md

---

## Final Notes

This exploratory analysis demonstrates how early engagement metrics can be used to segment users and extract actionable insights. The approach is designed to be interpretable, reproducible, and aligned with real-world data analytics workflows.

---

## Visualizations

### Average Total Revenue per User by Day-1 Engagement Segment
![Avg Revenue Per User](figures/revenue_by_engagement.png)

### Average Session Duration Over Player Lifetime
![Avg Session Duration](figures/session_duration_trend.png)

### Distribution of Total Revenue per User
![Distribution of Revenue by User](figures/revenue_distribution.png)