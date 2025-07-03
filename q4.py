import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'OrderID': ['20240101-001', '20240102-002', '20240101-003', '20240103-001'],
    'CustomerID': ['C1', 'C2', 'C1', 'C3'],
    'ProductID': ['P1', 'P2', 'P3', 'P1'],
    'Quantity': [2, 1, 3, 4],
    'TotalPrice': [200, 150, 300, 400]
}

df = pd.DataFrame(data)

# Extract 'Order Date' from OrderID (first 8 digits assumed to be YYYYMMDD)
df['Order Date'] = pd.to_datetime(df['OrderID'].str[:8])

# Filter for a specific customer
customer_orders = df[df['CustomerID'] == 'C1']

# Total spent by each customer
total_by_customer = df.groupby('CustomerID')['TotalPrice'].sum()

# Histogram of Total Price
plt.hist(df['TotalPrice'], bins=5)
plt.title('Distribution of Total Price')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.show()
