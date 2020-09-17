import numpy as np
from scipy.optimize import curve_fit
import math

#14.50514,19.00792,20.50299,20.50275,31.75555, 47.00243, 44.00451,44.00458
#4046.56, 5460.74, 5789.66, 5790.66,8093.12, 10921.48, 11579.32, 11581.32
exp_constants = np.array([14.50514,19.00792,20.50299,20.50275])
#exp_constants = [  for m in exp_constants]
means = np.array([4046.56, 5460.74, 5789.66, 5790.66])



def func(x1, a, b):
  return a * np.exp(b * x1)
guess = [100, -0.1]
popt, pcov = curve_fit(func, exp_constants, means, p0 = guess)

print(popt)
print(popt[1])

exp_constants = [ popt[0] * ( math.sin(math.radians(theta_m - popt[1])) - math.sin(math.radians(popt[1])) ) for theta_m in exp_constants]
print(exp_constants)

n_vals = np.array([1,1,1,1])

def func(x1, a, b):
  return a * np.exp(b * x1)
guess = [100, -0.1]
popt, pcov = curve_fit(func, exp_constants, n_vals, p0 = guess)

print(popt)
print(popt[1])
