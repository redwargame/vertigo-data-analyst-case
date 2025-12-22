"""
Runs the A/B test analysis and answers questions (a)–(f).
"""
from model import compute_dau, compute_daily_revenue

if __name__ == "__main__":
    days = 30

    revenue_a = compute_daily_revenue("A", days)
    revenue_b = compute_daily_revenue("B", days)

    print(f"Total Revenue by Day 15 - A: ${revenue_a[:16].sum():,.0f}")
    print(f"Total Revenue by Day 15 - B: ${revenue_b[:16].sum():,.0f}")

    print(f"Total Revenue by Day 30 - A: ${revenue_a.sum():,.0f}")
    print(f"Total Revenue by Day 30 - B: ${revenue_b.sum():,.0f}")