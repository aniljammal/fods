import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 32, 35, 40, 45, 50, 48, 46, 40, 35, 32, 30]
rainfall = [100, 80, 60, 40, 20, 10, 15, 25, 50, 75, 90, 100]

plt.plot(months, temperature, color='red', label="Temperature")
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()

plt.scatter(months, rainfall, color='blue', label="Rainfall")
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.show()
