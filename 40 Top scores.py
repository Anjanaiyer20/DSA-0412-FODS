import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create and save dataset
data = {
    'Name': ['Ronaldo','Messi','Neymar','Mbappe','Kane','Haaland','De Bruyne','Modric','Salah','Son'],
    'Age': [38, 36, 32, 25, 30, 24, 32, 38, 31, 30],
    'Position': ['Forward','Forward','Forward','Forward','Forward','Forward','Midfielder','Midfielder','Forward','Forward'],
    'Goals': [28, 30, 22, 34, 26, 33, 10, 4, 25, 18],
    'Salary': [500000, 550000, 450000, 600000, 400000, 520000, 470000, 300000, 410000, 390000]
}
df = pd.DataFrame(data)
df.to_csv("C:\\Users\\user\\OneDrive\\Documents\\Fundamentals of data science\\soccer_players.csv", index=False)

# Step 2: Read and analyze
df = pd.read_csv('soccer_players.csv')

print("Top 5 Goal Scorers:\n", df.nlargest(5, 'Goals')[['Name', 'Goals']])
print("\nTop 5 Highest Paid:\n", df.nlargest(5, 'Salary')[['Name', 'Salary']])

avg_age = df['Age'].mean()
print("\nAverage Age:", round(avg_age, 2))
print("\nPlayers Above Average Age:\n", df[df['Age'] > avg_age]['Name'])

# Step 3: Bar chart for position distribution
df['Position'].value_counts().plot(kind='bar', title='Player Position Distribution')
plt.xlabel('Position')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
