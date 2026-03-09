"""Generate _notes.pdf for 3 regression/correlation + 2 variance tests."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import NotesPDF

def title(pdf, t):
    pdf.add_title(t, "Undergraduate Statistics - Lecture Notes")

# ════════════════════════════════════════════════════════════════
#  19. CORRELATION T-TEST
# ════════════════════════════════════════════════════════════════
def gen_corr_t():
    pdf = NotesPDF()
    title(pdf, "T-Test for Correlation Coefficient")
    pdf.section("Section 1: Introduction")
    pdf.body("The correlation t-test determines whether the population Pearson correlation coefficient \u03c1 equals zero. A significant result means there is a linear association between two quantitative variables. This test does NOT determine causation.")
    pdf.body("Scenario: An education researcher collects data on weekly study hours and GPA for 30 university students to test whether there is a linear relationship.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: \u03c1 = 0  (no linear correlation)")
    pdf.body("H\u2081: \u03c1 \u2260 0  (two-tailed) or \u03c1 > 0 or \u03c1 < 0")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Both variables are quantitative and continuous.")
    pdf.numbered(2, "The pair (X, Y) follows a bivariate normal distribution.")
    pdf.numbered(3, "Observations are independent.")
    pdf.numbered(4, "The relationship is linear (check with a scatterplot).")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("t = r\u221a(n-2) / \u221a(1-r\u00b2)")
    pdf.body("r = sample Pearson correlation coefficient, n = number of pairs.")
    pdf.formula("df = n - 2")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if |t| > t_{\u03b1/2, n-2} or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("Use Fisher's z-transformation for a CI for \u03c1:")
    pdf.formula("z_r = 0.5 ln[(1+r)/(1-r)]")
    pdf.formula("SE = 1/\u221a(n-3)")
    pdf.formula("CI_z = z_r \u00b1 z_{\u03b1/2} / \u221a(n-3)")
    pdf.body("Back-transform: r = (e^(2z) - 1) / (e^(2z) + 1)")

    pdf.section("Section 7: Effect Size")
    pdf.formula("r\u00b2 = coefficient of determination")
    pdf.body("r\u00b2 tells us the proportion of variance in Y explained by X.")
    pdf.body("r\u00b2 = 0.01 small, 0.09 medium, 0.25 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("n = 30 students. Sample correlation r = 0.52 between study hours and GPA. Test at \u03b1 = 0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03c1 = 0     H\u2081: \u03c1 \u2260 0")
    pdf.bold_body("Test statistic")
    pdf.formula("t = 0.52\u221a28 / \u221a(1-0.2704) = 0.52(5.292) / \u221a0.7296 = 2.752 / 0.854 = 3.222")
    pdf.body("df = 28")
    pdf.bold_body("Critical value")
    pdf.body("t_{0.025, 28} = 2.048")
    pdf.bold_body("P-value")
    pdf.body("p = 0.0032")
    pdf.bold_body("Decision")
    pdf.body("|t| = 3.222 > 2.048, p = 0.003 < 0.05. Reject H\u2080.")
    pdf.bold_body("Confidence interval for \u03c1")
    pdf.body("z_r = 0.5 ln(1.52/0.48) = 0.5766")
    pdf.formula("CI_z = 0.5766 \u00b1 1.960/\u221a27 = (0.199, 0.954)")
    pdf.body("Back-transform: CI for \u03c1 = (0.197, 0.740)")
    pdf.bold_body("Effect size")
    pdf.formula("r\u00b2 = 0.52\u00b2 = 0.2704")
    pdf.body("Large effect: 27% of the variance in GPA is explained by study hours.")
    pdf.bold_body("Conclusion")
    pdf.body("There is a significant positive correlation between study hours and GPA (r = 0.52, t = 3.22, p = 0.003). Study hours explain about 27% of the variance in GPA.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding there is a correlation between study hours and GPA when there is none.")
    pdf.body("Type II: Failing to detect a real correlation between study hours and GPA.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Assuming correlation implies causation.")
    pdf.numbered(2, "Using Pearson's r when the relationship is non-linear. Check with a scatterplot.")
    pdf.numbered(3, "Ignoring outliers, which can strongly inflate or deflate r.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Regression Slope T-Test: Equivalent test for simple linear regression.")
    pdf.bullet("Regression F-Test: Tests overall model significance.")

    pdf.save("correlation_t_test")

# ════════════════════════════════════════════════════════════════
#  20. REGRESSION SLOPE T-TEST
# ════════════════════════════════════════════════════════════════
def gen_reg_slope():
    pdf = NotesPDF()
    title(pdf, "T-Test for Regression Slope")
    pdf.section("Section 1: Introduction")
    pdf.body("The regression slope t-test determines whether the slope (\u03b2\u2081) of a simple linear regression is significantly different from zero. If \u03b2\u2081 = 0, the predictor X has no linear effect on the response Y. This test is equivalent to the correlation t-test for simple linear regression.")
    pdf.body("Scenario: A marketing analyst examines whether advertising spend (in thousands) predicts monthly sales revenue (in thousands) for 25 months.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: \u03b2\u2081 = 0  (no linear relationship)")
    pdf.body("H\u2081: \u03b2\u2081 \u2260 0  (or > 0 or < 0)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Linearity: The relationship between X and Y is linear.")
    pdf.numbered(2, "Independence: Observations are independent.")
    pdf.numbered(3, "Normality: Residuals are normally distributed.")
    pdf.numbered(4, "Equal variance (homoscedasticity): The spread of residuals is constant across X values.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("t = b\u2081 / SE(b\u2081)")
    pdf.body("b\u2081 = sample slope, SE(b\u2081) = standard error of the slope.")
    pdf.formula("SE(b\u2081) = s / \u221a[\u2211(x_i - x\u0304)\u00b2]")
    pdf.body("where s = \u221a[SSE/(n-2)] is the residual standard error.")
    pdf.formula("df = n - 2")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if |t| > t_{\u03b1/2, n-2} or p-value < \u03b1.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI = b\u2081 \u00b1 t_{\u03b1/2, n-2} \u00d7 SE(b\u2081)")

    pdf.section("Section 7: Effect Size")
    pdf.formula("R\u00b2 = 1 - SSE/SST")
    pdf.body("R\u00b2 is the coefficient of determination: the proportion of variance in Y explained by X.")
    pdf.body("R\u00b2 = 0.01 small, 0.09 medium, 0.25 large.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("n=25, b\u2081 = 2.35 (each $1K in ads yields $2.35K in sales), SE(b\u2081) = 0.64, R\u00b2 = 0.36. Test at \u03b1=0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03b2\u2081 = 0     H\u2081: \u03b2\u2081 \u2260 0")
    pdf.bold_body("Test statistic")
    pdf.formula("t = 2.35 / 0.64 = 3.672")
    pdf.body("df = 25 - 2 = 23")
    pdf.bold_body("Critical value")
    pdf.body("t_{0.025, 23} = 2.069")
    pdf.bold_body("P-value")
    pdf.body("p = 0.0013")
    pdf.bold_body("Decision")
    pdf.body("|t| = 3.672 > 2.069, p = 0.001 < 0.05. Reject H\u2080.")
    pdf.bold_body("Confidence interval")
    pdf.formula("CI = 2.35 \u00b1 2.069 \u00d7 0.64 = (1.026, 3.674)")
    pdf.body("The CI does not contain 0.")
    pdf.bold_body("Effect size")
    pdf.body("R\u00b2 = 0.36. Advertising explains 36% of the variance in sales. Large effect.")
    pdf.bold_body("Conclusion")
    pdf.body("Advertising spend is a significant predictor of sales revenue (b\u2081 = 2.35, t = 3.67, p = 0.001). For each additional $1,000 spent on advertising, sales increase by approximately $2,350. R\u00b2 = 0.36 (large effect).")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding advertising predicts sales when it actually does not.")
    pdf.body("Type II: Failing to detect that advertising predicts sales when it actually does.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Not checking residual plots for violations of linearity and homoscedasticity.")
    pdf.numbered(2, "Extrapolating the regression line far beyond the range of observed X values.")
    pdf.numbered(3, "Interpreting a significant slope as proof of causation.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Correlation T-Test: Equivalent test (tests r = 0 vs \u03b2\u2081 = 0).")
    pdf.bullet("Regression F-Test: Tests overall model significance.")

    pdf.save("regression_slope_t_test")

# ════════════════════════════════════════════════════════════════
#  21. REGRESSION F-TEST
# ════════════════════════════════════════════════════════════════
def gen_reg_f():
    pdf = NotesPDF()
    title(pdf, "F-Test for Overall Regression Significance")
    pdf.section("Section 1: Introduction")
    pdf.body("The regression F-test tests whether the overall regression model is statistically significant - that is, whether at least one predictor variable has a non-zero effect on the response variable. For simple linear regression (one predictor), this test is equivalent to the t-test for the slope. For multiple regression, it tests all predictors jointly.")
    pdf.body("Scenario: A real estate analyst builds a model predicting house prices using square footage and number of bedrooms. The F-test determines whether the model as a whole explains a significant amount of variation in price.")

    pdf.section("Section 2: Hypotheses")
    pdf.body("H\u2080: \u03b2\u2081 = \u03b2\u2082 = ... = \u03b2_k = 0  (no predictor is useful)")
    pdf.body("H\u2081: At least one \u03b2_j \u2260 0  (at least one predictor is useful)")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Linear relationship between predictors and response.")
    pdf.numbered(2, "Independence of observations.")
    pdf.numbered(3, "Normality of residuals.")
    pdf.numbered(4, "Homoscedasticity (constant variance of residuals).")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("F = (SSR/k) / (SSE/(n-k-1)) = MSR / MSE")
    pdf.body("SSR = regression sum of squares, SSE = error sum of squares.")
    pdf.body("k = number of predictors, n = sample size.")
    pdf.formula("df\u2081 = k  (numerator),   df\u2082 = n - k - 1  (denominator)")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Reject H\u2080 if F > F_{\u03b1, k, n-k-1} or p-value < \u03b1. Always right-tailed.")

    pdf.section("Section 6: Confidence Interval")
    pdf.body("Not directly applicable to the F-test. CIs for individual coefficients use the t-distribution.")

    pdf.section("Section 7: Effect Size")
    pdf.formula("R\u00b2 = SSR / SST = 1 - SSE/SST")
    pdf.formula("Adjusted R\u00b2 = 1 - [(1-R\u00b2)(n-1)/(n-k-1)]")
    pdf.body("R\u00b2 = 0.01 small, 0.09 medium, 0.25 large.")
    pdf.body("Adjusted R\u00b2 penalises for the number of predictors and is preferred for multiple regression.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("House prices model: n=40, k=2 predictors (sqft, bedrooms). SSR=450000, SSE=300000, SST=750000. Test at \u03b1=0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03b2\u2081 = \u03b2\u2082 = 0     H\u2081: At least one \u03b2 \u2260 0")
    pdf.bold_body("Test statistic")
    pdf.formula("MSR = 450000/2 = 225000")
    pdf.formula("MSE = 300000/(40-2-1) = 300000/37 = 8108.1")
    pdf.formula("F = 225000/8108.1 = 27.75")
    pdf.body("df\u2081=2, df\u2082=37")
    pdf.bold_body("Critical value")
    pdf.body("F_{0.05, 2, 37} \u2248 3.252")
    pdf.bold_body("P-value")
    pdf.body("p < 0.0001")
    pdf.bold_body("Decision")
    pdf.body("F = 27.75 >> 3.252. Reject H\u2080.")
    pdf.bold_body("Effect size")
    pdf.formula("R\u00b2 = 450000/750000 = 0.600")
    pdf.formula("Adj R\u00b2 = 1 - [(1-0.60)(39)/37] = 1 - 0.4216 = 0.578")
    pdf.body("Very large effect. The model explains 60% of the variance in house prices.")
    pdf.bold_body("Conclusion")
    pdf.body("The regression model is highly significant (F = 27.75, df = 2 and 37, p < 0.0001). Square footage and bedrooms jointly explain 60% of the variance in house prices (R\u00b2 = 0.60, Adj R\u00b2 = 0.58).")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the model is significant when the predictors actually have no effect on price.")
    pdf.body("Type II: Failing to detect that the predictors have a real effect on price.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Confusing the overall F-test with individual t-tests. A significant F does not tell you WHICH predictors are significant.")
    pdf.numbered(2, "Using R\u00b2 alone without checking Adjusted R\u00b2 in multiple regression.")
    pdf.numbered(3, "Ignoring residual diagnostics (normality, homoscedasticity, linearity).")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Regression Slope T-Test: Tests individual predictors.")
    pdf.bullet("One-Way ANOVA: Related framework for comparing group means.")

    pdf.save("regression_f_test")

# ════════════════════════════════════════════════════════════════
#  22. CHI-SQUARE VARIANCE TEST
# ════════════════════════════════════════════════════════════════
def gen_chisq_var():
    pdf = NotesPDF()
    title(pdf, "Chi-Square Test for a Single Variance")
    pdf.section("Section 1: Introduction")
    pdf.body("The chi-square test for a single variance tests whether the population variance \u03c3\u00b2 equals a hypothesised value. This is important in quality control where consistency (low variance) is critical. It can also test the population standard deviation by squaring the hypothesised value.")
    pdf.body("Scenario: A manufacturer requires that the variance of bolt diameters not exceed 0.04 mm\u00b2. A sample of 20 bolts is measured to test this specification.")

    pdf.section("Section 2: Hypotheses")
    pdf.bold_body("Two-tailed:")
    pdf.body("H\u2080: \u03c3\u00b2 = \u03c3\u2080\u00b2     H\u2081: \u03c3\u00b2 \u2260 \u03c3\u2080\u00b2")
    pdf.bold_body("Right-tailed (variance exceeds spec):")
    pdf.body("H\u2080: \u03c3\u00b2 \u2264 \u03c3\u2080\u00b2     H\u2081: \u03c3\u00b2 > \u03c3\u2080\u00b2")
    pdf.bold_body("Left-tailed (variance is below spec):")
    pdf.body("H\u2080: \u03c3\u00b2 \u2265 \u03c3\u2080\u00b2     H\u2081: \u03c3\u00b2 < \u03c3\u2080\u00b2")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "The population is normally distributed. This test is VERY sensitive to non-normality.")
    pdf.numbered(2, "The sample is a simple random sample.")
    pdf.numbered(3, "Observations are independent.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("\u03c7\u00b2 = (n-1)s\u00b2 / \u03c3\u2080\u00b2")
    pdf.body("s\u00b2 = sample variance, \u03c3\u2080\u00b2 = hypothesised variance, n = sample size.")
    pdf.formula("df = n - 1")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Right-tailed: Reject H\u2080 if \u03c7\u00b2 > \u03c7\u00b2_{\u03b1, df}.")
    pdf.body("Left-tailed: Reject H\u2080 if \u03c7\u00b2 < \u03c7\u00b2_{1-\u03b1, df}.")
    pdf.body("Two-tailed: Reject if \u03c7\u00b2 > \u03c7\u00b2_{\u03b1/2, df} or \u03c7\u00b2 < \u03c7\u00b2_{1-\u03b1/2, df}.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI for \u03c3\u00b2: [(n-1)s\u00b2/\u03c7\u00b2_{\u03b1/2},  (n-1)s\u00b2/\u03c7\u00b2_{1-\u03b1/2}]")
    pdf.body("Take square roots for a CI for \u03c3.")

    pdf.section("Section 7: Effect Size")
    pdf.body("No standard effect size measure. The ratio s\u00b2/\u03c3\u2080\u00b2 provides a descriptive comparison.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("n=20 bolts, s\u00b2=0.058 mm\u00b2. Spec: \u03c3\u2080\u00b2=0.04 mm\u00b2. Test H\u2081: \u03c3\u00b2 > 0.04 at \u03b1=0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03c3\u00b2 \u2264 0.04     H\u2081: \u03c3\u00b2 > 0.04  (right-tailed)")
    pdf.bold_body("Test statistic")
    pdf.formula("\u03c7\u00b2 = (20-1)(0.058)/0.04 = 19 \u00d7 1.45 = 27.55")
    pdf.body("df = 19")
    pdf.bold_body("Critical value")
    pdf.body("\u03c7\u00b2_{0.05, 19} = 30.144")
    pdf.bold_body("P-value")
    pdf.body("P(\u03c7\u00b2 > 27.55 | df=19) \u2248 0.093")
    pdf.bold_body("Decision")
    pdf.body("27.55 < 30.144, p = 0.093 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Confidence interval")
    pdf.formula("CI = [19\u00d70.058/32.852, 19\u00d70.058/8.907] = [0.0336, 0.1237]")
    pdf.body("CI for \u03c3: (0.183, 0.352) mm")
    pdf.bold_body("Conclusion")
    pdf.body("At \u03b1=0.05, there is insufficient evidence that the variance exceeds 0.04 mm\u00b2 (\u03c7\u00b2=27.55, p=0.093). The 95% CI for \u03c3\u00b2 is (0.034, 0.124), which does include 0.04.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding bolt variance exceeds specs when it actually does not (unnecessarily halting production).")
    pdf.body("Type II: Failing to detect excessive variance when bolts are truly inconsistent.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using this test when the population is not normal. It is very sensitive to non-normality, unlike t-tests which are more robust.")
    pdf.numbered(2, "Confusing \u03c3 and \u03c3\u00b2. Make sure the hypothesised value matches what you are testing.")
    pdf.numbered(3, "Using the wrong tail. Right-tailed tests for 'variance too large'; left-tailed for 'variance too small'.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("F-Test for Two Variances: Compares variances from two populations.")

    pdf.save("chi_square_variance")

# ════════════════════════════════════════════════════════════════
#  23. F-TEST FOR TWO VARIANCES
# ════════════════════════════════════════════════════════════════
def gen_f_two_var():
    pdf = NotesPDF()
    title(pdf, "F-Test for Equality of Two Variances")
    pdf.section("Section 1: Introduction")
    pdf.body("The F-test for two variances tests whether two populations have equal variances. This is commonly used as a preliminary check before running a two-sample t-test that assumes equal variances. If variances are unequal, Welch's t-test should be used instead.")
    pdf.body("Scenario: A factory has two machines producing metal rods. The quality manager wants to test whether the variability in rod lengths is the same for both machines before comparing their means.")

    pdf.section("Section 2: Hypotheses")
    pdf.bold_body("Two-tailed:")
    pdf.body("H\u2080: \u03c3\u2081\u00b2 = \u03c3\u2082\u00b2     H\u2081: \u03c3\u2081\u00b2 \u2260 \u03c3\u2082\u00b2")
    pdf.bold_body("Right-tailed:")
    pdf.body("H\u2080: \u03c3\u2081\u00b2 \u2264 \u03c3\u2082\u00b2     H\u2081: \u03c3\u2081\u00b2 > \u03c3\u2082\u00b2")
    pdf.body("Convention: Place the larger sample variance in the numerator so F \u2265 1.")

    pdf.section("Section 3: Assumptions / Conditions")
    pdf.numbered(1, "Both populations are normally distributed. This test is VERY sensitive to non-normality.")
    pdf.numbered(2, "Samples are independent random samples.")
    pdf.numbered(3, "Observations are independent.")

    pdf.section("Section 4: Test Statistic Formula")
    pdf.formula("F = s\u2081\u00b2 / s\u2082\u00b2   (larger variance in numerator)")
    pdf.formula("df\u2081 = n\u2081 - 1  (numerator),  df\u2082 = n\u2082 - 1  (denominator)")

    pdf.section("Section 5: Decision Rule")
    pdf.body("Right-tailed: Reject H\u2080 if F > F_{\u03b1, df\u2081, df\u2082}.")
    pdf.body("Two-tailed: Reject H\u2080 if F > F_{\u03b1/2, df\u2081, df\u2082}.")

    pdf.section("Section 6: Confidence Interval")
    pdf.formula("CI for \u03c3\u2081\u00b2/\u03c3\u2082\u00b2: [(s\u2081\u00b2/s\u2082\u00b2)/F_{\u03b1/2,df\u2081,df\u2082}, (s\u2081\u00b2/s\u2082\u00b2) \u00d7 F_{\u03b1/2,df\u2082,df\u2081}]")
    pdf.body("If the CI includes 1, we cannot reject equal variances.")

    pdf.section("Section 7: Effect Size")
    pdf.body("The F ratio itself (s\u2081\u00b2/s\u2082\u00b2) serves as a descriptive measure. F = 1 means equal variances; F >> 1 means very different variances.")

    pdf.section("Section 8: Worked Example")
    pdf.bold_body("Problem")
    pdf.body("Machine A: n\u2081=16, s\u2081\u00b2=0.12. Machine B: n\u2082=21, s\u2082\u00b2=0.05. Test equality at \u03b1=0.05.")
    pdf.bold_body("Hypotheses")
    pdf.body("H\u2080: \u03c3\u2081\u00b2 = \u03c3\u2082\u00b2     H\u2081: \u03c3\u2081\u00b2 \u2260 \u03c3\u2082\u00b2  (two-tailed)")
    pdf.bold_body("Test statistic")
    pdf.formula("F = 0.12 / 0.05 = 2.400")
    pdf.body("df\u2081 = 15, df\u2082 = 20")
    pdf.bold_body("Critical value")
    pdf.body("F_{0.025, 15, 20} = 2.573")
    pdf.bold_body("P-value")
    pdf.body("p \u2248 0.068 (two-tailed)")
    pdf.bold_body("Decision")
    pdf.body("F = 2.400 < 2.573, p = 0.068 > 0.05. Fail to reject H\u2080.")
    pdf.bold_body("Confidence interval")
    pdf.body("CI for \u03c3\u2081\u00b2/\u03c3\u2082\u00b2 = (2.4/2.573, 2.4 \u00d7 2.762) = (0.933, 6.629)")
    pdf.body("The CI includes 1.")
    pdf.bold_body("Conclusion")
    pdf.body("At \u03b1=0.05, there is insufficient evidence that the variances differ (F=2.40, p=0.068). The equal-variance assumption is reasonable, and a pooled two-sample t-test may be used to compare the means.")

    pdf.section("Section 9: Type I and Type II Errors")
    pdf.body("Type I: Concluding the machines have different variability when they actually have the same.")
    pdf.body("Type II: Failing to detect different variability when the machines truly differ in consistency.")

    pdf.section("Section 10: Common Mistakes to Avoid")
    pdf.numbered(1, "Using this test when populations are not normal. Consider Levene's test as a more robust alternative.")
    pdf.numbered(2, "Placing the smaller variance in the numerator when the convention expects the larger one.")
    pdf.numbered(3, "Confusing this with the regression F-test, which tests model significance.")

    pdf.section("Section 11: Related Tests")
    pdf.bullet("Chi-Square Variance Test: Tests a single population variance.")
    pdf.bullet("Two-Sample T-Test (Equal Var): Requires this test first to check the equal-variance assumption.")

    pdf.save("f_test_two_variances")

if __name__ == "__main__":
    gen_corr_t()
    gen_reg_slope()
    gen_reg_f()
    gen_chisq_var()
    gen_f_two_var()
    print("\nAll 5 regression/variance PDFs generated.")
