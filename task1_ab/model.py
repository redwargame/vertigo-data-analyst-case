"""
Core modeling logic for Task 1.
Contains retention curves, DAU calculation, and revenue computation.
"""

import numpy as np

# Retention points provided in the case
RETENTION_POINTS = {
    "A": {
        1: 0.53,
        3: 0.27,
        7: 0.17,
        14: 0.06,
    },
    "B": {
        1: 0.48,
        3: 0.25,
        7: 0.19,
        14: 0.09,
    },
}

def get_retention_curve(variant: str, max_day: int) -> np.ndarray:
    """
    Returns an array where index d represents retention on day d (1-based).
    Retention between known points is linearly interpolated.
    After day 14, retention decays linearly toward zero.
    """
    points = RETENTION_POINTS[variant]
    days = sorted(points.keys())

    retention = np.zeros(max_day + 1)

    # Fill known points
    for d, r in points.items():
        if d <= max_day:
            retention[d] = r

    # Interpolate between known points
    for i in range(len(days) - 1):
        d_start, d_end = days[i], days[i + 1]
        r_start, r_end = points[d_start], points[d_end]

        for d in range(d_start + 1, min(d_end, max_day + 1)):
            t = (d - d_start) / (d_end - d_start)
            retention[d] = r_start + t * (r_end - r_start)

    # Linear decay after last known point
    last_day = days[-1]
    last_retention = points[last_day]

    for d in range(last_day + 1, max_day + 1):
        decay = max(0.0, last_retention * (1 - (d - last_day) / last_day))
        retention[d] = decay

    return retention

def compute_dau(
    variant: str,
    days: int,
    daily_installs: int = 20000,
) -> np.ndarray:
    """
    Computes Daily Active Users (DAU) for a given variant over a number of days.
    DAU is calculated using cohort-based retention.
    """
    retention = get_retention_curve(variant, days)
    dau = np.zeros(days + 1)

    for current_day in range(1, days + 1):
        active_users = 0.0

        # Sum contribution of all cohorts
        for install_day in range(1, current_day + 1):
            age = current_day - install_day + 1
            active_users += daily_installs * retention[age]

        dau[current_day] = active_users

    return dau