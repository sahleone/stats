"""Generate _notes.pdf for the 3 foundational topics:
binomial_distribution, confidence_intervals, bootstrapping.
(normal_distribution already has its PDF.)
"""
import os
import glob
from fpdf import FPDF

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── DejaVu font paths (bundled with matplotlib) ──────────────
_FONT_DIR = glob.glob(
    "/Library/Frameworks/Python.framework/Versions/*/lib/python*/site-packages/matplotlib/mpl-data/fonts/ttf"
)[0]
DEJAVU = os.path.join(_FONT_DIR, "DejaVuSans.ttf")
DEJAVU_B = os.path.join(_FONT_DIR, "DejaVuSans-Bold.ttf")

# ── colours ────────────────────────────────────────────────────
DARK_BLUE = (47, 84, 150)
BLACK = (0, 0, 0)
GRAY_BG = (240, 240, 240)
F = "DejaVu"  # font family alias


class NotesPDF(FPDF):
    """Reusable PDF helper with consistent formatting."""

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.add_font(F, "", DEJAVU, uni=True)
        self.add_font(F, "B", DEJAVU_B, uni=True)

    def header(self):
        pass  # handled manually per-page

    def footer(self):
        self.set_y(-15)
        self.set_font(F, "", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    # ── helpers ──────────────────────────────────────────────
    def add_title(self, title, subtitle):
        self.set_font(F, "B", 18)
        self.set_text_color(*DARK_BLUE)
        self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT", align="C")
        self.set_font(F, "", 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, subtitle, new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(4)
        self.draw_hrule()

    def section(self, title):
        if self.get_y() > 245:
            self.add_page()
        self.ln(3)
        self.draw_hrule()
        self.ln(2)
        self.set_font(F, "B", 14)
        self.set_text_color(*DARK_BLUE)
        self.multi_cell(0, 7, title)
        self.ln(2)

    def body(self, text):
        self.set_font(F, "", 11)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bold_body(self, text):
        self.set_font(F, "B", 11)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def formula(self, text):
        """Centered formula with gray background."""
        self.set_font(F, "", 12)
        self.set_text_color(*BLACK)
        w = self.get_string_width(text) + 16
        x = (self.w - w) / 2
        self.set_fill_color(*GRAY_BG)
        self.set_xy(x, self.get_y())
        self.cell(w, 8, text, fill=True, align="C")
        self.ln(10)

    def bullet(self, text):
        self.set_font(F, "", 11)
        self.set_text_color(*BLACK)
        x = self.get_x()
        self.cell(6, 5.5, chr(8226))
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def numbered(self, num, text):
        self.set_font(F, "B", 11)
        self.set_text_color(*BLACK)
        self.cell(8, 5.5, f"{num}.")
        self.set_font(F, "", 11)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def draw_hrule(self):
        self.set_draw_color(180, 180, 180)
        self.line(self.l_margin, self.get_y(),
                  self.w - self.r_margin, self.get_y())
        self.ln(2)

    def check_page_break(self, h=40):
        if self.get_y() + h > self.h - 25:
            self.add_page()


# ═══════════════════════════════════════════════════════════════
#  BINOMIAL DISTRIBUTION
# ═══════════════════════════════════════════════════════════════
def gen_binomial():
    pdf = NotesPDF("P", "mm", "Letter")
    pdf.set_auto_page_break(auto=True, margin=25)
    pdf.add_page()
    pdf.set_left_margin(25.4)
    pdf.set_right_margin(25.4)
    pdf.set_top_margin(25.4)
    pdf.set_y(25.4)

    # S1 Title
    pdf.add_title("The Binomial Distribution",
                  "Undergraduate Statistics \u2014 Lecture Notes")

    # S1 Intro
    pdf.body(
        "The binomial distribution is one of the most important discrete "
        "probability distributions in statistics. It models the number of "
        "successes in a fixed number of independent trials, where each trial "
        "has exactly two possible outcomes (success or failure) and the "
        "probability of success remains constant from trial to trial."
    )
    pdf.body(
        "Real-world example: A quality control inspector examines 20 "
        "items from a production line where the historical defect rate is "
        "8%. The inspector wants to know the probability of finding "
        "various numbers of defective items in the sample. The number of "
        "defective items follows a binomial distribution with n = 20 and "
        "p = 0.08."
    )

    # S2 Key Definitions
    pdf.section("Section 2: Key Definitions & Terminology")
    pdf.bold_body("Binomial Experiment")
    pdf.body(
        "A statistical experiment that satisfies four conditions: "
        "(1) a fixed number of trials n, (2) each trial has exactly two "
        "outcomes (success or failure), (3) trials are independent, and "
        "(4) the probability of success p is constant across all trials."
    )
    pdf.bold_body("Key Notation")
    pdf.bullet("n = number of trials (fixed in advance)")
    pdf.bullet("p = probability of success on any single trial")
    pdf.bullet("q = 1 - p = probability of failure on any single trial")
    pdf.bullet("k = number of successes (the value we are interested in)")
    pdf.bullet(
        "X = random variable representing the number of successes; "
        "X ~ Bin(n, p)"
    )
    pdf.bold_body("Binomial Coefficient")
    pdf.formula("C(n, k) = n! / [k! (n - k)!]")
    pdf.body(
        "Read as 'n choose k'. This counts the number of ways to "
        "arrange k successes among n trials."
    )
    pdf.bold_body("Probability Mass Function (PMF)")
    pdf.formula("P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)")
    pdf.body(
        "This gives the probability of obtaining exactly k successes "
        "in n independent trials."
    )
    pdf.bold_body("Mean, Variance, and Standard Deviation")
    pdf.formula("Mean:  \u03bc = n * p")
    pdf.formula("Variance:  \u03c3\u00b2 = n * p * (1 - p)")
    pdf.formula("Standard Deviation:  \u03c3 = \u221a[n * p * (1 - p)]")

    # S3 Core Theory
    pdf.section("Section 3: Core Theory & Properties")
    pdf.bold_body("The Four Conditions (BINS)")
    pdf.numbered(1,
        "Binary outcomes: each trial results in success or failure.")
    pdf.numbered(2,
        "Independent trials: the outcome of one trial does not affect "
        "any other trial.")
    pdf.numbered(3,
        "Number of trials is fixed: n is determined before the "
        "experiment begins.")
    pdf.numbered(4,
        "Same probability: p is constant across all trials.")
    pdf.body(
        "If any of these conditions is violated, the binomial model "
        "is not appropriate. For example, if sampling is done without "
        "replacement from a small population, the trials are not "
        "independent, and the hypergeometric distribution should be "
        "used instead."
    )
    pdf.check_page_break(50)
    pdf.bold_body("Cumulative Probabilities")
    pdf.body(
        "The cumulative distribution function (CDF) gives the "
        "probability that X is at most k:"
    )
    pdf.formula(
        "P(X \u2264 k) = \u2211 [i=0 to k] C(n,i) * p^i * (1-p)^(n-i)"
    )
    pdf.body(
        "Useful identities: P(X \u2265 k) = 1 - P(X \u2264 k-1) and "
        "P(X > k) = 1 - P(X \u2264 k)."
    )
    pdf.bold_body("Shape of the Distribution")
    pdf.body(
        "When p = 0.5 the distribution is perfectly symmetric. "
        "When p < 0.5 it is right-skewed, and when p > 0.5 it is "
        "left-skewed. As n increases, the distribution becomes more "
        "bell-shaped regardless of p, which motivates the normal "
        "approximation."
    )
    pdf.bold_body("Normal Approximation to the Binomial")
    pdf.body(
        "When n is large enough, the binomial distribution can be "
        "approximated by a normal distribution with mean \u03bc = np and "
        "standard deviation \u03c3 = \u221a(npq). The rule of thumb is:"
    )
    pdf.formula("np \u2265 5   AND   n(1 - p) \u2265 5")
    pdf.body(
        "When using the normal approximation, apply the continuity "
        "correction: to approximate P(X \u2265 k), compute P(Z \u2265 "
        "(k - 0.5 - np) / \u03c3). To approximate P(X \u2264 k), compute "
        "P(Z \u2264 (k + 0.5 - np) / \u03c3)."
    )

    # S4 Formulas
    pdf.section("Section 4: Formulas & Equations")
    pdf.bold_body("Probability Mass Function (PMF)")
    pdf.formula("P(X = k) = C(n,k) * p^k * (1-p)^(n-k)")
    pdf.body(
        "where k = 0, 1, 2, ..., n; C(n,k) = n!/(k!(n-k)!); "
        "p = probability of success; (1-p) = probability of failure."
    )
    pdf.bold_body("Cumulative Distribution Function (CDF)")
    pdf.formula(
        "P(X \u2264 k) = \u2211 [i=0 to k] C(n,i) * p^i * (1-p)^(n-i)"
    )
    pdf.bold_body("Moments")
    pdf.formula("Mean: \u03bc = np")
    pdf.formula("Variance: \u03c3\u00b2 = np(1 - p)")
    pdf.formula("Std Dev: \u03c3 = \u221a[np(1 - p)]")
    pdf.bold_body("Normal Approximation (with continuity correction)")
    pdf.formula("Z = (X \u00b1 0.5 - np) / \u221a[np(1 - p)]")
    pdf.body(
        "Use +0.5 when computing P(X \u2264 k) and -0.5 when computing "
        "P(X \u2265 k)."
    )

    # S5 Worked Examples
    pdf.section("Section 5: Worked Examples")

    # Example 1
    pdf.check_page_break(70)
    pdf.bold_body("Example 1: Finding P(X = k) Using the PMF")
    pdf.body(
        "Problem: A quality control inspector examines 10 items from a "
        "production line where the defect rate is 8%. What is the "
        "probability that exactly 2 items are defective?"
    )
    pdf.bold_body("Step 1: Identify the parameters")
    pdf.body("n = 10 (number of items inspected)")
    pdf.body("p = 0.08 (probability of a defect)")
    pdf.body("k = 2 (number of defective items)")
    pdf.bold_body("Step 2: Verify binomial conditions")
    pdf.body(
        "Binary (defective or not), independent (each item examined "
        "separately), fixed n = 10, constant p = 0.08. All conditions met."
    )
    pdf.bold_body("Step 3: Compute the binomial coefficient")
    pdf.formula("C(10, 2) = 10! / (2! * 8!) = (10 * 9) / (2 * 1) = 45")
    pdf.bold_body("Step 4: Apply the PMF formula")
    pdf.formula("P(X=2) = 45 * (0.08)^2 * (0.92)^8")
    pdf.body("(0.08)^2 = 0.0064")
    pdf.body("(0.92)^8 = 0.5132 (rounded to 4 decimal places)")
    pdf.formula("P(X=2) = 45 * 0.0064 * 0.5132 = 0.1478")
    pdf.bold_body("Step 5: Interpret")
    pdf.body(
        "There is approximately a 14.78% chance that exactly 2 of the "
        "10 inspected items are defective."
    )

    # Example 2
    pdf.check_page_break(70)
    pdf.bold_body("Example 2: Finding P(X \u2265 k) Using Cumulative "
                  "Probabilities")
    pdf.body(
        "Problem: A basketball player has a free-throw success rate of "
        "75%. In 8 free throws, what is the probability of making at "
        "least 7?"
    )
    pdf.bold_body("Step 1: Identify parameters")
    pdf.body("n = 8, p = 0.75, find P(X \u2265 7) = P(X=7) + P(X=8)")
    pdf.bold_body("Step 2: Compute P(X = 7)")
    pdf.formula("C(8,7) = 8")
    pdf.formula(
        "P(X=7) = 8 * (0.75)^7 * (0.25)^1 = 8 * 0.1335 * 0.25 = 0.2670"
    )
    pdf.bold_body("Step 3: Compute P(X = 8)")
    pdf.formula("C(8,8) = 1")
    pdf.formula("P(X=8) = 1 * (0.75)^8 * (0.25)^0 = 0.1001")
    pdf.bold_body("Step 4: Sum")
    pdf.formula("P(X \u2265 7) = 0.2670 + 0.1001 = 0.3671")
    pdf.bold_body("Step 5: Interpret")
    pdf.body(
        "There is approximately a 36.71% chance that the player makes "
        "at least 7 out of 8 free throws."
    )

    # Example 3
    pdf.check_page_break(80)
    pdf.bold_body(
        "Example 3: Normal Approximation with Continuity Correction"
    )
    pdf.body(
        "Problem: A factory produces lightbulbs with a 5% defect rate. "
        "In a shipment of 200 lightbulbs, what is the probability that "
        "more than 15 are defective?"
    )
    pdf.bold_body("Step 1: Identify parameters")
    pdf.body("n = 200, p = 0.05, find P(X > 15)")
    pdf.bold_body("Step 2: Check normal approximation conditions")
    pdf.body("np = 200 * 0.05 = 10 \u2265 5  \u2713")
    pdf.body("n(1-p) = 200 * 0.95 = 190 \u2265 5  \u2713")
    pdf.bold_body("Step 3: Compute mean and standard deviation")
    pdf.formula("\u03bc = np = 200 * 0.05 = 10")
    pdf.formula(
        "\u03c3 = \u221a(np(1-p)) = \u221a(200 * 0.05 * 0.95) = "
        "\u221a9.5 = 3.082"
    )
    pdf.bold_body("Step 4: Apply continuity correction")
    pdf.body(
        "P(X > 15) = P(X \u2265 16) \u2248 P(Z \u2265 (15.5 - 10)/3.082)"
    )
    pdf.formula("Z = (15.5 - 10) / 3.082 = 5.5 / 3.082 = 1.784")
    pdf.bold_body("Step 5: Find the probability")
    pdf.body("P(Z > 1.784) = 1 - P(Z \u2264 1.784) = 1 - 0.9628 = 0.0372")
    pdf.bold_body("Step 6: Interpret")
    pdf.body(
        "There is approximately a 3.72% chance that more than 15 of the "
        "200 lightbulbs are defective."
    )

    # S6 Visualizations
    pdf.section("Section 6: Visualizations & Interpretation")
    pdf.bold_body("Probability Histogram")
    pdf.body(
        "A binomial probability histogram has bars at each integer "
        "value k = 0, 1, ..., n. The height of each bar equals P(X=k). "
        "For small p, the histogram is right-skewed with the peak near "
        "np. For p = 0.5, it is perfectly symmetric."
    )
    pdf.bold_body("Effect of n")
    pdf.body(
        "As n increases, the histogram becomes more bell-shaped and "
        "spread out. The normal approximation becomes more accurate. "
        "Compare Bin(5, 0.3) (clearly skewed) with Bin(50, 0.3) "
        "(approximately normal)."
    )
    pdf.bold_body("Effect of p")
    pdf.body(
        "For fixed n, changing p shifts the center of the distribution. "
        "The distribution is symmetric only when p = 0.5. As p moves "
        "away from 0.5 in either direction, the distribution becomes "
        "more skewed."
    )
    pdf.bold_body("Normal Overlay")
    pdf.body(
        "When the normal approximation conditions are met, a normal "
        "curve with mean np and standard deviation \u221a(npq) can be "
        "overlaid on the histogram. The bars and the curve should "
        "match closely."
    )

    # S7 Misconceptions
    pdf.section("Section 7: Common Misconceptions & Mistakes")
    pdf.numbered(1,
        "Confusing binomial with geometric distribution. The geometric "
        "distribution counts the number of trials UNTIL the first "
        "success, while the binomial counts the number of successes in "
        "a FIXED number of trials.")
    pdf.numbered(2,
        "Forgetting the independence requirement. If items are sampled "
        "without replacement from a small population, trials are not "
        "independent. Use the hypergeometric distribution instead (or "
        "the binomial is acceptable if the sample is less than 10% of "
        "the population).")
    pdf.numbered(3,
        "Using the normal approximation when np < 5 or n(1-p) < 5. "
        "The approximation is poor when either condition fails. Always "
        "check both conditions before using the normal approximation.")
    pdf.numbered(4,
        "Forgetting the continuity correction. When approximating a "
        "discrete distribution with a continuous one, the continuity "
        "correction (+/- 0.5) improves accuracy substantially.")
    pdf.numbered(5,
        "Confusing P(X \u2265 k) with P(X > k). These differ by "
        "P(X = k). For discrete distributions this distinction matters: "
        "P(X \u2265 5) = P(X = 5) + P(X = 6) + ..., while "
        "P(X > 5) = P(X = 6) + P(X = 7) + ...")

    # S8 Connections
    pdf.section("Section 8: Connections to Other Topics")
    pdf.bold_body("See Also")
    pdf.bullet(
        "Normal Distribution: When n is large and np \u2265 5 and "
        "n(1-p) \u2265 5, the binomial distribution can be approximated "
        "by the normal distribution."
    )
    pdf.bullet(
        "Confidence Intervals for Proportions: The sample proportion "
        "p-hat = X/n is used to build confidence intervals; X follows "
        "a binomial distribution."
    )
    pdf.bullet(
        "One-Sample Proportion Z-Test: Tests whether a population "
        "proportion equals a hypothesized value, based on the "
        "binomial model."
    )
    pdf.bullet(
        "Chi-Square Goodness-of-Fit: Tests whether observed category "
        "counts match expected counts, extending the binomial idea to "
        "more than two categories."
    )

    out = os.path.join(BASE, "binomial_distribution",
                       "binomial_distribution_notes.pdf")
    pdf.output(out)
    print(f"Created {out}  ({os.path.getsize(out)} bytes)")


# ═══════════════════════════════════════════════════════════════
#  CONFIDENCE INTERVALS
# ═══════════════════════════════════════════════════════════════
def gen_confidence_intervals():
    pdf = NotesPDF("P", "mm", "Letter")
    pdf.set_auto_page_break(auto=True, margin=25)
    pdf.add_page()
    pdf.set_left_margin(25.4)
    pdf.set_right_margin(25.4)
    pdf.set_top_margin(25.4)
    pdf.set_y(25.4)

    pdf.add_title("Confidence Intervals",
                  "Undergraduate Statistics \u2014 Lecture Notes")

    # S1 Intro
    pdf.body(
        "A confidence interval (CI) is a range of values used to "
        "estimate an unknown population parameter, such as a mean or "
        "proportion. Rather than giving a single best guess (a point "
        "estimate), a confidence interval provides an interval of "
        "plausible values along with a measure of how confident we are "
        "that the interval captures the true parameter."
    )
    pdf.body(
        "Real-world example: A polling company surveys 1,000 registered "
        "voters and finds that 54% support a new policy. They report "
        "the result as '54% \u00b1 3.1 percentage points (95% confidence).' "
        "The interval (50.9%, 57.1%) is the confidence interval. It "
        "tells us that, based on this sample, we are 95% confident the "
        "true level of voter support is somewhere in that range."
    )

    # S2 Key Definitions
    pdf.section("Section 2: Key Definitions & Terminology")
    pdf.bold_body("Point Estimate")
    pdf.body(
        "A single value computed from sample data that serves as our "
        "best guess for the population parameter. Examples: the sample "
        "mean x-bar estimates the population mean \u03bc; the sample "
        "proportion p-hat estimates the population proportion p."
    )
    pdf.bold_body("Confidence Interval")
    pdf.body(
        "An interval [lower bound, upper bound] computed from sample "
        "data that is likely to contain the true population parameter. "
        "Written as: point estimate \u00b1 margin of error."
    )
    pdf.bold_body("Confidence Level (1 - \u03b1)")
    pdf.body(
        "The probability that the interval-construction method "
        "produces an interval containing the true parameter. A 95% "
        "confidence level means that if we repeated the sampling "
        "process many times, about 95% of the resulting intervals "
        "would contain the true parameter."
    )
    pdf.bold_body("Margin of Error (E)")
    pdf.body(
        "The half-width of the confidence interval. "
        "E = critical value \u00d7 standard error."
    )
    pdf.bold_body("Critical Value")
    pdf.body(
        "The value from the standard normal (z*) or t-distribution "
        "(t*) that corresponds to the desired confidence level. "
        "For 95% confidence: z* = 1.960; for 99%: z* = 2.576."
    )
    pdf.bold_body("Standard Error (SE)")
    pdf.body(
        "The estimated standard deviation of the sampling "
        "distribution of the statistic. For a sample mean: "
        "SE = s / \u221an. For a sample proportion: "
        "SE = \u221a[p-hat(1 - p-hat)/n]."
    )

    # S3 Core Theory
    pdf.section("Section 3: Core Theory & Properties")
    pdf.bold_body("The General CI Formula")
    pdf.formula("CI = point estimate \u00b1 (critical value \u00d7 SE)")
    pdf.body(
        "Every confidence interval follows this structure. The "
        "specific formula depends on what parameter we are estimating "
        "and what information we have about the population."
    )
    pdf.bold_body("What '95% Confidence' Actually Means")
    pdf.body(
        "Imagine repeating the study 100 times, each time drawing a "
        "new random sample and computing a new CI. About 95 of those "
        "100 intervals would contain the true population parameter. "
        "The confidence level describes the reliability of the METHOD, "
        "not the probability that any single interval is correct."
    )
    pdf.bold_body("Confidence Level vs. Width")
    pdf.body(
        "Higher confidence level \u2192 larger critical value \u2192 wider "
        "interval. A 99% CI is wider than a 95% CI. You gain "
        "confidence at the cost of precision."
    )
    pdf.bold_body("Sample Size vs. Width")
    pdf.body(
        "Larger sample size \u2192 smaller standard error \u2192 narrower "
        "interval. Doubling the sample size reduces the margin of "
        "error by a factor of \u221a2 (about 29% reduction)."
    )

    # S4 Formulas
    pdf.section("Section 4: Formulas & Equations")
    pdf.bold_body("CI for a Mean (\u03c3 Known) \u2014 Z-Interval")
    pdf.formula("x-bar \u00b1 z*(\u03b1/2) \u00b7 \u03c3 / \u221an")
    pdf.body(
        "x-bar = sample mean, \u03c3 = known population standard "
        "deviation, n = sample size, z*(\u03b1/2) = critical value from "
        "the standard normal distribution."
    )
    pdf.bold_body("CI for a Mean (\u03c3 Unknown) \u2014 t-Interval")
    pdf.formula("x-bar \u00b1 t*(\u03b1/2, n-1) \u00b7 s / \u221an")
    pdf.body(
        "s = sample standard deviation, df = n - 1. Use the "
        "t-distribution because we are estimating \u03c3 with s."
    )
    pdf.bold_body("CI for a Proportion")
    pdf.formula(
        "p-hat \u00b1 z*(\u03b1/2) \u00b7 \u221a[p-hat(1 - p-hat) / n]"
    )
    pdf.body(
        "p-hat = sample proportion = x/n, where x is the number of "
        "successes. Conditions: np-hat \u2265 10 and n(1 - p-hat) \u2265 10."
    )
    pdf.bold_body("Sample Size for a Desired Margin of Error (Mean)")
    pdf.formula("n = [z*(\u03b1/2) \u00b7 \u03c3 / E]\u00b2")
    pdf.body("Round up to the next whole number.")
    pdf.bold_body("Sample Size for a Desired Margin of Error (Proportion)")
    pdf.formula(
        "n = [z*(\u03b1/2)]\u00b2 \u00b7 p-hat(1 - p-hat) / E\u00b2"
    )
    pdf.body(
        "If no prior estimate of p is available, use p-hat = 0.5 "
        "(maximises the required sample size, giving a conservative "
        "estimate)."
    )

    # S5 Worked Examples
    pdf.section("Section 5: Worked Examples")

    # Ex 1
    pdf.check_page_break(80)
    pdf.bold_body("Example 1: CI for a Mean (\u03c3 Known) \u2014 Z-Interval")
    pdf.body(
        "Problem: A machine fills cereal boxes. The fill weights are "
        "normally distributed with a known population standard "
        "deviation of \u03c3 = 3.2 grams. A random sample of 36 boxes has "
        "a mean weight of 365.4 grams. Construct a 95% confidence "
        "interval for the true mean fill weight."
    )
    pdf.bold_body("Step 1: Identify known values")
    pdf.body(
        "x-bar = 365.4,  \u03c3 = 3.2,  n = 36,  "
        "confidence level = 95%  \u2192  \u03b1 = 0.05"
    )
    pdf.bold_body("Step 2: Find the critical value")
    pdf.body("For 95% confidence, z*(\u03b1/2) = z*(0.025) = 1.960")
    pdf.bold_body("Step 3: Compute the standard error")
    pdf.formula("SE = \u03c3 / \u221an = 3.2 / \u221a36 = 3.2 / 6 = 0.5333")
    pdf.bold_body("Step 4: Compute the margin of error")
    pdf.formula("E = 1.960 \u00d7 0.5333 = 1.0453")
    pdf.bold_body("Step 5: Construct the interval")
    pdf.formula(
        "CI = (365.4 - 1.045,  365.4 + 1.045) = (364.355,  366.445)"
    )
    pdf.bold_body("Step 6: Interpret")
    pdf.body(
        "We are 95% confident that the true mean fill weight of cereal "
        "boxes is between 364.36 and 366.45 grams."
    )

    # Ex 2
    pdf.check_page_break(80)
    pdf.bold_body("Example 2: CI for a Mean (\u03c3 Unknown) \u2014 t-Interval")
    pdf.body(
        "Problem: A researcher measures the reaction times (in ms) of "
        "20 participants. The sample mean is 245 ms and the sample "
        "standard deviation is 32 ms. Construct a 99% confidence "
        "interval for the true mean reaction time."
    )
    pdf.bold_body("Step 1: Identify known values")
    pdf.body(
        "x-bar = 245,  s = 32,  n = 20,  df = 19,  "
        "confidence level = 99%  \u2192  \u03b1 = 0.01"
    )
    pdf.bold_body("Step 2: Find the critical value")
    pdf.body(
        "For 99% confidence with df = 19: t*(0.005, 19) = 2.861 "
        "(from the t-table)"
    )
    pdf.bold_body("Step 3: Compute the standard error")
    pdf.formula("SE = s / \u221an = 32 / \u221a20 = 32 / 4.472 = 7.155")
    pdf.bold_body("Step 4: Compute the margin of error")
    pdf.formula("E = 2.861 \u00d7 7.155 = 20.47")
    pdf.bold_body("Step 5: Construct the interval")
    pdf.formula(
        "CI = (245 - 20.47,  245 + 20.47) = (224.53,  265.47)"
    )
    pdf.bold_body("Step 6: Interpret")
    pdf.body(
        "We are 99% confident that the true mean reaction time of the "
        "population is between 224.53 ms and 265.47 ms."
    )

    # Ex 3
    pdf.check_page_break(80)
    pdf.bold_body("Example 3: CI for a Proportion")
    pdf.body(
        "Problem: In a survey of 500 registered voters, 280 said they "
        "support a new policy. Construct a 90% confidence interval for "
        "the true proportion of voters who support the policy."
    )
    pdf.bold_body("Step 1: Identify known values")
    pdf.body(
        "x = 280,  n = 500,  p-hat = 280/500 = 0.560,  "
        "confidence level = 90%  \u2192  \u03b1 = 0.10"
    )
    pdf.bold_body("Step 2: Check conditions")
    pdf.body(
        "np-hat = 500(0.56) = 280 \u2265 10  \u2713     "
        "n(1-p-hat) = 500(0.44) = 220 \u2265 10  \u2713"
    )
    pdf.bold_body("Step 3: Find the critical value")
    pdf.body("For 90% confidence, z*(0.05) = 1.645")
    pdf.bold_body("Step 4: Compute the standard error")
    pdf.formula(
        "SE = \u221a[0.56 \u00d7 0.44 / 500] = \u221a[0.0004928] = 0.02220"
    )
    pdf.bold_body("Step 5: Compute the margin of error")
    pdf.formula("E = 1.645 \u00d7 0.02220 = 0.03652")
    pdf.bold_body("Step 6: Construct the interval")
    pdf.formula(
        "CI = (0.560 - 0.037,  0.560 + 0.037) = (0.5235,  0.5965)"
    )
    pdf.bold_body("Step 7: Interpret")
    pdf.body(
        "We are 90% confident that between 52.35% and 59.65% of all "
        "registered voters support the new policy."
    )

    # S6 Visualizations
    pdf.section("Section 6: Visualizations & Interpretation")
    pdf.bold_body("Repeated Sampling Diagram")
    pdf.body(
        "Imagine drawing 100 random samples from the population, each "
        "producing its own 95% CI. If you plotted all 100 intervals as "
        "horizontal lines, with a vertical line marking the true "
        "parameter value \u03bc, about 95 of the intervals would cross "
        "the vertical line (capturing \u03bc) and about 5 would miss it "
        "entirely."
    )
    pdf.bold_body("Annotated Confidence Interval")
    pdf.body(
        "A single CI can be drawn as a number line with three key "
        "elements marked: the point estimate (center), the lower "
        "bound (left endpoint), and the upper bound (right endpoint). "
        "The distance from the center to either endpoint is the margin "
        "of error E."
    )
    pdf.bold_body("Effect of Sample Size")
    pdf.body(
        "Visualise three CIs based on n = 25, n = 100, and n = 400, "
        "all at 95% confidence. The interval narrows noticeably as n "
        "increases: the margin of error is proportional to 1/\u221an."
    )

    # S7 Misconceptions
    pdf.section("Section 7: Common Misconceptions & Mistakes")
    pdf.numbered(1,
        "'There is a 95% probability that \u03bc is in this interval.' "
        "WRONG. The true parameter is fixed \u2014 it either is in the "
        "interval or it isn't. The 95% refers to the long-run success "
        "rate of the method, not the probability for any single "
        "interval.")
    pdf.numbered(2,
        "Confusing confidence level with the proportion of data values "
        "in the interval. A 95% CI for the mean does NOT mean that 95% "
        "of individual observations fall in the interval.")
    pdf.numbered(3,
        "Using z* when \u03c3 is unknown. When the population standard "
        "deviation is unknown and estimated by s, use the t-distribution, "
        "not the standard normal.")
    pdf.numbered(4,
        "Forgetting to check conditions. The formulas assume random "
        "sampling, approximate normality (or large n), and, for "
        "proportions, sufficiently large np-hat and n(1-p-hat).")
    pdf.numbered(5,
        "Thinking a wider interval is always better. A wider interval "
        "gives more confidence but less precision. The goal is to "
        "balance confidence and precision, often by increasing "
        "sample size.")
    pdf.numbered(6,
        "Interpreting the CI as the range of likely individual values. "
        "A CI estimates the parameter (e.g., the population mean), not "
        "individual data points. A prediction interval serves that "
        "different purpose.")

    # S8 Connections
    pdf.section("Section 8: Connections to Other Topics")
    pdf.bold_body("See Also")
    pdf.bullet(
        "Normal Distribution: Z-intervals rely on the standard normal "
        "distribution; t-intervals rely on the t-distribution (which "
        "approaches the normal as df increases)."
    )
    pdf.bullet(
        "One-Sample Z-Test / T-Test: A two-sided hypothesis test at "
        "significance level \u03b1 and a (1-\u03b1) confidence interval give "
        "consistent conclusions \u2014 reject H\u2080 if and only if the "
        "hypothesised value falls outside the CI."
    )
    pdf.bullet(
        "Bootstrapping: A non-parametric method for constructing "
        "confidence intervals when parametric assumptions are "
        "questionable."
    )
    pdf.bullet(
        "Sample Size Determination: The margin-of-error formula can "
        "be rearranged to find the minimum sample size needed for a "
        "desired level of precision."
    )

    out = os.path.join(BASE, "confidence_intervals",
                       "confidence_intervals_notes.pdf")
    pdf.output(out)
    print(f"Created {out}  ({os.path.getsize(out)} bytes)")


# ═══════════════════════════════════════════════════════════════
#  BOOTSTRAPPING
# ═══════════════════════════════════════════════════════════════
def gen_bootstrapping():
    pdf = NotesPDF("P", "mm", "Letter")
    pdf.set_auto_page_break(auto=True, margin=25)
    pdf.add_page()
    pdf.set_left_margin(25.4)
    pdf.set_right_margin(25.4)
    pdf.set_top_margin(25.4)
    pdf.set_y(25.4)

    pdf.add_title("Bootstrapping",
                  "Undergraduate Statistics \u2014 Lecture Notes")

    # S1 Intro
    pdf.body(
        "Bootstrapping is a powerful resampling technique used to "
        "estimate the sampling distribution of a statistic without "
        "relying on assumptions about the shape of the population "
        "distribution. Instead of using theoretical formulas, "
        "bootstrapping repeatedly resamples from the observed data "
        "(with replacement) to build an empirical approximation of "
        "the sampling distribution."
    )
    pdf.body(
        "Real-world example: A small medical study collects recovery "
        "times for 15 patients after a new treatment. The data are "
        "clearly skewed, so a t-interval may not be appropriate. "
        "Bootstrapping allows the researcher to build a confidence "
        "interval for the median recovery time without assuming "
        "normality."
    )

    # S2 Key Definitions
    pdf.section("Section 2: Key Definitions & Terminology")
    pdf.bold_body("Bootstrap Sample")
    pdf.body(
        "A sample of size n drawn WITH REPLACEMENT from the original "
        "sample of size n. Some observations will appear more than "
        "once and some will not appear at all."
    )
    pdf.bold_body("Bootstrap Statistic")
    pdf.body(
        "The statistic of interest (e.g., mean, median, standard "
        "deviation) computed from a single bootstrap sample."
    )
    pdf.bold_body("Bootstrap Distribution")
    pdf.body(
        "The collection of bootstrap statistics obtained from many "
        "(typically B = 1,000 to 10,000) bootstrap samples. This "
        "distribution approximates the sampling distribution of the "
        "statistic."
    )
    pdf.bold_body("Resampling with Replacement")
    pdf.body(
        "Each draw is independent; after selecting an observation, it "
        "is 'put back' so it can be selected again. This is what makes "
        "each bootstrap sample different from the original."
    )
    pdf.bold_body("B (number of bootstrap resamples)")
    pdf.body(
        "The number of times we resample. Larger B gives a smoother "
        "bootstrap distribution. B = 10,000 is common for confidence "
        "intervals."
    )

    # S3 Core Theory
    pdf.section("Section 3: Core Theory & Properties")
    pdf.bold_body("The Bootstrap Principle")
    pdf.body(
        "The key idea: the original sample is our best available "
        "representation of the population. By resampling from it, we "
        "mimic the process of drawing new samples from the population. "
        "The variability among bootstrap statistics approximates the "
        "variability of the statistic across repeated real samples."
    )
    pdf.bold_body("Why It Works")
    pdf.body(
        "The empirical distribution of the sample converges to the "
        "population distribution as n grows (by the Glivenko-Cantelli "
        "theorem). Resampling from the empirical distribution thus "
        "approximates sampling from the true population."
    )
    pdf.bold_body("Bootstrap Distribution vs Sampling Distribution")
    pdf.body(
        "The sampling distribution describes the variability of a "
        "statistic across all possible samples from the population. "
        "The bootstrap distribution approximates this, centred at "
        "the observed statistic rather than the true parameter. The "
        "SPREAD (standard error) of the bootstrap distribution is "
        "the useful part, not the centre."
    )
    pdf.bold_body("Percentile Method for CIs")
    pdf.body(
        "The simplest bootstrap CI: sort all B bootstrap statistics "
        "and take the \u03b1/2 and (1 - \u03b1/2) percentiles as the "
        "lower and upper bounds. For a 95% CI, use the 2.5th and "
        "97.5th percentiles."
    )
    pdf.bold_body("When Bootstrapping is Preferred")
    pdf.body(
        "Use bootstrapping when: (1) the population distribution is "
        "unknown or non-normal, (2) the sample size is small, "
        "(3) there is no standard formula for the statistic of "
        "interest (e.g., median, trimmed mean, ratio of statistics), "
        "or (4) you want to avoid relying on distributional "
        "assumptions."
    )

    # S4 Formulas
    pdf.section("Section 4: Formulas & Equations")
    pdf.bold_body("Bootstrap Algorithm (Pseudocode)")
    pdf.body(
        "1. Start with original sample: x1, x2, ..., xn\n"
        "2. For b = 1, 2, ..., B:\n"
        "   a. Draw a sample of size n WITH REPLACEMENT from the "
        "original data\n"
        "   b. Compute the statistic of interest: theta*_b\n"
        "3. The collection {theta*_1, theta*_2, ..., theta*_B} is "
        "the bootstrap distribution"
    )
    pdf.bold_body("Bootstrap Standard Error")
    pdf.formula(
        "SE_boot = std. dev. of {theta*_1, ..., theta*_B}"
    )
    pdf.bold_body("Percentile CI (confidence level 1 - \u03b1)")
    pdf.formula(
        "CI = [theta*_(\u03b1/2),  theta*_(1 - \u03b1/2)]"
    )
    pdf.body(
        "where theta*_(p) denotes the p-th percentile of the "
        "bootstrap distribution. For a 95% CI, use the 2.5th and "
        "97.5th percentiles."
    )
    pdf.bold_body("BCa Method (brief mention)")
    pdf.body(
        "The bias-corrected and accelerated (BCa) bootstrap adjusts "
        "for bias and skewness in the bootstrap distribution, "
        "producing more accurate CIs than the simple percentile "
        "method. It is preferred when the bootstrap distribution is "
        "noticeably skewed."
    )

    # S5 Worked Examples
    pdf.section("Section 5: Worked Examples")

    # Ex 1
    pdf.check_page_break(90)
    pdf.bold_body("Example 1: Small Bootstrap by Hand")
    pdf.body(
        "Problem: A researcher records the commute times (in minutes) "
        "of 6 employees: {12, 18, 22, 15, 30, 25}. Use 5 bootstrap "
        "resamples to estimate the standard error and build an "
        "approximate bootstrap CI for the population mean."
    )
    pdf.bold_body("Step 1: Original sample statistics")
    pdf.body(
        "Original sample: {12, 18, 22, 15, 30, 25}\n"
        "n = 6,  x-bar = (12+18+22+15+30+25)/6 = 122/6 = 20.33"
    )
    pdf.bold_body("Step 2: Draw 5 bootstrap samples (with replacement)")
    pdf.body(
        "Resample 1: {18, 25, 12, 25, 22, 18}  mean = 20.00\n"
        "Resample 2: {30, 15, 22, 22, 12, 18}  mean = 19.83\n"
        "Resample 3: {25, 30, 30, 15, 18, 12}  mean = 21.67\n"
        "Resample 4: {12, 12, 18, 22, 25, 15}  mean = 17.33\n"
        "Resample 5: {22, 25, 30, 18, 25, 22}  mean = 23.67"
    )
    pdf.bold_body("Step 3: Bootstrap distribution of means")
    pdf.body("{20.00, 19.83, 21.67, 17.33, 23.67}")
    pdf.bold_body("Step 4: Bootstrap standard error")
    pdf.body(
        "Mean of bootstrap means = (20.00+19.83+21.67+17.33+23.67)/5 "
        "= 20.50\n"
        "SE_boot = std dev of {20.00,19.83,21.67,17.33,23.67} = 2.31"
    )
    pdf.bold_body("Step 5: Interpret")
    pdf.body(
        "With only 5 resamples this is a rough illustration. In "
        "practice, use B = 10,000 or more. The bootstrap standard "
        "error of approximately 2.31 estimates the variability of the "
        "sample mean across repeated samples."
    )

    # Ex 2
    pdf.check_page_break(70)
    pdf.bold_body("Example 2: Full Bootstrap CI (B = 10,000)")
    pdf.body(
        "Problem: A nutritionist measures the daily calorie intake of "
        "25 adults. The sample mean is 2,150 kcal and the data are "
        "right-skewed. Using B = 10,000 bootstrap resamples, the "
        "researcher obtains the following bootstrap distribution "
        "summary:"
    )
    pdf.body(
        "Bootstrap mean of means: 2,148 kcal\n"
        "Bootstrap SE: 68.3 kcal\n"
        "2.5th percentile: 2,018 kcal\n"
        "97.5th percentile: 2,285 kcal"
    )
    pdf.bold_body("Step 1: Identify the percentile CI bounds")
    pdf.body("Lower bound = 2.5th percentile = 2,018 kcal")
    pdf.body("Upper bound = 97.5th percentile = 2,285 kcal")
    pdf.bold_body("Step 2: State the CI")
    pdf.formula("95% Bootstrap CI: (2,018 kcal,  2,285 kcal)")
    pdf.bold_body("Step 3: Interpret")
    pdf.body(
        "We are 95% confident that the true mean daily calorie intake "
        "of the adult population is between 2,018 and 2,285 kcal. "
        "Because the data are skewed, the bootstrap CI is preferred "
        "over a t-interval, which assumes normality."
    )

    # S6 Visualizations
    pdf.section("Section 6: Visualizations & Interpretation")
    pdf.bold_body("Bootstrap Distribution Histogram")
    pdf.body(
        "Plot a histogram of the B bootstrap statistics. It should be "
        "roughly bell-shaped and centred near the original sample "
        "statistic. The spread of this histogram is the bootstrap "
        "standard error."
    )
    pdf.bold_body("Percentile Cutoffs")
    pdf.body(
        "On the bootstrap histogram, draw vertical lines at the "
        "2.5th and 97.5th percentiles. The region between these lines "
        "represents the 95% bootstrap confidence interval."
    )
    pdf.bold_body("Comparison with Original Sample")
    pdf.body(
        "Overlay the original sample distribution (e.g., a dot plot) "
        "with the bootstrap distribution of the mean. The bootstrap "
        "distribution is narrower, reflecting the reduced variability "
        "of the mean compared to individual observations."
    )

    # S7 Misconceptions
    pdf.section("Section 7: Common Misconceptions & Mistakes")
    pdf.numbered(1,
        "Bootstrapping creates new data. WRONG. It only resamples "
        "from the existing data. No new information is generated; "
        "the method simply uses the data more efficiently to estimate "
        "sampling variability.")
    pdf.numbered(2,
        "Bootstrapping always works. It can fail when the sample is "
        "too small or not representative of the population. It also "
        "performs poorly for extreme quantiles (e.g., the maximum).")
    pdf.numbered(3,
        "The bootstrap distribution is centred at the true parameter. "
        "It is centred at the observed statistic. The spread (SE) is "
        "the useful output, not the centre.")
    pdf.numbered(4,
        "Resampling without replacement. Bootstrap samples MUST be "
        "drawn WITH replacement; otherwise every resample is identical "
        "to the original sample (just in a different order).")
    pdf.numbered(5,
        "Using too few resamples. B = 50 or B = 100 is insufficient "
        "for stable CI estimates. Use at least B = 1,000 for standard "
        "errors and B = 10,000 for confidence intervals.")

    # S8 Connections
    pdf.section("Section 8: Connections to Other Topics")
    pdf.bold_body("See Also")
    pdf.bullet(
        "Confidence Intervals: Bootstrapping provides an alternative "
        "way to construct CIs when parametric formulas require "
        "assumptions that are not met."
    )
    pdf.bullet(
        "Normal Distribution / Central Limit Theorem: When the CLT "
        "applies (large n), parametric CIs and bootstrap CIs will "
        "agree closely. Bootstrapping shines when n is small or the "
        "distribution is non-normal."
    )
    pdf.bullet(
        "Nonparametric Tests: Bootstrapping shares the philosophy "
        "of nonparametric methods \u2014 making minimal assumptions "
        "about the population distribution."
    )
    pdf.bullet(
        "Hypothesis Testing: The bootstrap can also be used for "
        "hypothesis testing (permutation tests are a related "
        "resampling approach)."
    )

    out = os.path.join(BASE, "bootstrapping",
                       "bootstrapping_notes.pdf")
    pdf.output(out)
    print(f"Created {out}  ({os.path.getsize(out)} bytes)")


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    gen_binomial()
    gen_confidence_intervals()
    gen_bootstrapping()
    print("\nAll 3 foundational PDFs generated.")
