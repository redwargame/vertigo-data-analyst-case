"""
Visualization utilities for Task 1 results.

Run the following command from the project root:
    python -m task1_ab.plots
"""


import matplotlib.pyplot as plt

from .model import (
    compute_dau,
    compute_daily_revenue,
    compute_daily_revenue_with_sale,
    compute_revenue_with_new_source,
)


def plot_dau(days: int = 30):
    dau_a = compute_dau("A", days)
    dau_b = compute_dau("B", days)

    plt.figure()
    plt.plot(dau_a, label="Variant A")
    plt.plot(dau_b, label="Variant B")
    plt.title("Daily Active Users Over Time")
    plt.xlabel("Day")
    plt.ylabel("DAU")
    plt.legend()
    plt.savefig("task1_ab/figures/dau_over_time.png", bbox_inches="tight")
    plt.show()
    plt.close()


def plot_cumulative_revenue(days: int = 30):
    rev_a = compute_daily_revenue("A", days).cumsum()
    rev_b = compute_daily_revenue("B", days).cumsum()

    plt.figure()
    plt.plot(rev_a, label="Variant A")
    plt.plot(rev_b, label="Variant B")
    plt.title("Cumulative Revenue (Baseline)")
    plt.xlabel("Day")
    plt.ylabel("Total Revenue")
    plt.legend()
    plt.savefig("task1_ab/figures/revenue.png", bbox_inches="tight")
    plt.show()
    plt.close()


def plot_revenue_scenarios(days: int = 30):
    base_a = compute_daily_revenue("A", days).cumsum()
    base_b = compute_daily_revenue("B", days).cumsum()

    sale_a = compute_daily_revenue_with_sale("A", days, 15, 24).cumsum()
    sale_b = compute_daily_revenue_with_sale("B", days, 15, 24).cumsum()

    new_a = compute_revenue_with_new_source("A", days).cumsum()
    new_b = compute_revenue_with_new_source("B", days).cumsum()

    plt.figure()
    plt.plot(base_a, label="A - Baseline")
    plt.plot(base_b, label="B - Baseline")
    plt.plot(sale_a, label="A - Sale")
    plt.plot(sale_b, label="B - Sale")
    plt.plot(new_a, label="A - New Source")
    plt.plot(new_b, label="B - New Source")

    plt.title("Cumulative Revenue Comparison")
    plt.xlabel("Day")
    plt.ylabel("Total Revenue")
    plt.legend()
    plt.savefig("task1_ab/figures/revenue_comparison.png", bbox_inches="tight")
    plt.show()
    plt.close()


if __name__ == "__main__":
    plot_dau()
    plot_cumulative_revenue()
    plot_revenue_scenarios()