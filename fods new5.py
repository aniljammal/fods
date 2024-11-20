import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 3000, 2000, 1500, 1000]

plt.plot(months, sales, marker='o', color='purple', label="Sales Line Plot")
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

plt.bar(months, sales, color='cyan', label="Sales Bar Plot")
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()
