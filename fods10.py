import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [20000, 30000, 40000, 50000]
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title("Monthly Sales (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
plt.bar(months, sales, color='orange')
plt.title("Monthly Sales (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
