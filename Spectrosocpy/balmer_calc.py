import numpy as np
from scipy.optimize import curve_fit
import math

#Mercury Numbers
# Angles: 14.50514,19.00792,20.50299,20.50275,31.75555, 47.00243, 44.00451,44.00458
# Wavelengths: 4046.56, 5460.74, 5789.66, 5790.66,8093.12, 10921.48, 11579.32, 11581.32

# Hydrogen
# 15.25, 17.24167, 23.75
# 410.17, 434.05, 656.28

angles_measured = np.array([14.50514,19.00792,20.50299,20.50275])
#angles_measured = [  for m in angles_measured]
means = np.array([4046.56, 5460.74, 5789.66, 5790.66])



def func(x1, a, b):
  return a * np.exp(b * x1)
guess = [100, -0.1]
popt = curve_fit(func, angles_measured, means, p0 = guess)

print(popt)
print(popt[1])

hydro = np.array([15.25, 17.24167, 23.75])

hydro = [ popt[0] * ( math.sin(math.radians(theta_m - popt[1])) - math.sin(math.radians(popt[1])) ) for theta_m in hydro]
hydro = [h**(-9) ]
print(hydro)

n_vals = np.array([6,5,3])

popt = curve_fit(func, hydro, means, p0 = guess)
