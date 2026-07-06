import numpy as np
def regression_y_on_x(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x * x)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / n
    return a, b
x = np.array([2, 4, 6, 8, 10])
y = np.array([3, 5, 7, 9, 11])
a, b = regression_y_on_x(x, y)
print("Intercept =", a)
print("Slope =", b)
print("Regression Line:")
print("Y = {:.2f} + {:.2f}X".format(a, b))