import pandas as pd
df = pd.read_csv("readmission_data.csv", encoding='utf-8') 
print("🔹 Original Dataset:\n")
print(df)
df_cleaned = df.dropna(subset=['age', 'gender', 'readmitted'])
print("\n✅ Cleaned Dataset (after dropping rows with nulls in 'age', 'gender', or 'readmitted'):\n")
print(df_cleaned)
