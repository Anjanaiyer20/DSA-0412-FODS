import pandas as pd

# ✅ Correct URL for Red Wine Quality dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

# Load the dataset (note: separator is semicolon `;`)
df = pd.read_csv(url, sep=';')

# Show the first 5 rows
print("📂 Wine Quality Dataset Loaded Successfully:\n")
print(df.head())

# Save it in the current directory
df.to_csv("winequality-red.csv", index=False)
print("\n✅ Saved as 'winequality-red.csv' in the current folder.")
