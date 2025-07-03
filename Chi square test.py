from scipy.stats import chi2_contingency
import numpy as np

# 2x2 table: rows = gender, columns = vote preference
data = np.array([[30, 10], [20, 40]])

chi2, p, dof, expected = chi2_contingency(data)
print("Chi-Square Test: χ² =", chi2, ", p =", p)
