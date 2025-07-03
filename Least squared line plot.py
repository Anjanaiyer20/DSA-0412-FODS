import numpy as np
import matplotlib.pyplot as plt

x = np.array([8, 3, 2, 10, 11, 3, 6, 5, 6, 8])
y = np.array([4, 12, 1, 12, 9, 4, 9, 6, 1, 14])

m, b = np.polyfit(x, y, 1)
print(f"Line: y = {m:.2f}x + {b:.2f}")

plt.scatter(x, y)
plt.plot(x, m*x + b, color='red')
plt.title("Line of Best Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
