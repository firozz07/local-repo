import numpy as np
def regression_x_on_y(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_y2 = np.sum(y * y)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_y2 - sum_y ** 2)
    a = (sum_x - b * sum_y) / n
    return a, b
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 4, 6, 8])
a, b = regression_x_on_y(x, y)
print("Intercept =", a)
print("Slope =", b)
print("Regression Line:")
print("X = {:.2f} + {:.2f}Y".format(a, b))