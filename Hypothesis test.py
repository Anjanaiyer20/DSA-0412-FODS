from scipy.stats import norm
import numpy as np

# Sample sizes
n1, n2 = 100, 120
# Means
x1, x2 = 6.2, 5.8
# Standard deviations
s1, s2 = 1.5, 1.2

z = (x1 - x2) / np.sqrt(s1**2/n1 + s2**2/n2)
p = 2 * (1 - norm.cdf(abs(z)))
print("Z-score:", z, "\nP-value:", p)
print("Significant difference" if p < 0.05 else "Not significant")
