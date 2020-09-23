import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


# Grating equation
def grating_func(x, a, b):
    return a * (np.sin(np.radians(x-b))-np.sin(np.radians(b))) # Fitting a and b to grating equation

#def r_func(x, a):
#    return( (4 * np.power(x,2))/(a*(np.power(x,2) - 4)))

def r_func(x, a):
    return( a * ((1/4) - ( 1/ np.power(x,2))))



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
#plt.show()
plt.clf()



#hydrogen_angles = [15.25, 17.245, 23.837, 31.784, 35.992, 52.492]
hydrogen_angles = [ 15.25, 17.245, 23.837, 31.784, 35.992, 52.492]


calc_lambda_h = [d*(np.sin(np.radians(theta_m-theta_i))-np.sin(np.radians(theta_i))) for theta_m in hydrogen_angles]
#calc_lambda_h =[1/l for l in calc_lambda_h]
print("Calculated Wavelengths are ", calc_lambda_h)

n_vals = [6, 4, 3, 6, 4, 3]
#n_vals = [1/l for l in n_vals]

param, param_cov = curve_fit(r_func, n_vals, calc_lambda_h, p0 = 10000000)
print("R is", param*10**3)

# Create the plot
plt.figure(figsize=(6, 4))
plt.scatter(n_vals, calc_lambda_h, label='Data')
plt.plot(n_vals, r_func(n_vals, param[0]),
         label='Fitted function')
plt.legend(loc='best')
plt.show()
plt.clf()


z = np.polyfit( calc_lambda_h,n_vals, 1)
print(z)
