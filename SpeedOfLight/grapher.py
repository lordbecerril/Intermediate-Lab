import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from scipy import stats


x = [1,2,3,4,5,6] # Meters
y = [0.6, 4.4, 7.3, 10.6,13.8,17.6] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("R using linregress is ", ((slope)*(1/(10**9)) ))
print("Standard Error is ", std_err)
plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.title("Linear Fit ")
plt.xlabel("Distance")
plt.ylabel("Time")
plt.legend()
plt.show()
