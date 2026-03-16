---
title: "Type I and Type II Errors"
author: MA235 Team
---

# Definitions
- **Type I Error (False Positive):** Rejecting a true H₀; probability = α.
- **Type II Error (False Negative):** Failing to reject a false H₀; probability = β.

# Outcomes Summary
- H₀ true & reject H₀ → **Type I error** (probability α).
- H₀ true & fail to reject → **Correct** (confidence = 1 − α).
- H₀ false & reject H₀ → **Correct** (power = 1 − β).
- H₀ false & fail to reject → **Type II error**.

# Contextual Examples
- **Two-sample t-test:** Type I → conclude two groups differ when they do not; Type II → miss a real difference.
- **Chi-square test of independence:** Type I → claim association when variables are independent; Type II → miss a true association.

# Managing Errors
- Lower α reduces Type I risk but usually increases β; higher α does the opposite.
- Increasing sample size reduces both errors by decreasing standard error.
- Choosing more sensitive tests or better measurement instruments can increase power (1 − β).

# Communication Tips
Always describe errors in context: specify the actual claim (means differ, proportions equal, etc.) so students grasp consequences. Avoid saying “accept H₀”; instead use “fail to reject H₀.”

# Related Documents
- `test_power_and_examples.pdf` explains how to quantify β and power.
- Per-topic how-to PDFs provide scenario-specific Type I/II statements.
