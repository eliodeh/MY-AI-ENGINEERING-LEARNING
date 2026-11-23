# statistics for machine learning:
Never ship a 0.02 improvement without proving it isn't noise. Statistics separates signal from randomness. Without it, you're guessing.

# Statistical vs Practical Significance:
With n = 1M, a 0.03% gain gives p = 0.001 — statistically significant, practically meaningless. Always report both p-value (is it real?) and effect size (does it matter?).

# Parametric vs Non-Parametric:
. Parametric (t-test, Pearson, ANOVA): assumes normality, more power, needs large n

. Non-parametric (Wilcoxon, Mann-Whitney, Spearman): no assumptions, better for small n / skewed / ordinal data

. In ML with 5–10 CV folds → prefer Wilcoxon signed-rank over t-test

A p-value says "is it real?" Effect size says "does it matter?" A CI says "how sure am I?" Bootstrap gives all three without assuming normality — and with small CV folds, prefer non-parametric tests.

