# Import required packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import numpy.polynomial.polynomial as poly
import math

# Function to calculate the exponential with constants a and b
def exponential(x, a, b):
    return a*np.exp(b*x)

# Generate dummy dataset
x = [14.50514,19.00792,20.50299,20.50275,31.75555, 47.00243, 44.00451,44.00458]
x = [math.sin(xi) for xi in x]
print(x)

y = [4046.56, 5460.74, 5789.66, 5790.66,8093.12, 10921.48, 11579.32, 11581.32]
#y = [math.sin(yi) for yi in y]

# calculate polynomial
z = np.polyfit(x, y, 1)
f = np.poly1d(z)

print(z)
print(f)


# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
