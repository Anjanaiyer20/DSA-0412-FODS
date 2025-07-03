from scipy.stats import f_oneway

group1 = [85, 86, 88]
group2 = [78, 76, 80]
group3 = [90, 92, 89]

f_stat, p_val = f_oneway(group1, group2, group3)
print("F-test (ANOVA): F =", f_stat, ", p =", p_val)
