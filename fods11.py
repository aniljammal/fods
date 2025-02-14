import matplotlib.pyplot as plt
days = range(1, 31)
sales = [100 + i * 2 for i in days]
plt.plot(days, sales, color='blue', label='Daily Sales')
plt.title("Daily Sales (Line Plot)")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.show()
plt.scatter(days, sales, color='green', label='Daily Sales')
plt.title("Daily Sales (Scatter Plot)")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.show()
plt.bar(days, sales, color='red', label='Daily Sales')
plt.title("Daily Sales (Bar Plot)")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.show()
