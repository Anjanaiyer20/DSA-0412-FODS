import numpy as np
from scipy.stats import ttest_1samp

sample = np.array([20, 22, 19, 24, 21])
mu = 20

t_stat, p_val = ttest_1samp(sample, mu)
print("T-test: t =", t_stat, ", p =", p_val)
