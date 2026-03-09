"""Generate _notes.pdf for chi-square tests (3) + shapiro-wilk (1)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import NotesPDF

def title(pdf, t):
    pdf.add_title(t, "Undergraduate Statistics - Lecture Notes")

# ════════════════════════════════════════════════════════════════
#  9. CHI-SQUARE GOODNESS-OF-FIT
# ════════════════════════════════════════════════════════════════
def gen_chisq_gof():
    pdf = NotesPDF()
    title(pdf, "Chi-Square Goodness-of-Fit Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The chi-square goodness-of-fit test determines whether the observed frequency distribution of a single categorical variable matches an expected (theoretical) distribution. It compares observed counts in each category to the counts we would expect if the hypothesised distribution were true.")
    pdf.body("Scenario: A candy company claims its bags contain equal proportions of 5 colours. A consumer counts the colours in a bag of 200 candies to test this claim.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The observed frequencies match the expected distribution.")
    pdf.body("H\u2081: The observed frequencies do not match the expected distribution.")
    pdf.body("This test is always right-tailed (large \u03c7\u00b2 values indicate poor fit).")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Data are counts (frequencies) for each category.")
    pdf.numbered(2, "Expected frequency in each cell \u2265 5.")
    pdf.numbered(3, "Observations are independent.")
    pdf.numbered(4, "The sample is a simple random sample.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("\u03c7\u00b2 = \u2211 [(O_i - E_i)\u00b2 / E_i]")
    pdf.body("O_i = observed frequency in category i, E_i = expected frequency in category i.")
    pdf.formula("df = k - 1")
    pdf.body("where k = number of categories.")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if \u03c7\u00b2 > \u03c7\u00b2_{\u03b1, df} (always right-tailed).")
    pdf.body("Or reject if p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("Not applicable for this test. The chi-square goodness-of-fit test evaluates the overall fit of a distribution; there is no single parameter for which a CI is naturally constructed.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's w = \u221a(\u03c7\u00b2 / n)")
    pdf.body("|w| = 0.1 small, 0.3 medium, 0.5 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("200 candies counted. Expected: 40 of each colour. Observed: Red=48, Blue=35, Green=42, Yellow=38, Orange=37. Test at \u03b1=0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: proportions are equal (each 0.20)     H\u2081: at least one proportion differs")
    pdf.bold_body("Expected counts")
    pdf.body("E = 200 \u00d7 0.20 = 40 for each colour. All \u2265 5 \u2713")
    pdf.bold_body("Test statistic")
    pdf.body("(48-40)\u00b2/40 + (35-40)\u00b2/40 + (42-40)\u00b2/40 + (38-40)\u00b2/40 + (37-40)\u00b2/40")
    pdf.formula("= 64/40 + 25/40 + 4/40 + 4/40 + 9/40 = 1.600+0.625+0.100+0.100+0.225 = 2.650")
    pdf.body("df = 5 - 1 = 4")
    pdf.bold_body("Critical value")
    pdf.body("\u03c7\u00b2_{0.05, 4} = 9.488")
    pdf.bold_body("P-value")
    pdf.body("p = P(\u03c7\u00b2 > 2.650 | df=4) \u2248 0.618")
    pdf.bold_body("Decision")
    pdf.body("2.650 < 9.488, p = 0.618 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Effect size")
    pdf.formula("w = \u221a(2.650/200) = \u221a0.01325 = 0.115")
    pdf.body("Small effect.")
    pdf.bold_body("Conclusion")
    pdf.body("There is no evidence the colour distribution differs from equal proportions (\u03c7\u00b2 = 2.65, df = 4, p = 0.618). Cohen's w = 0.12 indicates a small effect size.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the colour distribution is not equal when it actually is.")
    pdf.body("Type II: Failing to detect an unequal colour distribution when one exists.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using proportions or percentages instead of raw counts in the formula.")
    pdf.numbered(2, "Proceeding when expected counts are below 5. Combine categories or use an exact test.")
    pdf.numbered(3, "Interpreting this as a two-tailed test. It is always right-tailed.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Sample Proportion Z-Test: For a single proportion with 2 categories.")
    pdf.bullet("Shapiro-Wilk Test: Specifically tests for normality.")

    pdf.save("chi_square_goodness_of_fit")

# ════════════════════════════════════════════════════════════════
#  10. CHI-SQUARE TEST OF INDEPENDENCE
# ════════════════════════════════════════════════════════════════
def gen_chisq_indep():
    pdf = NotesPDF()
    title(pdf, "Chi-Square Test of Independence")
    pdf.section("Section 1: Introduction")
    pdf.body("The chi-square test of independence determines whether there is a statistically significant association between two categorical variables. It uses a contingency table of observed frequencies.")
    pdf.body("Scenario: A researcher surveys 400 people to determine whether preferred exercise type (Running, Swimming, Gym) is associated with age group (18-30, 31-50, 51+).")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The two variables are independent (no association).")
    pdf.body("H\u2081: The two variables are not independent (there is an association).")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Data are counts in a contingency table.")
    pdf.numbered(2, "All expected cell counts \u2265 5.")
    pdf.numbered(3, "Observations are independent.")
    pdf.numbered(4, "Random sampling.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("\u03c7\u00b2 = \u2211 [(O_ij - E_ij)\u00b2 / E_ij]")
    pdf.bold_body("Expected frequency:")
    pdf.formula("E_ij = (Row_i total \u00d7 Column_j total) / Grand total")
    pdf.formula("df = (r - 1)(c - 1)")
    pdf.body("r = number of rows, c = number of columns.")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if \u03c7\u00b2 > \u03c7\u00b2_{\u03b1, df} or p-value < \u03b1. Always right-tailed.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("Not directly applicable. For individual proportions, separate CIs can be constructed.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cramer's V = \u221a[\u03c7\u00b2 / (n \u00d7 min(r-1, c-1))]")
    pdf.body("V ranges from 0 (no association) to 1 (perfect association).")
    pdf.body("Interpretation depends on df* = min(r-1, c-1): for df*=1, V=0.10 small, 0.30 medium, 0.50 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Contingency table (400 people):")
    pdf.body("             Running  Swimming  Gym   |  Total")
    pdf.body("18-30:         55       40       65   |  160")
    pdf.body("31-50:         45       50       45   |  140")
    pdf.body("51+:           30       40       30   |  100")
    pdf.body("Total:        130      130      140   |  400")
    pdf.body("Test at \u03b1 = 0.05.")
    pdf.bold_body("Expected frequencies")
    pdf.body("E(18-30, Run) = 160\u00d7130/400 = 52.0")
    pdf.body("E(18-30, Swim) = 160\u00d7130/400 = 52.0")
    pdf.body("E(18-30, Gym) = 160\u00d7140/400 = 56.0")
    pdf.body("E(31-50, Run) = 140\u00d7130/400 = 45.5")
    pdf.body("E(31-50, Swim) = 140\u00d7130/400 = 45.5")
    pdf.body("E(31-50, Gym) = 140\u00d7140/400 = 49.0")
    pdf.body("E(51+, Run) = 100\u00d7130/400 = 32.5")
    pdf.body("E(51+, Swim) = 100\u00d7130/400 = 32.5")
    pdf.body("E(51+, Gym) = 100\u00d7140/400 = 35.0")
    pdf.body("All expected counts \u2265 5 \u2713")
    pdf.bold_body("Test statistic")
    pdf.body("\u03c7\u00b2 = (55-52)\u00b2/52 + (40-52)\u00b2/52 + (65-56)\u00b2/56 + (45-45.5)\u00b2/45.5 + (50-45.5)\u00b2/45.5 + (45-49)\u00b2/49 + (30-32.5)\u00b2/32.5 + (40-32.5)\u00b2/32.5 + (30-35)\u00b2/35")
    pdf.formula("= 0.173+2.769+1.446+0.005+0.445+0.327+0.192+1.731+0.714 = 7.803")
    pdf.body("df = (3-1)(3-1) = 4")
    pdf.bold_body("Critical value & p-value")
    pdf.body("\u03c7\u00b2_{0.05,4} = 9.488. p \u2248 0.099.")
    pdf.bold_body("Decision")
    pdf.body("7.803 < 9.488, p = 0.099 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Effect size")
    pdf.formula("V = \u221a(7.803 / (400 \u00d7 2)) = \u221a0.00976 = 0.099")
    pdf.body("Small effect.")
    pdf.bold_body("Conclusion")
    pdf.body("No significant association between age group and exercise preference (\u03c7\u00b2 = 7.80, df = 4, p = 0.099). Cramer's V = 0.10 indicates a small effect.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding there is an association between age and exercise when they are independent.")
    pdf.body("Type II: Failing to detect a real association between age and exercise.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using percentages instead of counts.")
    pdf.numbered(2, "Proceeding when expected counts < 5. Use Fisher's exact test instead.")
    pdf.numbered(3, "Confusing independence with homogeneity (different study designs, same test).")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Fisher's Exact Test: Use when expected counts < 5.")
    pdf.bullet("Two-Proportion Z-Test: Equivalent test for 2\u00d72 tables.")

    pdf.save("chi_square_independence")

# ════════════════════════════════════════════════════════════════
#  11. FISHER'S EXACT TEST
# ════════════════════════════════════════════════════════════════
def gen_fishers():
    pdf = NotesPDF()
    title(pdf, "Fisher's Exact Test")
    pdf.section("Section 1: Introduction")
    pdf.body("Fisher's exact test is used to determine whether there is a significant association between two categorical variables in a 2\u00d72 contingency table, especially when sample sizes are small and expected cell counts are below 5. Unlike the chi-square test, it calculates the exact probability rather than relying on an approximation.")
    pdf.body("Scenario: A small clinical trial tests whether a new treatment improves recovery. Of 8 treated patients, 6 recovered; of 7 control patients, 2 recovered. The expected counts are too small for a chi-square test.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The two variables are independent (treatment and outcome are not associated).")
    pdf.body("H\u2081: The two variables are associated.")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Data are in a 2\u00d72 contingency table.")
    pdf.numbered(2, "Observations are independent.")
    pdf.numbered(3, "The row and column totals are fixed (or considered fixed for analysis).")
    pdf.body("No minimum expected count requirement - this is the advantage over chi-square.")

    pdf.section("Section 4: Test Statistic")
    pdf.body("Fisher's exact test does not use a test statistic in the traditional sense. Instead, it computes the exact probability of observing the given table (or more extreme tables) under H\u2080, using the hypergeometric distribution.")
    pdf.bold_body("For a 2\u00d72 table:")
    pdf.body("     | Success | Failure | Total")
    pdf.body("Group 1 |   a   |   b    |  a+b")
    pdf.body("Group 2 |   c   |   d    |  c+d")
    pdf.body("Total   |  a+c  |  b+d   |   n")
    pdf.formula("P = C(a+b, a) \u00d7 C(c+d, c) / C(n, a+c)")
    pdf.body("or equivalently:")
    pdf.formula("P = (a+b)!(c+d)!(a+c)!(b+d)! / [n! a! b! c! d!]")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Sum the probabilities of the observed table and all tables more extreme (in the direction of the alternative). This sum is the p-value.")
    pdf.body("Reject H\u2080 if p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("A CI can be constructed for the odds ratio: OR = (a\u00d7d)/(b\u00d7c). Exact CIs are available but computationally complex.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Odds Ratio = (a \u00d7 d) / (b \u00d7 c)")
    pdf.body("OR = 1 means no association. OR > 1 means the odds of success are higher in Group 1.")
    pdf.formula("Cramer's V = \u221a(\u03c7\u00b2 / n)  (for 2\u00d72 tables)")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Treatment: 6 recovered, 2 not. Control: 2 recovered, 5 not. Test at \u03b1 = 0.05.")
    pdf.body("Table: a=6, b=2, c=2, d=5. n=15.")
    pdf.bold_body("Compute probability of observed table")
    pdf.formula("P = 8!7!8!7! / (15! \u00d7 6!2!2!5!) = (40320\u00d75040\u00d740320\u00d75040) / (1.307E12 \u00d7 720\u00d72\u00d72\u00d7120)")
    pdf.body("P(this table) \u2248 0.1282")
    pdf.bold_body("More extreme tables")
    pdf.body("Table (7,1,1,6): P \u2248 0.0210")
    pdf.body("Table (8,0,0,7): P \u2248 0.0008")
    pdf.bold_body("P-value (one-sided)")
    pdf.body("p = 0.1282 + 0.0210 + 0.0008 = 0.1500")
    pdf.bold_body("P-value (two-sided)")
    pdf.body("p \u2248 0.0630 (Fisher's method, summing both tails)")
    pdf.bold_body("Decision")
    pdf.body("p = 0.063 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Odds ratio")
    pdf.formula("OR = (6\u00d75)/(2\u00d72) = 30/4 = 7.5")
    pdf.body("Patients in the treatment group had 7.5 times the odds of recovery compared to control.")
    pdf.bold_body("Conclusion")
    pdf.body("Despite a large odds ratio (7.5), the test is not significant at \u03b1=0.05 (p=0.063) due to the very small sample size. The data suggest a possible treatment effect that warrants further investigation with a larger sample.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the treatment is effective when it actually is not.")
    pdf.body("Type II: Failing to detect an effective treatment when it actually works.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using the chi-square test when expected counts are < 5. Use Fisher's exact test instead.")
    pdf.numbered(2, "Applying Fisher's test to tables larger than 2\u00d72 without appropriate extensions.")
    pdf.numbered(3, "Confusing one-sided and two-sided p-values. Always report which you are using.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Chi-Square Independence: Use when all expected counts \u2265 5.")
    pdf.bullet("Two-Proportion Z-Test: Large-sample alternative for comparing two proportions.")

    pdf.save("fishers_exact_test")

# ════════════════════════════════════════════════════════════════
#  12. SHAPIRO-WILK TEST
# ════════════════════════════════════════════════════════════════
def gen_shapiro():
    pdf = NotesPDF()
    title(pdf, "Shapiro-Wilk Test for Normality")
    pdf.section("Section 1: Introduction")
    pdf.body("The Shapiro-Wilk test assesses whether a sample comes from a normally distributed population. It is one of the most powerful tests for normality and is recommended for sample sizes from 3 to 5000. Normality is an assumption of many parametric tests, so this test serves as a diagnostic check.")
    pdf.body("Scenario: Before running a one-sample t-test on blood pressure measurements from 20 patients, a researcher uses the Shapiro-Wilk test to verify the data are approximately normal.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: The data come from a normally distributed population.")
    pdf.body("H\u2081: The data do not come from a normally distributed population.")
    pdf.body("Note: We typically WANT to fail to reject H\u2080 (we want the data to be normal).")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "The sample is a random sample.")
    pdf.numbered(2, "Observations are independent.")
    pdf.numbered(3, "Works best for n between 3 and 5000.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("W = (\u2211 a_i x_(i))\u00b2 / \u2211 (x_i - x\u0304)\u00b2")
    pdf.body("Where x_(i) are the ordered sample values, a_i are constants derived from the expected values and covariance matrix of order statistics from a normal distribution.")
    pdf.body("W ranges from 0 to 1. Values close to 1 indicate normality.")
    pdf.body("The exact computation requires special tables for the a_i coefficients, which is why software is used in practice.")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 (reject normality) if W < W_{\u03b1, n} (critical value from Shapiro-Wilk tables) or if p-value < \u03b1.")
    pdf.body("Note: This is a LEFT-tailed test. Small W values indicate departure from normality.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("Not applicable. The Shapiro-Wilk test is a diagnostic test, not a test about a specific parameter value.")

    pdf.section("Section 7: Effect Size")
    pdf.body("There is no standard effect-size measure for the Shapiro-Wilk test. The W statistic itself serves as a measure of how closely the data match a normal distribution (W = 1 is perfect normality).")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Blood pressure readings (mmHg) from 15 patients: 118, 124, 131, 119, 128, 135, 122, 126, 120, 133, 127, 121, 129, 125, 130. Test normality at \u03b1 = 0.05.")
    pdf.bold_body("Step 1: Order the data")
    pdf.body("118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 133, 135")
    pdf.bold_body("Step 2: Compute sample statistics")
    pdf.body("x\u0304 = 125.87,  s = 4.98")
    pdf.bold_body("Step 3: The W statistic")
    pdf.body("Using software (scipy.stats.shapiro): W = 0.9726, p = 0.8921")
    pdf.bold_body("Step 4: Decision")
    pdf.body("W = 0.9726 is close to 1. p = 0.892 >> 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Step 5: Conclusion")
    pdf.body("There is no evidence against normality (W = 0.973, p = 0.892). The data are consistent with a normal distribution. It is appropriate to proceed with parametric tests.")
    pdf.bold_body("Visual checks")
    pdf.body("A Q-Q plot would show the points falling approximately along a straight line. A histogram would appear roughly bell-shaped and symmetric.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the blood pressure data are not normal when they actually are (leading to unnecessary use of nonparametric tests).")
    pdf.body("Type II: Failing to detect non-normality when the data are truly not normal (leading to invalid t-test results).")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Treating a non-significant result as proof of normality. We only fail to reject normality; we do not prove it.")
    pdf.numbered(2, "Relying solely on the Shapiro-Wilk test. Always combine with visual methods (Q-Q plot, histogram).")
    pdf.numbered(3, "Being too strict about normality. Many parametric tests are robust to mild departures from normality, especially with large n.")
    pdf.numbered(4, "Using the test with very large samples (n > 5000). With large n, even trivial departures from normality become significant.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Sample T-Test: Requires normality; use Shapiro-Wilk to check.")
    pdf.bullet("Paired T-Test: Requires normality of differences; check with Shapiro-Wilk.")
    pdf.bullet("One-Way ANOVA: Requires normality within each group.")

    pdf.save("shapiro_wilk_test")

if __name__ == "__main__":
    gen_chisq_gof()
    gen_chisq_indep()
    gen_fishers()
    gen_shapiro()
    print("\nAll 4 chi-square/normality PDFs generated.")
