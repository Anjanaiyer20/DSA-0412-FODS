import pandas as pd

# Load your CSV file (make sure it's in the same folder as this script)
df = pd.read_csv("readmission_data.csv", encoding='utf-8')

# Display first 5 rows
print(df.head())
