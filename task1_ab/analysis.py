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


from model import compute_daily_revenue_with_sale

if __name__ == "__main__":
    days = 30

    sale_start = 15
    sale_end = 24  # 10 days total

    revenue_a_sale = compute_daily_revenue_with_sale(
        "A", days, sale_start, sale_end
    )
    revenue_b_sale = compute_daily_revenue_with_sale(
        "B", days, sale_start, sale_end
    )

    print("\nWith 10-day sale :")
    print(f"Total Revenue by Day 30 - A: ${revenue_a_sale.sum():,.0f}")
    print(f"Total Revenue by Day 30 - B: ${revenue_b_sale.sum():,.0f}")