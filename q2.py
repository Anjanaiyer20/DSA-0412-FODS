import pandas as pd
import matplotlib.pyplot as plt

data = {'Smoking': [20, 15, 5, 25, 30, 10, 18, 22, 8, 12],
        'LungCancer': [5, 4, 1, 6, 8, 2, 3, 7, 1, 2]}
df = pd.DataFrame(data)

print("Correlation:", df['Smoking'].corr(df['LungCancer']))

plt.scatter(df['Smoking'], df['LungCancer'])
plt.xlabel('Smoking')
plt.ylabel('Lung Cancer')
plt.title('Smoking vs Lung Cancer')
plt.show()
