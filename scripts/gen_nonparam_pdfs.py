"""Generate _notes.pdf for 4 nonparametric tests."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import NotesPDF

def title(pdf, t):
    pdf.add_title(t, "Undergraduate Statistics - Lecture Notes")

# ════════════════════════════════════════════════════════════════
#  15. SIGN TEST
# ════════════════════════════════════════════════════════════════
def gen_sign():
    pdf = NotesPDF()
    title(pdf, "Sign Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The sign test is a nonparametric test for matched pairs (or a single sample) that tests whether the median of differences equals zero. It requires only the SIGNS (+/-) of the differences, not their magnitudes, making it useful for ordinal data or when the distribution of differences is heavily skewed with outliers.")
    pdf.body("Scenario: A taste-testing panel of 12 judges each rates two coffee brands (A and B). The researcher records whether each judge preferred A (+) or B (-), ignoring ties. The question is whether there is a significant preference for one brand.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The median difference is 0 (P(+) = 0.5)")
    pdf.body("H\u2081: The median difference \u2260 0  (two-tailed)")
    pdf.body("Or H\u2081: median > 0  (right-tailed) or H\u2081: median < 0  (left-tailed)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Paired observations or single sample compared to a hypothesised median.")
    pdf.numbered(2, "The data are at least ordinal (we only need the direction of each difference).")
    pdf.numbered(3, "Pairs are independent.")
    pdf.numbered(4, "Ties (zero differences) are excluded from the analysis.")

    pdf.section("Section 4: Test Statistic")
    pdf.body("Let S = number of positive differences (or negative, whichever is fewer for a two-tailed test).")
    pdf.body("Under H\u2080, S follows a Binomial(n, 0.5) distribution, where n is the number of non-tied pairs.")
    pdf.bold_body("For large n (n \u2265 25), use the normal approximation:")
    pdf.formula("z = (S - n/2) / (\u221an / 2)")

    pdf.section("Section 5: Decision Rule")
    pdf.body("For small n: Use binomial tables. Reject H\u2080 if P(X \u2264 S) < \u03b1/2 (two-tailed).")
    pdf.body("For large n: Use the z-statistic. Reject H\u2080 if |z| > z_{\u03b1/2}.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("A CI for the median can be constructed using binomial quantiles. The k-th smallest and k-th largest observations form the CI endpoints, where k is found from the binomial distribution.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("r = Z / \u221an")
    pdf.body("|r| = 0.1 small, 0.3 medium, 0.5 large.")
    pdf.body("Alternatively, report the proportion of positive signs as a descriptive measure.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("12 judges taste-test two coffees. Results (A vs B): +, +, -, +, +, +, -, +, +, -, +, +. Count: 9 positive, 3 negative, 0 ties. Test at \u03b1 = 0.05 whether there is a preference.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: P(+) = 0.5     H\u2081: P(+) \u2260 0.5")
    pdf.bold_body("Test statistic")
    pdf.body("S = min(9, 3) = 3 (using the smaller count), n = 12")
    pdf.bold_body("P-value (exact, binomial)")
    pdf.body("p = 2 \u00d7 P(X \u2264 3 | n=12, p=0.5) = 2 \u00d7 0.0730 = 0.1460")
    pdf.bold_body("Decision")
    pdf.body("p = 0.146 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Effect size")
    pdf.body("Using normal approximation: z = (9 - 6) / (0.5\u221a12) = 3/1.732 = 1.732")
    pdf.formula("r = 1.732 / \u221a12 = 0.500")
    pdf.body("Large effect, but not significant due to small sample size.")
    pdf.bold_body("Conclusion")
    pdf.body("There is no statistically significant preference for either coffee brand at \u03b1 = 0.05 (p = 0.146), despite 9 of 12 judges preferring Brand A. The small sample size limits statistical power.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding there is a preference for one coffee when there actually is not.")
    pdf.body("Type II: Failing to detect a real preference when one exists.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Including ties in the count. Tied observations should be excluded.")
    pdf.numbered(2, "Using the sign test when the Wilcoxon signed-rank test is more appropriate. The sign test discards magnitude information and is less powerful.")
    pdf.numbered(3, "Forgetting to double the tail probability for a two-tailed test.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Wilcoxon Signed-Rank Test: More powerful nonparametric paired test (uses magnitudes).")
    pdf.bullet("Paired T-Test: Parametric alternative when differences are normally distributed.")

    pdf.save("sign_test")

# ════════════════════════════════════════════════════════════════
#  16. WILCOXON SIGNED-RANK TEST
# ════════════════════════════════════════════════════════════════
def gen_wilcoxon():
    pdf = NotesPDF()
    title(pdf, "Wilcoxon Signed-Rank Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The Wilcoxon signed-rank test is a nonparametric test for paired data that tests whether the median difference between paired observations equals zero. Unlike the sign test, it uses both the signs AND the magnitudes (ranks) of the differences, making it more powerful.")
    pdf.body("Scenario: A physiotherapist measures pain scores (1-10 scale) of 10 patients before and after a treatment to determine whether the treatment reduces pain.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The median of the differences is 0.")
    pdf.body("H\u2081: The median of the differences \u2260 0  (or < 0 or > 0)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Paired observations (before/after, matched subjects).")
    pdf.numbered(2, "The differences are continuous and symmetric about the median.")
    pdf.numbered(3, "The differences are at least interval-scaled (we need magnitudes).")
    pdf.numbered(4, "Pairs are independent.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.body("1. Compute differences d_i = x_i - y_i. Exclude zeros.")
    pdf.body("2. Rank the |d_i| values from smallest to largest. Assign average ranks for ties.")
    pdf.body("3. Assign each rank the sign of its d_i.")
    pdf.body("4. W+ = sum of positive ranks, W- = sum of negative ranks.")
    pdf.formula("W = min(W+, W-)   (for two-tailed test)")
    pdf.bold_body("For large n (\u2265 25), use normal approximation:")
    pdf.formula("z = (W - n(n+1)/4) / \u221a[n(n+1)(2n+1)/24]")

    pdf.section("Section 5: Decision Rule")
    pdf.body("For small n: Reject H\u2080 if W \u2264 W_critical (from Wilcoxon tables).")
    pdf.body("For large n: Reject H\u2080 if |z| > z_{\u03b1/2} or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("A CI for the median difference can be constructed using Walsh averages: compute all pairwise averages (d_i + d_j)/2 for i \u2264 j, then take the appropriate percentiles.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("r = Z / \u221an")
    pdf.body("|r| = 0.1 small, 0.3 medium, 0.5 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Pain scores (before - after) for 10 patients: 3, -1, 4, 2, 5, 1, 3, 0, 2, 4. Test at \u03b1 = 0.05.")
    pdf.bold_body("Step 1: Remove zeros")
    pdf.body("Remove the 0: remaining differences = {3, -1, 4, 2, 5, 1, 3, 2, 4}, n = 9")
    pdf.bold_body("Step 2: Rank absolute values")
    pdf.body("|d|: 1, 1, 2, 2, 3, 3, 4, 4, 5")
    pdf.body("Ranks: 1.5, 1.5, 3.5, 3.5, 5.5, 5.5, 7.5, 7.5, 9")
    pdf.bold_body("Step 3: Assign signs to ranks")
    pdf.body("Positive: 1.5(d=1) + 3.5(d=2) + 5.5(d=3) + 7.5(d=4) + 9(d=5) + 5.5(d=3) + 3.5(d=2) + 7.5(d=4) = 43.5")
    pdf.body("Negative: 1.5(d=-1) = 1.5")
    pdf.bold_body("Step 4: Test statistic")
    pdf.body("W+ = 43.5, W- = 1.5. W = min(43.5, 1.5) = 1.5")
    pdf.bold_body("Step 5: Critical value")
    pdf.body("For n=9, \u03b1=0.05 two-tailed: W_critical = 5.")
    pdf.bold_body("Step 6: Decision")
    pdf.body("W = 1.5 < 5. Reject H\u2080.")
    pdf.bold_body("Step 7: Effect size")
    pdf.body("z \u2248 -2.547 (from normal approximation)")
    pdf.formula("r = 2.547 / \u221a9 = 0.849")
    pdf.body("Very large effect.")
    pdf.bold_body("Conclusion")
    pdf.body("The treatment significantly reduced pain scores (W = 1.5, p < 0.05, r = 0.85). The effect is very large.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the treatment reduces pain when it actually does not.")
    pdf.body("Type II: Failing to detect that the treatment reduces pain when it actually does.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Forgetting to remove zero differences before ranking.")
    pdf.numbered(2, "Not using average ranks for tied values.")
    pdf.numbered(3, "Applying this test when data are only ordinal (no meaningful magnitudes). Use the sign test instead.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Paired T-Test: Parametric alternative (more powerful when normality holds).")
    pdf.bullet("Sign Test: Less powerful alternative when only signs are meaningful.")
    pdf.bullet("Mann-Whitney U: Independent samples version.")

    pdf.save("wilcoxon_signed_rank")

# ════════════════════════════════════════════════════════════════
#  17. MANN-WHITNEY U TEST
# ════════════════════════════════════════════════════════════════
def gen_mann_whitney():
    pdf = NotesPDF()
    title(pdf, "Mann-Whitney U Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The Mann-Whitney U test (also called the Wilcoxon rank-sum test) is a nonparametric test that compares two independent groups to determine whether their population distributions differ. It tests whether one group tends to have larger values than the other.")
    pdf.body("Scenario: A company compares customer satisfaction ratings (1-10) between two store locations (Store A: n=12, Store B: n=10) to determine if satisfaction differs.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The distributions of the two populations are identical.")
    pdf.body("H\u2081: The distributions differ (one group tends to have larger values).")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Two independent random samples.")
    pdf.numbered(2, "The dependent variable is at least ordinal.")
    pdf.numbered(3, "Observations within and between groups are independent.")
    pdf.numbered(4, "Under the null, the two distributions have the same shape (differ only in location, if at all).")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.body("1. Combine all observations and rank them from 1 to N = n\u2081 + n\u2082.")
    pdf.body("2. Sum the ranks for each group: R\u2081 and R\u2082.")
    pdf.formula("U\u2081 = n\u2081 n\u2082 + n\u2081(n\u2081+1)/2 - R\u2081")
    pdf.formula("U\u2082 = n\u2081 n\u2082 + n\u2082(n\u2082+1)/2 - R\u2082")
    pdf.formula("U = min(U\u2081, U\u2082)")
    pdf.bold_body("Normal approximation (large samples):")
    pdf.formula("z = (U - n\u2081 n\u2082/2) / \u221a[n\u2081 n\u2082(n\u2081+n\u2082+1)/12]")

    pdf.section("Section 5: Decision Rule")
    pdf.body("For small samples: Reject H\u2080 if U \u2264 U_critical (from Mann-Whitney tables).")
    pdf.body("For large samples: Reject H\u2080 if |z| > z_{\u03b1/2} or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("A CI can be constructed for the difference in medians using the Hodges-Lehmann estimator: compute all n\u2081\u00d7n\u2082 pairwise differences and take the median.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("r = Z / \u221aN   (where N = n\u2081 + n\u2082)")
    pdf.body("|r| = 0.1 small, 0.3 medium, 0.5 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Store A ratings: 7, 8, 6, 9, 5, 8, 7, 6, 9, 8, 7, 8 (n\u2081=12)")
    pdf.body("Store B ratings: 5, 6, 4, 7, 5, 6, 3, 5, 6, 4 (n\u2082=10)")
    pdf.body("Test at \u03b1 = 0.05.")
    pdf.bold_body("Step 1: Rank all 22 values combined")
    pdf.body("Sum of ranks for Store A: R\u2081 = 183.5")
    pdf.body("Sum of ranks for Store B: R\u2082 = 69.5")
    pdf.bold_body("Step 2: Compute U")
    pdf.formula("U\u2081 = 12\u00d710 + 12(13)/2 - 183.5 = 120+78-183.5 = 14.5")
    pdf.formula("U\u2082 = 12\u00d710 + 10(11)/2 - 69.5 = 120+55-69.5 = 105.5")
    pdf.body("U = min(14.5, 105.5) = 14.5")
    pdf.bold_body("Step 3: Normal approximation")
    pdf.formula("z = (14.5 - 60) / \u221a[120\u00d723/12] = -45.5 / \u221a230 = -45.5/15.17 = -2.999")
    pdf.bold_body("Step 4: Decision")
    pdf.body("|z| = 3.00 > 1.960, p \u2248 0.003 < 0.05. Reject H\u2080.")
    pdf.bold_body("Step 5: Effect size")
    pdf.formula("r = 2.999 / \u221a22 = 0.640")
    pdf.body("Large effect.")
    pdf.bold_body("Conclusion")
    pdf.body("Store A has significantly higher satisfaction ratings than Store B (U = 14.5, z = -3.00, p = 0.003). The effect size is large (r = 0.64).")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding satisfaction differs between stores when it actually does not.")
    pdf.body("Type II: Failing to detect a real difference in satisfaction between stores.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using this test on paired data. Use Wilcoxon signed-rank test instead.")
    pdf.numbered(2, "Forgetting to handle ties properly (use average ranks).")
    pdf.numbered(3, "Interpreting the test as comparing medians specifically. It compares entire distributions.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Two-Sample T-Test / Welch's T-Test: Parametric alternatives.")
    pdf.bullet("Wilcoxon Signed-Rank: Paired-sample version.")
    pdf.bullet("Kruskal-Wallis: Extension to more than 2 groups.")

    pdf.save("mann_whitney_u")

# ════════════════════════════════════════════════════════════════
#  18. KRUSKAL-WALLIS TEST
# ════════════════════════════════════════════════════════════════
def gen_kruskal():
    pdf = NotesPDF()
    title(pdf, "Kruskal-Wallis Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The Kruskal-Wallis test is a nonparametric alternative to the one-way ANOVA. It tests whether the distributions of three or more independent groups are identical, without assuming normality. It extends the Mann-Whitney U test to more than two groups.")
    pdf.body("Scenario: A researcher compares student satisfaction scores (1-10 scale) across three different online learning platforms (n\u2081=8, n\u2082=7, n\u2083=9) to determine if satisfaction differs by platform.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: All k population distributions are identical.")
    pdf.body("H\u2081: At least one distribution differs from the others.")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "k \u2265 2 independent random samples.")
    pdf.numbered(2, "The dependent variable is at least ordinal.")
    pdf.numbered(3, "Observations are independent within and between groups.")
    pdf.numbered(4, "The distributions have similar shapes (the test compares locations).")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.body("1. Combine all N observations and rank from 1 to N.")
    pdf.body("2. Compute the sum of ranks for each group: R_1, R_2, ..., R_k.")
    pdf.formula("H = [12 / (N(N+1))] \u2211 [R_i\u00b2 / n_i] - 3(N+1)")
    pdf.body("N = total sample size, n_i = size of group i, R_i = rank sum for group i.")
    pdf.body("Under H\u2080, H follows approximately a chi-square distribution with df = k - 1.")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if H > \u03c7\u00b2_{\u03b1, k-1} or p-value < \u03b1. Always right-tailed.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("Not directly applicable to the overall test. Post-hoc pairwise comparisons (e.g., Dunn's test) can be performed if H\u2080 is rejected.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("\u03b7\u00b2_H = (H - k + 1) / (N - k)")
    pdf.body("Or equivalently: \u03b5\u00b2 = H / (N\u00b2 - 1)/(N + 1).")
    pdf.body("Interpretation: 0.01 small, 0.06 medium, 0.14 large (same as ANOVA \u03b7\u00b2).")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Platform A: 7, 8, 6, 9, 7, 8, 5, 8 (n\u2081=8)")
    pdf.body("Platform B: 5, 6, 4, 5, 7, 6, 5 (n\u2082=7)")
    pdf.body("Platform C: 8, 9, 7, 8, 9, 8, 7, 9, 8 (n\u2083=9)")
    pdf.body("N = 24. Test at \u03b1 = 0.05.")
    pdf.bold_body("Step 1: Rank all 24 values")
    pdf.body("R\u2081 (Platform A) = 131.0")
    pdf.body("R\u2082 (Platform B) = 44.0")
    pdf.body("R\u2083 (Platform C) = 125.0")
    pdf.bold_body("Step 2: Compute H")
    pdf.formula("H = [12/(24\u00d725)] \u00d7 [131\u00b2/8 + 44\u00b2/7 + 125\u00b2/9] - 3(25)")
    pdf.formula("= 0.02 \u00d7 [2145.1 + 276.6 + 1736.1] - 75 = 0.02 \u00d7 4157.8 - 75 = 83.16 - 75 = 8.16")
    pdf.body("df = 3 - 1 = 2")
    pdf.bold_body("Critical value")
    pdf.body("\u03c7\u00b2_{0.05, 2} = 5.991")
    pdf.bold_body("Decision")
    pdf.body("H = 8.16 > 5.991, p \u2248 0.017 < 0.05. Reject H\u2080.")
    pdf.bold_body("Effect size")
    pdf.formula("\u03b7\u00b2 = (8.16 - 2) / (24 - 3) = 6.16 / 21 = 0.293")
    pdf.body("Large effect.")
    pdf.bold_body("Conclusion")
    pdf.body("There is a significant difference in satisfaction across the three platforms (H = 8.16, df = 2, p = 0.017). Post-hoc tests (e.g., Dunn's test) would identify which specific pairs differ.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding platforms differ in satisfaction when they actually do not.")
    pdf.body("Type II: Failing to detect real differences in satisfaction across platforms.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using Kruskal-Wallis for paired/repeated measures data. Use Friedman's test instead.")
    pdf.numbered(2, "Stopping at the overall test. If H\u2080 is rejected, perform post-hoc pairwise comparisons.")
    pdf.numbered(3, "Forgetting ties correction when many tied ranks are present.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Way ANOVA: Parametric alternative (more powerful when normality holds).")
    pdf.bullet("Mann-Whitney U: Use when comparing only 2 groups.")

    pdf.save("kruskal_wallis")

if __name__ == "__main__":
    gen_sign()
    gen_wilcoxon()
    gen_mann_whitney()
    gen_kruskal()
    print("\nAll 4 nonparametric PDFs generated.")
