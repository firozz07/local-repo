import numpy as np
import matplotlib.pyplot as plt
# Generate random data
np.random.seed(10)
x = np.random.rand(100)
# Correlation data
y_pos = x + np.random.normal(0, 0.15, 100)
y_zero = np.random.rand(100)
y_neg = -x + np.random.normal(0, 0.15, 100)
# Create plots
plt.figure(figsize=(12,4))
# Negative Correlation
plt.subplot(1,3,1)
plt.scatter(x, y_neg, color='red')
plt.title("r = -0.85")
# No Correlation
plt.subplot(1,3,2)
plt.scatter(x, y_zero, color='blue')
plt.title("r = 0")
# Positive Correlation
plt.subplot(1,3,3)
plt.scatter(x, y_pos, color='green')
plt.title("r = 0.85")
plt.tight_layout()
plt.show()
