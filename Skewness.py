import pandas as pd

x = pd.Series([8, 3, 2, 10, 11, 3, 6, 5, 6, 8])
y = pd.Series([4, 12, 1, 12, 9, 4, 9, 6, 1, 14])

for name, data in zip(['x', 'y'], [x, y]):
    skewness = data.skew()
    pearson = 3 * (data.mean() - data.median()) / data.std()
    print(f"{name} → Skewness: {skewness:.2f}, Pearson: {pearson:.2f}")
