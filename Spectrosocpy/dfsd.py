import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit

from matplotlib import pyplot as plt

# numpy.linspace with the given arguments
# produce an array of 40 numbers between 0
# and 10, both inclusive
x = [14.50514,19.00792,20.50299,20.50275]
y = [4046.56, 5460.74, 5789.66, 5790.66]
# Test function with coefficients as parameters
def test(x, a, b):
    return a * np.sin(b * x)

# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
param, param_cov = curve_fit(test, x, y)


print("Sine funcion coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)

# ans stores the new y-data according to
# the coefficients given by curve-fit() function
ans = [(param[0]*(np.sin(param[1]*x1))) for x1 in x ]

'''Below 4 lines can be un-commented for plotting results
using matplotlib as shown in the first example. '''

plt.plot(x, y, 'o', color ='red', label ="data")
plt.plot(x, ans, '--', color ='blue', label ="optimized data")
# plt.legend()
# plt.show()
