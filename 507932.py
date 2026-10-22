import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

# 1. Load data
df = pd.read_csv('archive\\results.csv')
data = df['Total']

# 2. Compute mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

print('Mean:', mean)
print('Standard Deviation:', std_dev)

# 3. Generate the normal distribution curve
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
y = norm.pdf(x, mean, std_dev)

# 4. Plot the normal distribution curve
plt.figure(figsize=(8, 5))

plt.plot(x, y, color='blue', label='Normal Distribution Curve')
plt.hist(data, bins=30, density=True, alpha=0.4, color='orange', label='Actual Data')

plt.axvline(mean, color='red', linestyle='--', label='Mean')
plt.axvline(mean + std_dev, color='green', linestyle=':', label='+1 Std Dev')
plt.axvline(mean - std_dev, color='green', linestyle=':', label='-1 Std Dev')

plt.title('Normal Distribution Curve of Total Marks')
plt.xlabel('Total Marks')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

# 5. Apply the Empirical (68-95-99.7) Rule
within_1std = np.mean(
    (data > mean - std_dev) & (data < mean + std_dev)
) * 100

within_2std = np.mean(
    (data > mean - 2 * std_dev) & (data < mean + 2 * std_dev)
) * 100

print(f'% of data within 1 std dev: {within_1std:.2f}%')
print(f'% of data within 2 std dev: {within_2std:.2f}%')