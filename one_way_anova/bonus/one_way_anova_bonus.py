"""Basic ANOVA helper using statistics module."""
from __future__ import annotations

import statistics

def anova(groups: list[list[float]]) -> tuple[float, float, float]:
    k = len(groups)
    n_total = sum(len(g) for g in groups)
    grand_mean = sum(sum(g) for g in groups) / n_total
    ss_between = sum(len(g) * (statistics.mean(g) - grand_mean) ** 2 for g in groups)
    ss_within = sum(sum((x - statistics.mean(g)) ** 2 for x in g) for g in groups)
    df_between = k - 1
    df_within = n_total - k
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    f_stat = ms_between / ms_within
    return f_stat, df_between, df_within

if __name__ == "__main__":
    g1 = [45, 47, 50, 48, 46]
    g2 = [42, 40, 41, 43, 39]
    g3 = [38, 37, 39, 36, 35]
    f, dfb, dfw = anova([g1, g2, g3])
    print(f"F={f:.2f} with df={dfb},{dfw}")
