"""
Runs the A/B test analysis and answers questions (a)–(f).
"""
from model import get_retention_curve

if __name__ == "__main__":
    curve_a = get_retention_curve("A", 30)
    curve_b = get_retention_curve("B", 30)

    print("Variant A - D1, D7, D14:", curve_a[1], curve_a[7], curve_a[14])
    print("Variant B - D1, D7, D14:", curve_b[1], curve_b[7], curve_b[14])