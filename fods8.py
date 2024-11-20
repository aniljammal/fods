import pandas as pd
sales_data = pd.DataFrame({
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'D', 'B', 'A'],
    'quantity_sold': [2, 5, 3, 4, 2, 1, 6, 7, 4, 2]
})
total_sales = sales_data.groupby('product_name')['quantity_sold'].sum()
top_5_products = total_sales.nlargest(5)
print("Top 5 products by quantity sold:\n", top_5_products)
