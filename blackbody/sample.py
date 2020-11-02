import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit

# this function is for S(λ;T) = r(λ) * ε(λ;T) * λ^-5 * e^(-h*c/λ*kB*T)
def func(x, a, b,c,d,e,f):
    return a * b * (c**-5) * np.exp((-1*d*e) / (c*f*x))

# this function is for S(λ;T) = r(λ) * ε(λ;T) * λ^-5 * e^(-h*c/λ*kB*T)
def func2(x, a, b):
    return a * (656**-5) * np.exp((-1*b*2.99E9) / (656*1.38E-23*x))

def func3(x, a, b,c,d):
    return a + np.log(b*c*656-5)- ((d*2.99E9)/(656E-5*1.38E-23*x))



temps = [1525, 1550, 1575, 1600, 1650, 1675, 1700, 1725, 1750, 1775, 1800, 1850, 1875, 1890, 1910, 1925, 1950, 1975, 1990, 2000, 2025, 2050, 2075, 2100, 2110, 2125, 2150, 2160, 2175, 2190, 2200, 2225, 2250, 2275, 2290, 2300, 2310, 2325, 2350, 2375, 2380, 2390, 2400, 2410, 2425, 2445, 2450, 2475, 2490, 2500, 2510, 2525, 2550, 2560, 2575, 2580, 2590, 2600, 2610, 2625, 2650, 2660, 2670, 2690, 2700, 2710, 2720, 2750, 2775]
temps = np.array(temps)

signals = [1.1, 1.6, 2.16, 2.87, 3.77, 4.84, 6.12, 7.65, 9.51, 11.5, 13.8, 16.4, 19.3, 22.6, 27.7, 30.199999999999996, 34.6, 39.4, 43.7, 49.5, 53.49999999999999, 61.5, 68.8, 76.2, 87.8, 89.2, 92.5, 96.7, 106.0, 115.99999999999999, 126.0, 136.0, 147.0, 159.0, 171.0, 184.0, 198.0, 211.0, 225.0, 239.99999999999997, 255.0, 271.0, 289.0, 305.0, 322.0, 341.0, 360.0, 377.0, 397.0, 417.0, 436.99999999999994, 459.0, 481.99999999999994, 505.0, 528.0, 549.0, 574.0, 587.0, 612.0, 636.0, 663.0, 688.0, 713.0, 740.0, 760.0, 780.0, 792.0, 807.0, 823.0000000000001]
signals = np.array(signals)


p0 =[4.30739944e-13,4.30739944e-13, 656E-9, 6.626E-34, 2.99E8,1.38E-23]
popt, pcov = curve_fit(func, temps, signals, maxfev=1000)
print(popt)
print(pcov)
print('r(λ)=', popt[0])
print('ε(λ;T)=', popt[1])
print('λ=', popt[2])
print('h=', popt[3])
print('c=', popt[4])
print('kB=', popt[5])

plt.scatter(temps, signals)
plt.plot(temps, func(temps, popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('signals(Watts)')
plt.legend()
plt.show()
plt.clf()



#p0 =[4.30739944e-13,6.626E-34]
popt, pcov = curve_fit(func, temps, signals, maxfev=1000)
print(popt)
print(pcov)
print('r(λ)*ε(λ;T)=', popt[0])
print('h=', popt[3])
plt.scatter(temps, signals)
plt.plot(temps, func2(temps, popt[0],popt[1]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('signals(Watts)')
plt.legend()
plt.show()
plt.clf()

p0 =[4.30739944e-13,6.626E-34]
popt, pcov = curve_fit(func3, temps, np.log(signals), maxfev=1000)
print(popt)
print(pcov)
print('constant=', popt[0])
print('r=', popt[1])
print('epsilon=', popt[2])
print('h=', popt[3])

plt.scatter(temps, np.log(signals))
plt.plot(temps, func3(temps, popt[0],popt[1],popt[2],popt[3]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('ln(Signals) (Watts)')
plt.legend()
plt.show()
plt.clf()
