


import matplotlib.pyplot as plt

import numpy as np

from math import exp
from math import factorial
from math import log
import statistics

from scipy.stats import poisson
from scipy.stats import norm


from scipy.stats import norm
from scipy.stats import chisquare



# Starting with mercury
LHS = [15.004305556, 19.00833333, 20.503833333] # Purple, green, yellow

x = [14.50514,19.00792,20.50299,20.50275,31.75555, 47.00243, 44.00451,44.00458]

y = [4046.56, 5460.74, 5789.66, 5790.66,8093.12, 10921.48, 11579.32, 11581.32]

#y = [yi*2 for yi in y]
#print(y)

plt.plot(x, y, 'o')

m, b = np.polyfit(x, y, 1)
print("m is ", m)
print("b is ", b)

plt.plot(x, [(m*xs)+b for xs in x])

plt.show()
