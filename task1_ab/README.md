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