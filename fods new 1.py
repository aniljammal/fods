import pandas as pd
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 101, 103, 104],
    'ProductID': [201, 202, 203, 201, 202],
    'Quantity': [2, 1, 4, 3, 2],
    'TotalPrice': [20.0, 15.0, 40.0, 30.0, 25.0]
}
orders = pd.DataFrame(data)
sales_per_customer = orders.groupby('CustomerID')['TotalPrice'].sum()
quantity_per_product = orders.groupby('ProductID')['Quantity'].sum()
avg_order_value = orders['TotalPrice'].mean()
print("Sales per customer:\n", sales_per_customer)
print("Quantity sold per product:\n", quantity_per_product)
print("Average order value:", avg_order_value)
