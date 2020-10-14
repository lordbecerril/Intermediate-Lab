import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from scipy import stats


y = [1,2,3,4,5,6] # Meters
x = [0.6E-9, 4.4E-9, 7.3E-9, 10.6E-9,13.8E-9,17.6E-9] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[1.5,0.5,0.2,0.2,0.1,0.2], fmt = 'o')
plt.title("Linear Fit of Rising Edge")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
plt.show()
