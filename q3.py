import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {'ProductCategory': ['Electronics', 'Clothing', 'Home Decor', 'Electronics', 'Clothing', 'Books'],
        'SalesAmount': [5000, 3000, 4500, 6000, 2000, 1500]}

df = pd.DataFrame(data)

# Group by category and sum sales
sales_by_category = df.groupby('ProductCategory')['SalesAmount'].sum()

# Line plot
sales_by_category.plot(kind='line', title='Line Plot')
plt.ylabel('Total Sales')
plt.show()

# Scatter plot
sales_by_category.plot(style='o', title='Scatter Plot')
plt.ylabel('Total Sales')
plt.show()

# Bar plot
sales_by_category.plot(kind='bar', title='Bar Plot')
plt.ylabel('Total Sales')
plt.show()
