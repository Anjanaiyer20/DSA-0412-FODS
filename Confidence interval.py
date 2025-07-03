from statsmodels.stats.proportion import proportion_confint

count, nobs = 80, 100
ci_low, ci_upp = proportion_confint(count, nobs, alpha=0.05, method='normal')
print("95% CI for proportion:", (ci_low, ci_upp))
