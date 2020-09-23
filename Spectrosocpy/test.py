import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


# Grating equation
def grating_func(x, a, b):
    return a * (np.sin(np.radians(x-b))-np.sin(np.radians(b))) # Fitting a and b to grating equation



x = [14.808, 19.475, 20.679, 20.665, 32.083 ,41.112 ,44.271 ,44.525] #Averaged Angles we gathered

#x = np.deg2rad(x)
print("Angles are ", x) #print the angles



y = [4046.56 , 5460.74 , 5789.66 , 5790.66  ,8093.12 ,10921.48 ,11579.32, 11581.32] # Wavelengths




# curve_fit() function takes the grating_func-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
param, param_cov = curve_fit(grating_func, x, y, p0 = [600,0])
print("Params are ", param)

d = param[0]
d = (1/d) * (1/(10**-10))* ((1*10**-3))
print("D is ",d)

theta_i = param[1]
print("Theta i is ", theta_i)

# Create the plot
plt.figure(figsize=(6, 4))
plt.scatter(x, y, label='Data')
plt.plot(x, grating_func(x, param[0], param[1]),
         label='Fitted function')
plt.legend(loc='best')
plt.show()
plt.clf()
