import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, .1)


def y(val):
    return val**5


plt.plot(x, y(x))
plt.grid()
plt.xlabel("x (unit of x)")
plt.ylabel("y (unit of y)")
plt.title('y vs x')
plt.show()