---
title: "Two-Way ANOVA — How-To"
author: MA235 Team
---

# Overview
Tests main effects of two factors (A and B) and their interaction on a numeric response.

## Assumptions
1. Random, independent observations.
2. Approximately normal residuals for each cell.
3. Equal variances across cell combinations.

## Hypotheses
- **Main effect A:** H₀: all A means equal.
- **Main effect B:** H₀: all B means equal.
- **Interaction:** H₀: no interaction between A and B.

## Procedure
1. Organize data by factor levels (cells).
2. Compute sums of squares: SS_A, SS_B, SS_AB, SS_Error.
3. df_A = a − 1, df_B = b − 1, df_AB = (a − 1)(b − 1), df_Error = N − ab.
4. MS = SS/df for each component.
5. F_A = MS_A / MS_Error (similar for B and AB).
6. Compare each F to F_{α, df_component, df_Error}; compute p-values.
7. If interaction is significant, interpret with interaction plots before discussing main effects.
8. Report effect sizes (η²) for each component.
9. Optionally run post-hoc tests within significant factors.

## Related Tests
- One-way ANOVA (single factor).
- MANOVA when multiple responses exist.
