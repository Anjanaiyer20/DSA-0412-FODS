import pandas as pd
import matplotlib.pyplot as plt

# i) Read the data
marks = pd.read_csv("marks.csv")

# ii) First and last 5 rows
print(marks.head())         # First 5
print(marks.tail())         # Last 5

# Purpose of describe():
# Gives summary statistics (mean, std, min, max, etc.)

# iv) Select 3rd to 6th row (index 2 to 5)
print(marks.iloc[2:6])

# v) Select rows where M3 > 84
print(marks[marks['M3'] > 84])

# vi) Filter rows with missing values
print(marks[marks.isnull().any(axis=1)])

# vii) Remove rows with missing values
print(marks.dropna())

# viii) Sort M1 column in descending order
print(marks.sort_values(by='M1', ascending=False))

# ix) Plot the table (bar chart for marks)
marks.set_index('NAME')[['M1','M2','M3']].plot(kind='bar')
plt.ylabel("Marks")
plt.title("Student Marks")
plt.tight_layout()
plt.show()

# x) marks.ix[3:6, ['m2','m3']] → outdated method, use loc or iloc
# Updated version:
print(marks.loc[3:6, ['M2', 'M3']])
