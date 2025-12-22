# Task 1 – A/B Test Modeling

## Assumptions

Since the problem does not explicitly state how users behave on days where retention values are not given, the following assumptions are made in order to complete the analysis.

- Retention values are only provided for Days 1, 3, 7, and 14. To estimate daily active users, retention between these days is assumed to decrease smoothly and is interpolated linearly.
- After Day 14, retention is assumed to continue decreasing linearly toward zero.
- Each day, 20,000 new users install each variant. Daily active users are calculated by summing the retained users from all previous days and the current day.
- The daily purchase ratio is interpreted as the probability that an active user makes a purchase on a given day. Since the value of a purchase is not specified, each purchase is assumed to generate $1 of revenue. This normalization allows comparison between variants without affecting relative results.
- Ad revenue is calculated using the provided eCPM and the average number of ad impressions per active user. The number of impressions and eCPM are assumed to be constant over time.
- Retention, ad viewing, and purchase behavior are assumed to be independent of each other. Temporary sales only affect purchase probability, and new user sources follow the retention formulas provided in the problem.

These assumptions are made to keep the model simple while allowing meaningful comparison between Variant A and Variant B.

## Conclusions

### Answer for a
- According to the analysis, Variant A is expected to have 56,714 daily active users on Day 15, while Variant B is expected to have 59,171. This indicates that Variant B has more daily active users than Variant A after 15 days.

### Answer for b
- By Day 15, Variant A is expected to earn $31,979, while Variant B earns $28,969. Therefore, Variant A earns more total revenue by Day 15.

### Answer for c
- By Day 30, Variant A is expected to earn $81,119, while Variant B earns $77,809. This means the preferred variant does not change when extending the time horizon to 30 days.

### Answer for d
- If a 10-day sale is run starting on Day 15, Variant A is expected to earn $87,151, while Variant B earns $84,266. Although both variants benefit from the sale, Variant A still earns more total revenue by Day 30.

### Answer for e
- With the inclusion of a new user source starting on Day 20, Variant A is expected to earn $84,417 by Day 30, while Variant B earns $80,561. This indicates that Variant A continues to outperform Variant B in total revenue.

### Answer for f
- I would prioritize the 10-day sale improvement, as it generates a larger revenue increase by Day 30 compared to adding the new user source. The sale shows a clear advantage over the new user source for both variants, making it the more impactful improvement within the observed time frame.

### Overall Conclusion for Task 1
- While Variant B achieves a higher daily active user count than Variant A in later days, Variant A’s stronger ad monetization efficiency makes it the better overall choice. Over a 30-day period, Variant B does not gain enough additional daily active users to overcome the revenue advantage created by Variant A’s higher monetization and stronger early performance.

## Visualizations

### Daily Active Users Over Time
![DAU Over Time](figures/dau_over_time.png)

### Cumulative Revenue (Baseline)
![Baseline Revenue](figures/revenue.png)

### Cumulative Revenue Across Scenarios
![Revenue Scenarios](figures/revenue_comparison.png)