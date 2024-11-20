import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2, 1],
    'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06']),
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A'],
    'order_quantity': [2, 5, 3, 4, 2, 1]
})
orders_per_customer = order_data.groupby('customer_id').size()
avg_order_quantity = order_data.groupby('product_name')['order_quantity'].mean()
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()
print("Orders per customer:\n", orders_per_customer)
print("Average order quantity per product:\n", avg_order_quantity)
print("Earliest order date:", earliest_date)
print("Latest order date:", latest_date)
