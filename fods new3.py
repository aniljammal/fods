import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Category': ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Toys'],
    'TotalSales': [10000, 8000, 12000, 5000, 7000]
}
sales_data = pd.DataFrame(data)

plt.plot(sales_data['Category'], sales_data['TotalSales'], marker='o', label="Line Plot")
plt.title("Sales by Category - Line Plot")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.legend()
plt.show()

plt.scatter(sales_data['Category'], sales_data['TotalSales'], color='green', label="Scatter Plot")
plt.title("Sales by Category - Scatter Plot")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.legend()
plt.show()

plt.bar(sales_data['Category'], sales_data['TotalSales'], color='orange', label="Bar Plot")
plt.title("Sales by Category - Bar Plot")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.legend()
plt.show()
