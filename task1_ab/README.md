# Task 1 – A/B Test Modeling

## Assumptions

Since the problem doesn't explicitly state how users behave on days where retention values are not given, the following assumptions are made to be able to complete the analysis.

- Retention values are only provided for days 1, 3, 7, and 14. To estimate daily active users, retention between these days is assumed to decrease smoothly and is interpolated linearly.
- After Day 14, retention is assumed to continue decreasing linearly toward zero.
- Each day, 20,000 new users install each variant, and daily active users are calculated by summing the retained users from all previous days and the current day.
- The daily purchase ratio is interpreted as the probability that an active user makes a purchase on a given day. Since the value of a purchase is not specified, each purchase is assumed to generate $1 of revenue. This normalization allows comparison between variants without affecting relative results.
- Ad revenue is calculated using the provided eCPM and average ad impressions per active user. The number of impressions and eCPM are assumed to be constant over time.
- Retention, ad viewing, and purchase behavior are assumed to be independent of each other. Temporary sales only affect purchase probability, and new user sources follow the retention formulas provided in the problem.

These assumptions are made to keep the model simple while allowing meaningful comparison between Variant A and Variant B.


## Conclusions

### Answer for a
- According to analysis, Variant A is expected to have 56,714 active users on Day 15, while Variant B has 59,171. This means Variant B has more daily active users than Variant A after 15 days.

### Answer for b
- By Day 15, Variant A is expected to earn $31,979, while Variant B earns $28,969. This means Variant A earns more money by Day 15.

### Answer for c
- By Day 30, Variant A is expected to earn $81,119, while Variant B earns $77,809. This means our choice does not change.

### Answer for d
- If we run a 10-day sale starting on Day 15, Variant A is expected to earn $87,151, while Variant B earns $84,266. This means the sale doesn't change the result. Variant A is still expected to earn more money by Day 30.

### Answer for e
- With the inclusion of a new user source, Variant A is expected to earn $84,417, while Variant B earns $80,561. This means Variant A makes more money by Day 30.

### Answer for f
- I would prioritize the 10-day sale improvement since it will make the most overall money by Day 30. It has a clear adventage over the new user source improvement on both variants. For that reason, I would go with the sale improvement in either scenario.

### Overall conclusion for Task 1
- While Variant B has a higher daily active user count than Variant A, Variant A’s ad monetization efficiency makes it the better choice overall. Over a 30-day period, Variant B does not gain enough additional daily active users to close the gap created by Variant A’s stronger early DAU performance and superior ad monetization.


## Visualizations

### Daily Active Users Over Time
![DAU Over Time](figures/dau_over_time.png)

### Cumulative Revenue (Baseline)
![Baseline Revenue](figures/revenue.png)

### Cumulative Revenue Across Scenarios
![Revenue Scenarios](figures/revenue_comparison.png)