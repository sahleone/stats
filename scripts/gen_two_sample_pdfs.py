"""Generate _notes.pdf for 5 two-sample hypothesis tests."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import NotesPDF

def title(pdf, t):
    pdf.add_title(t, "Undergraduate Statistics - Lecture Notes")

# ════════════════════════════════════════════════════════════════
#  4. TWO-SAMPLE Z-TEST
# ════════════════════════════════════════════════════════════════
def gen_two_sample_z():
    pdf = NotesPDF()
    title(pdf, "Two-Sample Z-Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The two-sample z-test compares the means of two independent populations when both population standard deviations (\u03c3\u2081 and \u03c3\u2082) are known. It tests whether the difference between the two population means equals a hypothesised value (usually 0).")
    pdf.body("Real-world scenario: A pharmaceutical company compares the average recovery time for patients using Drug A versus Drug B. Historical data give \u03c3\u2081 = 3.5 days and \u03c3\u2082 = 4.0 days. Samples of 50 patients per group are compared.")

    pdf.section("Section 2: Hypotheses")
    pdf.bold_body("Two-tailed:")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 \u2260 0")
    pdf.bold_body("Left-tailed:")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 < 0")
    pdf.bold_body("Right-tailed:")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 > 0")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Both population standard deviations \u03c3\u2081 and \u03c3\u2082 are known.")
    pdf.numbered(2, "Samples are independent simple random samples.")
    pdf.numbered(3, "Both populations are normal, OR both sample sizes are \u2265 30.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("z = (x\u0304\u2081 - x\u0304\u2082) / \u221a(\u03c3\u2081\u00b2/n\u2081 + \u03c3\u2082\u00b2/n\u2082)")
    pdf.body("No degrees of freedom (uses the standard normal distribution).")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Same as the one-sample z-test: compare |z| to z_{\u03b1/2} (two-tailed) or z_\u03b1 (one-tailed). Reject H\u2080 if p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = (x\u0304\u2081 - x\u0304\u2082) \u00b1 z_{\u03b1/2} \u00b7 \u221a(\u03c3\u2081\u00b2/n\u2081 + \u03c3\u2082\u00b2/n\u2082)")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's d = (x\u0304\u2081 - x\u0304\u2082) / \u221a[(\u03c3\u2081\u00b2 + \u03c3\u2082\u00b2)/2]")
    pdf.body("|d| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Drug A: n\u2081=50, x\u0304\u2081=12.3 days, \u03c3\u2081=3.5. Drug B: n\u2082=50, x\u0304\u2082=14.1 days, \u03c3\u2082=4.0. Test whether recovery times differ at \u03b1 = 0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 \u2260 0")
    pdf.bold_body("Test statistic")
    pdf.formula("SE = \u221a(3.5\u00b2/50 + 4.0\u00b2/50) = \u221a(0.245 + 0.32) = \u221a0.565 = 0.7517")
    pdf.formula("z = (12.3 - 14.1) / 0.7517 = -1.8 / 0.7517 = -2.395")
    pdf.bold_body("Critical value & p-value")
    pdf.body("z_{0.025} = 1.960. p-value = 2 \u00d7 P(Z < -2.395) = 2 \u00d7 0.0083 = 0.0166.")
    pdf.bold_body("Decision")
    pdf.body("|z| = 2.395 > 1.960, p = 0.0166 < 0.05. Reject H\u2080.")
    pdf.bold_body("Confidence interval")
    pdf.formula("CI = -1.8 \u00b1 1.960 \u00d7 0.7517 = (-3.273, -0.327)")
    pdf.body("0 is outside the CI.")
    pdf.bold_body("Effect size")
    pdf.formula("d = -1.8 / \u221a[(3.5\u00b2 + 4.0\u00b2)/2] = -1.8 / 3.755 = -0.479")
    pdf.body("Medium effect.")
    pdf.bold_body("Conclusion")
    pdf.body("There is significant evidence (z = -2.40, p = 0.017) that recovery times differ between the two drugs. Drug A patients recover about 1.8 days faster. The effect is medium-sized (d = -0.48).")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding recovery times differ when they actually do not.")
    pdf.body("Type II: Failing to detect a real difference in recovery times.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using this test when \u03c3\u2081 or \u03c3\u2082 is unknown. Use a two-sample t-test instead.")
    pdf.numbered(2, "Applying this test to paired data. Use the paired t-test for matched samples.")
    pdf.numbered(3, "Forgetting to check independence between the two samples.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Two-Sample T-Test (Equal Variances): Use when \u03c3 is unknown.")
    pdf.bullet("Welch's T-Test: Use when \u03c3 is unknown and variances are unequal.")

    pdf.save("two_sample_z_test")

# ════════════════════════════════════════════════════════════════
#  5. TWO-SAMPLE T-TEST (EQUAL VARIANCES)
# ════════════════════════════════════════════════════════════════
def gen_two_sample_t_eq():
    pdf = NotesPDF()
    title(pdf, "Two-Sample T-Test (Equal Variances)")
    pdf.section("Section 1: Introduction")
    pdf.body("The two-sample t-test for independent means (equal variances assumed) compares the means of two independent populations when \u03c3 is unknown but the two populations are assumed to have equal variances. The pooled standard deviation is used.")
    pdf.body("Scenario: A school district compares test scores of students taught with Method A (n\u2081=30, x\u0304\u2081=78.4, s\u2081=9.2) versus Method B (n\u2082=28, x\u0304\u2082=83.1, s\u2082=8.7).")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 \u2260 0  (or one-tailed)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Both populations have equal variances (\u03c3\u2081\u00b2 = \u03c3\u2082\u00b2). Verify with F-test or Levene's test.")
    pdf.numbered(2, "Samples are independent random samples.")
    pdf.numbered(3, "Both populations are approximately normal, or both n \u2265 30.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("t = (x\u0304\u2081 - x\u0304\u2082) / [s_p \u221a(1/n\u2081 + 1/n\u2082)]")
    pdf.bold_body("Pooled standard deviation:")
    pdf.formula("s_p = \u221a[((n\u2081-1)s\u2081\u00b2 + (n\u2082-1)s\u2082\u00b2) / (n\u2081+n\u2082-2)]")
    pdf.formula("df = n\u2081 + n\u2082 - 2")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if |t| > t_{\u03b1/2, df} (two-tailed) or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = (x\u0304\u2081 - x\u0304\u2082) \u00b1 t_{\u03b1/2,df} \u00b7 s_p\u221a(1/n\u2081 + 1/n\u2082)")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's d = (x\u0304\u2081 - x\u0304\u2082) / s_p")
    pdf.body("|d| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Method A: n\u2081=30, x\u0304\u2081=78.4, s\u2081=9.2. Method B: n\u2082=28, x\u0304\u2082=83.1, s\u2082=8.7. Test at \u03b1 = 0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 \u2260 0")
    pdf.bold_body("Pooled std dev")
    pdf.formula("s_p = \u221a[((29)(84.64) + (27)(75.69)) / 56] = \u221a[(2454.6+2043.6)/56] = \u221a80.33 = 8.963")
    pdf.bold_body("Test statistic")
    pdf.formula("t = (78.4-83.1) / [8.963 \u221a(1/30+1/28)] = -4.7 / (8.963\u00d70.2635) = -4.7/2.362 = -1.990")
    pdf.body("df = 30 + 28 - 2 = 56")
    pdf.bold_body("Critical value")
    pdf.body("t_{0.025, 56} \u2248 2.003")
    pdf.bold_body("P-value")
    pdf.body("p \u2248 0.0514")
    pdf.bold_body("Decision")
    pdf.body("|t|=1.990 < 2.003, p=0.051 > 0.05. Fail to reject H\u2080 (barely).")
    pdf.bold_body("CI")
    pdf.formula("CI = -4.7 \u00b1 2.003 \u00d7 2.362 = (-9.43, 0.03)")
    pdf.bold_body("Effect size")
    pdf.formula("d = -4.7 / 8.963 = -0.524")
    pdf.body("Medium effect.")
    pdf.bold_body("Conclusion")
    pdf.body("At \u03b1 = 0.05, there is not quite enough evidence to conclude a difference between the teaching methods (t = -1.99, p = 0.051). However, the effect size (d = -0.52) is medium, suggesting the difference may be practically meaningful. A larger sample might achieve significance.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the teaching methods differ in effectiveness when they actually do not.")
    pdf.body("Type II: Failing to detect a real difference between the methods.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Assuming equal variances without checking. Use an F-test first.")
    pdf.numbered(2, "Using this test on paired data instead of the paired t-test.")
    pdf.numbered(3, "Forgetting to use the pooled standard deviation.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Welch's T-Test: Use when the equal-variance assumption fails.")
    pdf.bullet("F-Test for Two Variances: Use to check the equal-variance assumption.")
    pdf.bullet("Mann-Whitney U: Nonparametric alternative when normality is violated.")
    pdf.bullet("Shapiro-Wilk Test: To verify normality.")

    pdf.save("two_sample_t_test_equal_var")

# ════════════════════════════════════════════════════════════════
#  6. WELCH'S T-TEST
# ════════════════════════════════════════════════════════════════
def gen_welchs():
    pdf = NotesPDF()
    title(pdf, "Welch's T-Test")
    pdf.section("Section 1: Introduction")
    pdf.body("Welch's t-test compares the means of two independent populations when the population standard deviations are unknown AND are not assumed to be equal. It is the default recommendation for comparing two independent means because it does not require the equal-variance assumption.")
    pdf.body("Scenario: A researcher compares anxiety scores between patients receiving therapy (n\u2081=22, x\u0304\u2081=38.5, s\u2081=7.2) versus a control group (n\u2082=18, x\u0304\u2082=44.3, s\u2082=12.1).")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 \u2260 0  (or one-tailed)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Samples are independent random samples.")
    pdf.numbered(2, "Both populations are approximately normal, or both n \u2265 30.")
    pdf.numbered(3, "Variances may be unequal (no equal-variance assumption required).")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("t = (x\u0304\u2081 - x\u0304\u2082) / \u221a(s\u2081\u00b2/n\u2081 + s\u2082\u00b2/n\u2082)")
    pdf.bold_body("Welch-Satterthwaite degrees of freedom:")
    pdf.formula("df = (s\u2081\u00b2/n\u2081 + s\u2082\u00b2/n\u2082)\u00b2 / [(s\u2081\u00b2/n\u2081)\u00b2/(n\u2081-1) + (s\u2082\u00b2/n\u2082)\u00b2/(n\u2082-1)]")
    pdf.body("Round df down to the nearest integer.")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if |t| > t_{\u03b1/2, df} or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = (x\u0304\u2081 - x\u0304\u2082) \u00b1 t_{\u03b1/2,df} \u00b7 \u221a(s\u2081\u00b2/n\u2081 + s\u2082\u00b2/n\u2082)")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's d = (x\u0304\u2081 - x\u0304\u2082) / \u221a[(s\u2081\u00b2 + s\u2082\u00b2)/2]")
    pdf.body("|d| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Therapy: n\u2081=22, x\u0304\u2081=38.5, s\u2081=7.2. Control: n\u2082=18, x\u0304\u2082=44.3, s\u2082=12.1. Test at \u03b1=0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03bc\u2081 - \u03bc\u2082 = 0     H\u2081: \u03bc\u2081 - \u03bc\u2082 \u2260 0")
    pdf.bold_body("Standard error")
    pdf.formula("SE = \u221a(7.2\u00b2/22 + 12.1\u00b2/18) = \u221a(2.3564 + 8.1339) = \u221a10.490 = 3.239")
    pdf.bold_body("Test statistic")
    pdf.formula("t = (38.5 - 44.3) / 3.239 = -5.8 / 3.239 = -1.790")
    pdf.bold_body("Degrees of freedom")
    pdf.formula("df = (10.490)\u00b2 / [(2.3564)\u00b2/21 + (8.1339)\u00b2/17] = 110.04 / (0.2644 + 3.891) = 110.04/4.155 = 26.5")
    pdf.body("df \u2248 26")
    pdf.bold_body("Critical value")
    pdf.body("t_{0.025, 26} = 2.056")
    pdf.bold_body("P-value")
    pdf.body("p \u2248 0.0852")
    pdf.bold_body("Decision")
    pdf.body("|t| = 1.790 < 2.056, p = 0.085 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("CI")
    pdf.formula("CI = -5.8 \u00b1 2.056 \u00d7 3.239 = (-12.46, 0.86)")
    pdf.body("0 is in the interval.")
    pdf.bold_body("Effect size")
    pdf.formula("d = -5.8 / \u221a[(51.84+146.41)/2] = -5.8 / 9.963 = -0.582")
    pdf.body("Medium effect.")
    pdf.bold_body("Conclusion")
    pdf.body("At \u03b1 = 0.05, we do not have sufficient evidence that therapy reduces anxiety scores compared to the control (t = -1.79, p = 0.085). However, Cohen's d = -0.58 indicates a medium effect, suggesting a potentially meaningful reduction that may be detectable with a larger sample.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding therapy reduces anxiety when it does not.")
    pdf.body("Type II: Failing to detect that therapy reduces anxiety when it truly does.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using the pooled t-test when variances are clearly unequal.")
    pdf.numbered(2, "Computing degrees of freedom as n\u2081+n\u2082-2 (that's for the pooled test).")
    pdf.numbered(3, "Applying this to paired/matched data instead of the paired t-test.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Two-Sample T-Test (Equal Var): Use when variances are confirmed equal.")
    pdf.bullet("Mann-Whitney U: Nonparametric alternative.")

    pdf.save("welchs_t_test")

# ════════════════════════════════════════════════════════════════
#  7. PAIRED T-TEST
# ════════════════════════════════════════════════════════════════
def gen_paired_t():
    pdf = NotesPDF()
    title(pdf, "Paired T-Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The paired t-test compares the means of two related measurements on the same subjects (or matched pairs). It tests whether the mean difference between paired observations equals zero.")
    pdf.body("Scenario: A fitness trainer measures the resting heart rate of 15 participants before and after an 8-week training programme to determine whether the programme reduces heart rate.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("Let d = before - after (or measurement 1 - measurement 2).")
    pdf.bold_body("Two-tailed:")
    pdf.body("H\u2080: \u03bc_d = 0     H\u2081: \u03bc_d \u2260 0")
    pdf.bold_body("Left-tailed:")
    pdf.body("H\u2080: \u03bc_d = 0     H\u2081: \u03bc_d < 0")
    pdf.bold_body("Right-tailed:")
    pdf.body("H\u2080: \u03bc_d = 0     H\u2081: \u03bc_d > 0")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "The data consist of paired observations (before/after, matched subjects).")
    pdf.numbered(2, "The differences d_i are approximately normally distributed (or n \u2265 30).")
    pdf.numbered(3, "The pairs are independent of each other.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("t = d\u0304 / (s_d / \u221an)")
    pdf.body("Where d\u0304 = mean of the differences, s_d = standard deviation of the differences, n = number of pairs.")
    pdf.formula("df = n - 1")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if |t| > t_{\u03b1/2, df} (two-tailed) or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = d\u0304 \u00b1 t_{\u03b1/2, df} \u00b7 s_d/\u221an")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's d = d\u0304 / s_d")
    pdf.body("|d| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("15 participants' resting heart rates before and after training. Differences (before - after): 5, 3, 8, 2, 6, 4, 7, 1, 5, 3, 9, 4, 6, 2, 5. Test at \u03b1 = 0.05 whether the programme reduces heart rate.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03bc_d = 0     H\u2081: \u03bc_d > 0  (right-tailed, since positive d means reduction)")
    pdf.bold_body("Compute differences")
    pdf.body("d\u0304 = (5+3+8+2+6+4+7+1+5+3+9+4+6+2+5)/15 = 70/15 = 4.667")
    pdf.body("s_d = 2.289  (computed from the differences)")
    pdf.bold_body("Test statistic")
    pdf.formula("t = 4.667 / (2.289/\u221a15) = 4.667 / 0.591 = 7.897")
    pdf.body("df = 14")
    pdf.bold_body("Critical value")
    pdf.body("t_{0.05, 14} = 1.761 (one-tailed)")
    pdf.bold_body("P-value")
    pdf.body("p < 0.0001")
    pdf.bold_body("Decision")
    pdf.body("t = 7.897 >> 1.761, p < 0.0001 < 0.05. Reject H\u2080.")
    pdf.bold_body("CI (95%)")
    pdf.formula("CI = 4.667 \u00b1 2.145 \u00d7 0.591 = (3.399, 5.935)")
    pdf.body("The entire CI is above 0.")
    pdf.bold_body("Effect size")
    pdf.formula("d = 4.667 / 2.289 = 2.039")
    pdf.body("Very large effect.")
    pdf.bold_body("Conclusion")
    pdf.body("The training programme significantly reduced resting heart rate (t = 7.90, p < 0.0001, df = 14). The mean reduction was 4.67 bpm with a 95% CI of (3.40, 5.94). Cohen's d = 2.04 indicates a very large effect.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the training programme reduces heart rate when it actually does not.")
    pdf.body("Type II: Failing to detect that the training programme reduces heart rate when it actually does.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using an independent two-sample t-test on paired data. This ignores the pairing and loses power.")
    pdf.numbered(2, "Defining differences inconsistently. Always state the direction (before - after, etc.).")
    pdf.numbered(3, "Ignoring outliers in the differences. Check with a boxplot or Shapiro-Wilk test.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Sample T-Test: The paired t-test is equivalent to a one-sample t-test on the differences.")
    pdf.bullet("Wilcoxon Signed-Rank Test: Nonparametric alternative when differences are not normal.")
    pdf.bullet("Sign Test: Nonparametric alternative for ordinal data.")

    pdf.save("paired_t_test")

# ════════════════════════════════════════════════════════════════
#  8. TWO-PROPORTION Z-TEST
# ════════════════════════════════════════════════════════════════
def gen_two_prop():
    pdf = NotesPDF()
    title(pdf, "Two-Proportion Z-Test")
    pdf.section("Section 1: Introduction")
    pdf.body("The two-proportion z-test compares proportions from two independent populations to determine whether they differ. It is used when both samples are large enough for the normal approximation.")
    pdf.body("Scenario: A marketing team tests two ad designs. Ad A was shown to 300 users (78 clicked) and Ad B to 350 users (105 clicked). Is there a difference in click-through rates?")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: p\u2081 - p\u2082 = 0     H\u2081: p\u2081 - p\u2082 \u2260 0  (or one-tailed)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Independent random samples from two populations.")
    pdf.numbered(2, "n\u2081p\u0302 \u2265 5, n\u2081(1-p\u0302) \u2265 5, n\u2082p\u0302 \u2265 5, n\u2082(1-p\u0302) \u2265 5.")
    pdf.numbered(3, "Samples are independent of each other.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("z = (p\u0302\u2081 - p\u0302\u2082) / \u221a[p\u0302(1-p\u0302)(1/n\u2081 + 1/n\u2082)]")
    pdf.bold_body("Pooled proportion:")
    pdf.formula("p\u0302 = (x\u2081 + x\u2082) / (n\u2081 + n\u2082)")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if |z| > z_{\u03b1/2} or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = (p\u0302\u2081 - p\u0302\u2082) \u00b1 z_{\u03b1/2} \u221a[p\u0302\u2081(1-p\u0302\u2081)/n\u2081 + p\u0302\u2082(1-p\u0302\u2082)/n\u2082]")
    pdf.body("Note: the CI uses individual sample proportions, not the pooled proportion.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's h = 2 arcsin(\u221ap\u0302\u2081) - 2 arcsin(\u221ap\u0302\u2082)")
    pdf.body("|h| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Ad A: n\u2081=300, x\u2081=78. Ad B: n\u2082=350, x\u2082=105. Test at \u03b1=0.05.")
    pdf.body("p\u0302\u2081 = 78/300 = 0.260, p\u0302\u2082 = 105/350 = 0.300")
    pdf.bold_body("Pooled proportion")
    pdf.formula("p\u0302 = (78+105)/(300+350) = 183/650 = 0.2815")
    pdf.bold_body("Test statistic")
    pdf.formula("SE = \u221a[0.2815 \u00d7 0.7185 \u00d7 (1/300+1/350)] = \u221a[0.2023 \u00d7 0.006190] = \u221a0.001252 = 0.03539")
    pdf.formula("z = (0.260 - 0.300) / 0.03539 = -0.040 / 0.03539 = -1.130")
    pdf.bold_body("Decision")
    pdf.body("|z| = 1.130 < 1.960, p = 0.258 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("CI")
    pdf.formula("SE_CI = \u221a[0.26\u00d70.74/300 + 0.30\u00d70.70/350] = 0.03516")
    pdf.formula("CI = -0.040 \u00b1 1.960 \u00d7 0.03516 = (-0.109, 0.029)")
    pdf.bold_body("Effect size")
    pdf.body("h = 2 arcsin(\u221a0.26) - 2 arcsin(\u221a0.30) = -0.089. Very small effect.")
    pdf.bold_body("Conclusion")
    pdf.body("No significant difference in click-through rates between the two ads (z = -1.13, p = 0.258). The 95% CI for the difference (-10.9% to +2.9%) includes zero.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding click-through rates differ when they actually do not.")
    pdf.body("Type II: Failing to detect a real difference in click-through rates.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using individual proportions instead of the pooled proportion in the test statistic.")
    pdf.numbered(2, "Using the pooled proportion in the CI (it should use individual proportions).")
    pdf.numbered(3, "Applying this test when expected counts are very small. Use Fisher's exact test instead.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Sample Proportion Z-Test: For testing a single proportion.")
    pdf.bullet("Chi-Square Test of Independence: Equivalent for 2x2 tables; extends to larger tables.")
    pdf.bullet("Fisher's Exact Test: Use when sample sizes are small.")

    pdf.save("two_proportion_z_test")

if __name__ == "__main__":
    gen_two_sample_z()
    gen_two_sample_t_eq()
    gen_welchs()
    gen_paired_t()
    gen_two_prop()
    print("\nAll 5 two-sample test PDFs generated.")
