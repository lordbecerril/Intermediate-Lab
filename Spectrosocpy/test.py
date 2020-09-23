import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
import math
from matplotlib import pyplot as plt

# numpy.linspace with the given arguments
# produce an array of 40 numbers between 0
# and 10, both inclusive
#x = [14.808, 19.475, 20.679, 20.665, 32.083 ,41.112 ,44.271 ,44.525 ,52.617]
x = [14.808, 19.475, 20.679, 20.665, 32.083,41.112]

#x = np.deg2rad(x)
print("Angles are ", x)


# y is another array which stores 3.45 times
# the sine of (values in x) * 1.334.
# The random.normal() draws random sample
# from normal (Gaussian) distribution to make
# them scatter across the base line


#y = [4046.56 , 5460.74 , 5789.66 , 5790.66  ,8093.12 ,10921.48 ,11579.32, 11581.32, 12139.68]
y = [4046.56 , 5460.74 , 5789.66 , 5790.66  ,8093.12 ,10921.48]


# Test function with coefficients as parameters
def test(x, a, b):
    #return a * np.sin(b * x)
    return a * (np.sin(x-b)-np.sin(b)) # Fitting to

# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
param, param_cov = curve_fit(test, x, y, p0 = [600,0])
print("Params are ", param)
#print(param_cov)

d = param[0]



plt.figure(figsize=(6, 4))
plt.scatter(x, y, label='Data')
plt.plot(x, test(x, param[0], param[1]),
         label='Fitted function')

plt.legend(loc='best')

plt.show()
plt.clf()
