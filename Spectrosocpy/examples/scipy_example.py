import numpy as np
from scipy.optimize import curve_fit

#14.50514,19.00792,20.50299,20.50275,31.75555, 47.00243, 44.00451,44.00458
#4046.56, 5460.74, 5789.66, 5790.66,8093.12, 10921.48, 11579.32, 11581.32
exp_constants = np.array([31.75555, 47.00243, 44.00451,44.00458])
means = np.array([8093.12, 10921.48, 11579.32, 11581.32])



def func(x1, a, b):
  return a * np.exp(b * x1)
guess = [100, -0.1]
popt, pcov = curve_fit(func, exp_constants, means, p0 = guess)

print(popt)
