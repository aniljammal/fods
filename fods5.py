import numpy as np
fuel_efficiency = np.array([25, 30, 28, 35, 40])
average_efficiency = np.mean(fuel_efficiency)
percentage_improvement = ((fuel_efficiency[4] - fuel_efficiency[1]) / fuel_efficiency[1]) * 100
print("Average fuel efficiency:", average_efficiency)
print("Percentage improvement between model 2 and model 5:", percentage_improvement)
