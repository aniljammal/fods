import numpy as np
import matplotlib.pyplot as plt
smoking_rates = np.array([10, 20, 30, 40, 50])  
lung_cancer_rates = np.array([5, 10, 15, 20, 25])
correlation = np.corrcoef(smoking_rates, lung_cancer_rates)[0, 1]
plt.scatter(smoking_rates, lung_cancer_rates, color='blue')
plt.title("Smoking vs Lung Cancer Rates")
plt.xlabel("Smoking Rates (%)")
plt.ylabel("Lung Cancer Rates (%)")
plt.show()
print("Correlation coefficient between smoking and lung cancer rates:", correlation)
