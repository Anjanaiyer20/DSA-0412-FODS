import pandas as pd

# Load CSV file
df = pd.read_csv("ecommerce_orders.csv")

# Show first 5 rows
print("Data Preview:")
print(df.head())

# Total Sales
print("Total Sales:", df['Total Price'].sum())

# Average Quantity
print("Average Quantity Ordered:", df['Quantity'].mean())

# Top-selling Products
top_products = df.groupby('Product ID')['Quantity'].sum().sort_values(ascending=False)
print("Top-Selling Products:")
print(top_products.head())
