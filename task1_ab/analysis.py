"""
Runs the A/B test analysis and answers questions (a)–(f).
"""
from model import get_retention_curve, compute_dau

if __name__ == "__main__":
    days = 30

    dau_a = compute_dau("A", days)
    dau_b = compute_dau("B", days)

    print(f"DAU Day 15 - Variant A: {int(dau_a[15]):,}")
    print(f"DAU Day 15 - Variant B: {int(dau_b[15]):,}")