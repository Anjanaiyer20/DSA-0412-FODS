import matplotlib.pyplot as plt

# Sample sales data
days = [1, 5, 10, 15, 20, 25, 30]
sales = [100, 150, 180, 130, 170, 200, 220]

# Line plot
plt.plot(days, sales, label='Line', marker='o')
# Scatter plot
plt.scatter(days, sales, color='red', label='Scatter')

plt.title("Sales Over Time")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()
# Total orders per customer
orders_per_customer = order_data['customer ID'].value_counts()
print("Orders per customer:\n", orders_per_customer)

# Average quantity per product
avg_qty_per_product = order_data.groupby('product name')['order quantity'].mean()
print("Average order quantity per product:\n", avg_qty_per_product)

# Earliest and latest order date
print("Earliest:", order_data['order date'].min())
print("Latest:", order_data['order date'].max())
top_5_products = df.groupby('product name')['order quantity'].sum().nlargest(5)
print("Top 5 sold products:\n", top_5_products)
