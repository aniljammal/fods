import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [30, 32, 35, 40, 45, 50]
rainfall = [100, 80, 60, 40, 20, 10]
plt.plot(months, temperature, color='red', label='Temperature')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()
plt.scatter(months, rainfall, color='blue', label='Rainfall')
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.show()
