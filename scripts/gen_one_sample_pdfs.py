"""Generate _notes.pdf for 3 one-sample hypothesis tests."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import NotesPDF

def _hyp_test_pdf(pdf, title, subtitle="Undergraduate Statistics - Lecture Notes"):
    pdf.add_title(title, subtitle)

# ════════════════════════════════════════════════════════════════
#  1. ONE-SAMPLE Z-TEST
# ════════════════════════════════════════════════════════════════
def gen_one_sample_z():
    pdf = NotesPDF()
    _hyp_test_pdf(pdf, "One-Sample Z-Test")

    # S1 Intro
    pdf.section("Section 1: Introduction")
    pdf.body(
        "The one-sample z-test is used to determine whether the mean of a "
        "population differs from a hypothesised value when the population "
        "standard deviation (\u03c3) is known. This is one of the simplest "
        "hypothesis tests and serves as the foundation for understanding "
        "more complex tests."
    )
    pdf.body(
        "Real-world scenario: A bottling company claims its machines fill "
        "bottles with an average of 500 mL of water. The population "
        "standard deviation is known to be 8 mL from long-term quality "
        "records. A quality inspector samples 40 bottles and wants to test "
        "whether the true mean fill volume equals 500 mL."
    )

    # S2 Hypotheses
    pdf.section("Section 2: Hypotheses")
    pdf.bold_body("Two-tailed test:")
    pdf.body("H\u2080: \u03bc = \u03bc\u2080   (the population mean equals the hypothesised value)")
    pdf.body("H\u2081: \u03bc \u2260 \u03bc\u2080   (the population mean differs from the hypothesised value)")
    pdf.bold_body("Left-tailed test:")
    pdf.body("H\u2080: \u03bc = \u03bc\u2080      H\u2081: \u03bc < \u03bc\u2080")
    pdf.body("We believe the true mean is less than the hypothesised value.")
    pdf.bold_body("Right-tailed test:")
    pdf.body("H\u2080: \u03bc = \u03bc\u2080      H\u2081: \u03bc > \u03bc\u2080")
    pdf.body("We believe the true mean is greater than the hypothesised value.")

    # S3 Assumptions
    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "The population standard deviation \u03c3 is known. If \u03c3 is unknown, use the one-sample t-test instead.")
    pdf.numbered(2, "The sample is a simple random sample from the population.")
    pdf.numbered(3, "The population is normally distributed, OR the sample size is large (n \u2265 30) so the Central Limit Theorem applies.")
    pdf.numbered(4, "Observations are independent of each other.")

    # S4 Test Statistic
    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("z = (x\u0304 - \u03bc\u2080) / (\u03c3 / \u221an)")
    pdf.body("Where:")
    pdf.bullet("x\u0304 = sample mean")
    pdf.bullet("\u03bc\u2080 = hypothesised population mean")
    pdf.bullet("\u03c3 = known population standard deviation")
    pdf.bullet("n = sample size")
    pdf.body("Degrees of freedom: Not applicable (the z-test uses the standard normal distribution).")

    # S5 Decision Rule
    pdf.section("Section 5: Decision Rule")
    pdf.bold_body("Critical Value Approach")
    pdf.body(
        "Two-tailed: Reject H\u2080 if |z| > z_{\u03b1/2}. "
        "Left-tailed: Reject H\u2080 if z < -z_\u03b1. "
        "Right-tailed: Reject H\u2080 if z > z_\u03b1."
    )
    pdf.body("Common critical values: \u03b1=0.05 two-tailed: z=\u00b11.960; \u03b1=0.01 two-tailed: z=\u00b12.576.")
    pdf.bold_body("P-value Approach")
    pdf.body(
        "Two-tailed: p-value = 2 \u00d7 P(Z > |z|). "
        "Left-tailed: p-value = P(Z < z). "
        "Right-tailed: p-value = P(Z > z). "
        "Reject H\u2080 if p-value < \u03b1."
    )

    # S6 Confidence Interval
    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = x\u0304 \u00b1 z_{\u03b1/2} \u00b7 \u03c3/\u221an")
    pdf.body(
        "If the hypothesised value \u03bc\u2080 falls outside this interval, "
        "we reject H\u2080. The CI and two-tailed test at significance level "
        "\u03b1 always give the same conclusion."
    )

    # S7 Effect Size
    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's d = (x\u0304 - \u03bc\u2080) / \u03c3")
    pdf.body("Interpretation: |d| = 0.2 small, 0.5 medium, 0.8 large.")
    pdf.body(
        "Effect size tells us the practical significance of the result. "
        "A statistically significant result with a small effect size may "
        "not be meaningful in practice."
    )

    # S8 Worked Example
    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body(
        "A bottling company claims its machines fill bottles with a mean of "
        "500 mL. The population standard deviation is \u03c3 = 8 mL. An "
        "inspector measures 40 randomly selected bottles and finds a sample "
        "mean of x\u0304 = 497.5 mL. Test whether the true mean differs from "
        "500 mL at \u03b1 = 0.05."
    )
    pdf.bold_body("Step 1: State the problem")
    pdf.body("We want to know if the machine's average fill volume has changed from 500 mL.")
    pdf.bold_body("Step 2: Identify the test")
    pdf.body("One-sample z-test (population \u03c3 is known, n = 40 \u2265 30).")
    pdf.bold_body("Step 3: State hypotheses")
    pdf.body("H\u2080: \u03bc = 500     H\u2081: \u03bc \u2260 500  (two-tailed)")
    pdf.bold_body("Step 4: Set significance level")
    pdf.body("\u03b1 = 0.05")
    pdf.bold_body("Step 5: Compute test statistic")
    pdf.formula("z = (497.5 - 500) / (8 / \u221a40) = -2.5 / 1.2649 = -1.976")
    pdf.bold_body("Step 6: Find critical value")
    pdf.body("For \u03b1 = 0.05 two-tailed: z_crit = \u00b11.960")
    pdf.bold_body("Step 7: Compute p-value")
    pdf.body("p-value = 2 \u00d7 P(Z < -1.976) = 2 \u00d7 0.0241 = 0.0482")
    pdf.bold_body("Step 8: Decision")
    pdf.body("|z| = 1.976 > 1.960, and p-value = 0.0482 < 0.05. Reject H\u2080.")
    pdf.bold_body("Step 9: Confidence interval")
    pdf.formula("CI = 497.5 \u00b1 1.960 \u00d7 (8/\u221a40) = 497.5 \u00b1 2.480 = (495.02, 499.98)")
    pdf.body("500 is outside this interval, consistent with rejecting H\u2080.")
    pdf.bold_body("Step 10: Effect size")
    pdf.formula("d = (497.5 - 500) / 8 = -0.3125")
    pdf.body("Small-to-medium effect (|d| = 0.31).")
    pdf.bold_body("Step 11: Conclusion")
    pdf.body(
        "At the 5% significance level, there is sufficient evidence that the "
        "true mean fill volume differs from 500 mL. The sample mean of 497.5 mL "
        "is significantly below the target (z = -1.976, p = 0.048). The 95% CI "
        "(495.02, 499.98) does not contain 500 mL. The effect size (d = -0.31) "
        "indicates a small-to-medium practical difference."
    )

    # S9 Type I / II Errors
    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body(
        "Type I error: Concluding that the mean fill volume differs from "
        "500 mL when it actually equals 500 mL (false alarm)."
    )
    pdf.body(
        "Type II error: Failing to detect that the mean fill volume differs "
        "from 500 mL when it actually has changed (missed finding)."
    )

    # S10 Common Mistakes
    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using the z-test when \u03c3 is unknown. If you only have the sample standard deviation s, use the t-test.")
    pdf.numbered(2, "Forgetting to check the normality/sample-size condition. For small n with non-normal data, the z-test is not appropriate.")
    pdf.numbered(3, "Confusing one-tailed and two-tailed p-values. A two-tailed p-value is double the one-tailed p-value.")
    pdf.numbered(4, "Interpreting 'fail to reject H\u2080' as proof that H\u2080 is true. We simply lack evidence to reject it.")

    # S11 Related Tests
    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Sample T-Test: Use when \u03c3 is unknown and must be estimated by s.")
    pdf.bullet("Shapiro-Wilk Test: Use to verify the normality assumption before applying the z-test.")

    pdf.save("one_sample_z_test")

# ════════════════════════════════════════════════════════════════
#  2. ONE-SAMPLE T-TEST
# ════════════════════════════════════════════════════════════════
def gen_one_sample_t():
    pdf = NotesPDF()
    _hyp_test_pdf(pdf, "One-Sample T-Test")

    pdf.section("Section 1: Introduction")
    pdf.body(
        "The one-sample t-test is used to determine whether the mean of a "
        "population differs from a hypothesised value when the population "
        "standard deviation is UNKNOWN and must be estimated from the sample. "
        "This is the most commonly used version because \u03c3 is rarely known "
        "in practice."
    )
    pdf.body(
        "Real-world scenario: A battery manufacturer claims its AA batteries "
        "last an average of 48 hours of continuous use. A consumer group "
        "tests 25 randomly selected batteries and records their lifespans "
        "to determine if the claim is accurate."
    )

    pdf.section("Section 2: Hypotheses")
    pdf.bold_body("Two-tailed:")
    pdf.body("H\u2080: \u03bc = \u03bc\u2080     H\u2081: \u03bc \u2260 \u03bc\u2080")
    pdf.bold_body("Left-tailed:")
    pdf.body("H\u2080: \u03bc = \u03bc\u2080     H\u2081: \u03bc < \u03bc\u2080")
    pdf.bold_body("Right-tailed:")
    pdf.body("H\u2080: \u03bc = \u03bc\u2080     H\u2081: \u03bc > \u03bc\u2080")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "The population standard deviation \u03c3 is UNKNOWN. (If known, use the z-test.)")
    pdf.numbered(2, "The sample is a simple random sample.")
    pdf.numbered(3, "The population is approximately normal, OR n \u2265 30. For 15 \u2264 n < 30, the data should be roughly symmetric with no strong outliers. For n < 15, normality should be checked (e.g., Shapiro-Wilk test).")
    pdf.numbered(4, "Observations are independent.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("t = (x\u0304 - \u03bc\u2080) / (s / \u221an)")
    pdf.body("Where:")
    pdf.bullet("x\u0304 = sample mean")
    pdf.bullet("\u03bc\u2080 = hypothesised population mean")
    pdf.bullet("s = sample standard deviation")
    pdf.bullet("n = sample size")
    pdf.bold_body("Degrees of Freedom")
    pdf.formula("df = n - 1")

    pdf.section("Section 5: Decision Rule")
    pdf.bold_body("Critical Value Approach")
    pdf.body("Two-tailed: Reject H\u2080 if |t| > t_{\u03b1/2, df}.")
    pdf.body("Left-tailed: Reject H\u2080 if t < -t_{\u03b1, df}.")
    pdf.body("Right-tailed: Reject H\u2080 if t > t_{\u03b1, df}.")
    pdf.bold_body("P-value Approach")
    pdf.body("Compute the p-value from the t-distribution with df = n - 1. Reject H\u2080 if p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = x\u0304 \u00b1 t_{\u03b1/2, df} \u00b7 s/\u221an")
    pdf.body("If \u03bc\u2080 falls outside the CI, reject H\u2080 (for a two-tailed test at the same \u03b1).")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's d = (x\u0304 - \u03bc\u2080) / s")
    pdf.body("Interpretation: |d| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body(
        "A battery manufacturer claims AA batteries last \u03bc\u2080 = 48 hours. "
        "A consumer group tests n = 25 batteries and finds x\u0304 = 46.2 hours "
        "with s = 4.1 hours. Test whether the true mean differs from 48 hours "
        "at \u03b1 = 0.05."
    )
    pdf.bold_body("Step 1: State hypotheses")
    pdf.body("H\u2080: \u03bc = 48     H\u2081: \u03bc \u2260 48  (two-tailed)")
    pdf.bold_body("Step 2: Identify the test")
    pdf.body("One-sample t-test (\u03c3 unknown, n = 25).")
    pdf.bold_body("Step 3: Set significance level")
    pdf.body("\u03b1 = 0.05")
    pdf.bold_body("Step 4: Compute test statistic")
    pdf.formula("t = (46.2 - 48) / (4.1 / \u221a25) = -1.8 / 0.82 = -2.195")
    pdf.bold_body("Step 5: Degrees of freedom")
    pdf.formula("df = 25 - 1 = 24")
    pdf.bold_body("Step 6: Find critical value")
    pdf.body("t_{0.025, 24} = 2.064")
    pdf.bold_body("Step 7: Compute p-value")
    pdf.body("p-value = 2 \u00d7 P(t < -2.195 | df=24) = 2 \u00d7 0.0189 = 0.0378")
    pdf.bold_body("Step 8: Decision")
    pdf.body("|t| = 2.195 > 2.064, p-value = 0.0378 < 0.05. Reject H\u2080.")
    pdf.bold_body("Step 9: Confidence interval")
    pdf.formula("CI = 46.2 \u00b1 2.064 \u00d7 0.82 = 46.2 \u00b1 1.692 = (44.508, 47.892)")
    pdf.body("48 is outside the CI, consistent with rejecting H\u2080.")
    pdf.bold_body("Step 10: Effect size")
    pdf.formula("d = (46.2 - 48) / 4.1 = -0.439")
    pdf.body("Medium effect (|d| = 0.44).")
    pdf.bold_body("Step 11: Conclusion")
    pdf.body(
        "At the 5% significance level, there is sufficient evidence that the "
        "mean battery lifespan differs from 48 hours. The sample mean of 46.2 "
        "hours is significantly below the claim (t = -2.195, p = 0.038). The "
        "95% CI (44.51, 47.89) excludes 48 hours. Cohen's d = -0.44 indicates "
        "a medium practical effect."
    )

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I error: Concluding the mean battery lifespan differs from 48 hours when it actually equals 48 hours.")
    pdf.body("Type II error: Failing to detect that the mean battery lifespan differs from 48 hours when it actually does.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using the z-test when \u03c3 is unknown. Always use the t-test with s.")
    pdf.numbered(2, "Ignoring outliers. The t-test is sensitive to outliers, especially with small samples.")
    pdf.numbered(3, "Using the wrong degrees of freedom. For a one-sample t-test, df = n - 1, not n.")
    pdf.numbered(4, "Confusing statistical significance with practical significance. Always report the effect size.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("One-Sample Z-Test: Use when \u03c3 is known.")
    pdf.bullet("Paired T-Test: Use when data come in matched pairs.")
    pdf.bullet("Shapiro-Wilk Test: Use to verify normality before applying the t-test.")
    pdf.bullet("Wilcoxon Signed-Rank Test: Nonparametric alternative when normality is violated.")

    pdf.save("one_sample_t_test")

# ════════════════════════════════════════════════════════════════
#  3. ONE-SAMPLE PROPORTION Z-TEST
# ════════════════════════════════════════════════════════════════
def gen_one_sample_prop():
    pdf = NotesPDF()
    _hyp_test_pdf(pdf, "One-Sample Proportion Z-Test")

    pdf.section("Section 1: Introduction")
    pdf.body(
        "The one-sample proportion z-test is used to determine whether a "
        "population proportion p differs from a hypothesised value p\u2080. "
        "It applies when the data are categorical with two outcomes (success "
        "or failure) and the sample size is large enough for the normal "
        "approximation to the binomial distribution."
    )
    pdf.body(
        "Real-world scenario: A university claims that 70% of its graduates "
        "find employment within 6 months. A survey of 200 recent graduates "
        "finds that 128 (64%) secured jobs. Is there evidence the true rate "
        "differs from 70%?"
    )

    pdf.section("Section 2: Hypotheses")
    pdf.bold_body("Two-tailed:")
    pdf.body("H\u2080: p = p\u2080     H\u2081: p \u2260 p\u2080")
    pdf.bold_body("Left-tailed:")
    pdf.body("H\u2080: p = p\u2080     H\u2081: p < p\u2080")
    pdf.bold_body("Right-tailed:")
    pdf.body("H\u2080: p = p\u2080     H\u2081: p > p\u2080")
    pdf.body("Where p is the true population proportion and p\u2080 is the hypothesised value.")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "The sample is a simple random sample.")
    pdf.numbered(2, "There are only two outcomes (success/failure).")
    pdf.numbered(3, "np\u2080 \u2265 10 and n(1 - p\u2080) \u2265 10 (large-sample condition for normal approximation).")
    pdf.numbered(4, "Observations are independent. If sampling without replacement, n should be \u2264 10% of the population.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("z = (p\u0302 - p\u2080) / \u221a[p\u2080(1 - p\u2080)/n]")
    pdf.body("Where:")
    pdf.bullet("p\u0302 = x/n = sample proportion (x = number of successes)")
    pdf.bullet("p\u2080 = hypothesised population proportion")
    pdf.bullet("n = sample size")
    pdf.body("Note: The standard error uses p\u2080 (not p\u0302) because we assume H\u2080 is true when computing the test statistic.")

    pdf.section("Section 5: Decision Rule")
    pdf.bold_body("Critical Value Approach")
    pdf.body("Two-tailed: Reject H\u2080 if |z| > z_{\u03b1/2}.")
    pdf.body("One-tailed: Reject H\u2080 if z < -z_\u03b1 (left) or z > z_\u03b1 (right).")
    pdf.bold_body("P-value Approach")
    pdf.body("Compute p-value from the standard normal. Reject H\u2080 if p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = p\u0302 \u00b1 z_{\u03b1/2} \u00b7 \u221a[p\u0302(1 - p\u0302)/n]")
    pdf.body("Note: The CI uses p\u0302 in the standard error (not p\u2080), unlike the test statistic.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("Cohen's h = 2 arcsin(\u221ap\u0302) - 2 arcsin(\u221ap\u2080)")
    pdf.body("Interpretation: |h| = 0.2 small, 0.5 medium, 0.8 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body(
        "A university claims 70% of graduates find jobs within 6 months. "
        "Of 200 surveyed graduates, 128 found employment. Test at \u03b1 = 0.05."
    )
    pdf.bold_body("Step 1: Hypotheses")
    pdf.body("H\u2080: p = 0.70     H\u2081: p \u2260 0.70  (two-tailed)")
    pdf.bold_body("Step 2: Check conditions")
    pdf.body("np\u2080 = 200(0.70) = 140 \u2265 10  \u2713     n(1-p\u2080) = 200(0.30) = 60 \u2265 10  \u2713")
    pdf.bold_body("Step 3: Compute sample proportion")
    pdf.formula("p\u0302 = 128/200 = 0.64")
    pdf.bold_body("Step 4: Compute test statistic")
    pdf.formula("z = (0.64 - 0.70) / \u221a[0.70 \u00d7 0.30 / 200]")
    pdf.formula("  = -0.06 / \u221a(0.00105) = -0.06 / 0.03240 = -1.852")
    pdf.bold_body("Step 5: Critical value")
    pdf.body("z_{0.025} = 1.960")
    pdf.bold_body("Step 6: P-value")
    pdf.body("p-value = 2 \u00d7 P(Z < -1.852) = 2 \u00d7 0.0321 = 0.0642")
    pdf.bold_body("Step 7: Decision")
    pdf.body("|z| = 1.852 < 1.960, p-value = 0.0642 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Step 8: Confidence interval")
    pdf.formula("CI = 0.64 \u00b1 1.960 \u00d7 \u221a(0.64 \u00d7 0.36 / 200) = 0.64 \u00b1 0.0665")
    pdf.formula("CI = (0.5735, 0.7065)")
    pdf.body("0.70 is inside the CI, consistent with failing to reject H\u2080.")
    pdf.bold_body("Step 9: Effect size")
    pdf.body("h = 2 arcsin(\u221a0.64) - 2 arcsin(\u221a0.70) = 2(0.9273) - 2(0.9911) = 1.8546 - 1.9823 = -0.128")
    pdf.body("|h| = 0.13, small effect.")
    pdf.bold_body("Step 10: Conclusion")
    pdf.body(
        "At the 5% significance level, there is insufficient evidence that "
        "the true employment rate differs from 70%. The sample proportion of "
        "64% is not significantly different (z = -1.852, p = 0.064). The "
        "95% CI (57.4%, 70.7%) includes 70%. The effect size is small (h = -0.13)."
    )

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I error: Concluding the employment rate differs from 70% when it actually is 70%.")
    pdf.body("Type II error: Failing to detect that the employment rate differs from 70% when it actually does.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using p\u0302 instead of p\u2080 in the standard error of the test statistic. The test assumes H\u2080 is true.")
    pdf.numbered(2, "Applying the test when np\u2080 or n(1-p\u2080) is less than 10. The normal approximation is unreliable.")
    pdf.numbered(3, "Forgetting that the CI uses p\u0302 while the test statistic uses p\u2080 for the standard error.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Two-Proportion Z-Test: Use when comparing proportions between two groups.")
    pdf.bullet("Chi-Square Goodness-of-Fit: Use when testing proportions across multiple categories (more than 2).")

    pdf.save("one_sample_proportion_z_test")


if __name__ == "__main__":
    gen_one_sample_z()
    gen_one_sample_t()
    gen_one_sample_prop()
    print("\nAll 3 one-sample test PDFs generated.")
