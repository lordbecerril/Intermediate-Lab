import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
'''
Mercury Numbers

  Lists will go in the order of Purple, Green, 1st yellow, 2nd  Yellow
  Order 1 Angles Averaged: 15.258, 19.5, 20.833, 20.73
  Order 2 Angles Averaged: 32.358, 41.133, 44.642, 45.0
  Order 3 Angles Averaged (only purple): 53.375
  Wavelengths m=1: 4046.56, 5460.74, 5789.66, 5790.66,
  Wavelengths m=2: 8093.12, 10921.48, 11579.32, 11581.32
  Wavelengths m=3: 12139.68
'''

# Wavelength Calc function
def func(x, a, b):
    return a * (np.sin(x-b)-np.sin(b)) # Fitting to

def func2(x,a):
    return ((4 * x**2)/(a*(x**2 - 4)))

# Left Hand Side of mercury data
hg_lhs = [15+(15.5/60), 19+(30/60), 20.5+(20/60), 20.5+(13.8/60), 32+(21.5/60), 41+(8/60), 44.5+(8.5/60), 44.5+(30/60), 53+(22.5/60)] # All orders
#hg_lhs = [15+(15.5/60), 19+(30/60), 20.5+(20/60), 20.5+(13.8/60)] # only order 1

hg_lhs = [round(answer, 3) for answer in hg_lhs] # This rounds to 1 decimal place
print("LHS Measured values are ", hg_lhs)

# Right hand side of mercury data
hg_rhs = [14+(21.5/60), 19+(27/60), 20.5+(1.5/60), 20.5+(6/60), 31.5+(18.5/60), 41+(5.5/60), 43.5+(24/60), 44+(3/60), 51.5+(21.5/60)]
#hg_rhs = [14+(21.5/60), 19+(27/60), 20.5+(1.5/60), 20.5+(6/60)] # only order 1

hg_rhs = [round(answer, 3) for answer in hg_rhs] # This rounds to 1 decimal place
print("RHS Measure values are ", hg_rhs)

# Take the average of the rhs and lhs of mercury data
average_hg = [] # Create an empty array
for i in hg_rhs: # loop through each value in hg_rhs
    #print(hg_rhs.index(i)) #TEST PRINT the indice of each value in hg_rhs
    a = (i + hg_lhs[hg_rhs.index(i)]) / 2 # Calculate the average and put in varaible a
    average_hg.append(round(a, 3)) # Append a to the array named average
average_hg = np.array(average_hg)
print("Average measured value is", average_hg)



#The given wavelengths in the order of purple, green, 1st yellow, and 2nd yellow
wavelengths_hg = [4046.56, 5460.74, 5789.66, 5790.66,8093.12, 10921.48, 11579.32, 11581.32, round(4046.56*3,2)] # All orders
#wavelengths_hg = [4046.56, 5460.74, 5789.66, 5790.66] # only order 1
wavelengths_hg = np.array(wavelengths_hg)
print("Wavelengths are ", wavelengths_hg)

func = np.vectorize(func)

guess = [600, 0]
popt, pcov = curve_fit(func, average_hg, wavelengths_hg, p0 = guess)
print("popt is ", popt)
d = (1/popt[0])* 10**6
theta_i = (popt[1])
print("d is ", d)
print("Theta i is ", theta_i)


plt.figure(figsize=(6, 4))
plt.scatter(average_hg, wavelengths_hg, label='Data')
plt.plot(average_hg, [func(a, popt[0], popt[1]) for a in average_hg],
         label='Fitted function')

plt.legend(loc='best')

plt.show()
plt.clf()

'''
Hydrogen:
  Lists will go in the order of Purple, Blue, Red
'''
h_rhs = [(15+(28/60)+15+(24/60))/2, (17+(19/60)+17+(15/60))/2, (23.5+(1/60)+23.5+(30/60))/2, (31.5+(5/60)+31.5+(4/60))/2, (35.5+(25/60)+35.5+(24/60))/2,(51.5+(19/60)+51.5+(23/60))/2]
h_rhs = [round(answer, 3) for answer in h_rhs] # This rounds to 1 decimal place
print("Hydrogen RHS is ", h_rhs)

h_lhs = [(15+(3/60)+15+(5/60))/2, (17+(15/60)+17+(10/60))/2,(23.5+(25/60)+23.5+(25/60))/2,(31.5+(30/60)+31.5+(29/60))/2,(36+(4/60)+36+(5/60))/2,(53+(8/60)+53+(8/60))/2]
h_lhs = [round(answer, 3) for answer in h_lhs] # This rounds to 1 decimal place
print("Hydrogen LHS is ", h_lhs)

average_h = [] # Create an empty array
for i in h_rhs: # loop through each value in hg_rhs
    #print(hg_rhs.index(i)) #TEST PRINT the indice of each value in hg_rhs
    a = (i + h_lhs[h_rhs.index(i)]) / 2 # Calculate the average and put in varaible a
    average_h.append(round(a, 3)) # Append a to the array named average
print("Average measured value is", average_h)

#Now we Calculate wavelengths for hydrogen
calc_lambda_h = [d*(math.sin(math.radians(theta_m-theta_i))-math.sin(math.radians(theta_i))) for theta_m in average_h]
print("Calculated Wavelengths are ", calc_lambda_h)

inverse_lambda = [1/l for l in calc_lambda_h]

n_vals = [6, 4, 3, 6, 4, 3]
guess = [1, 0.01]
popt, pcov = curve_fit(func, calc_lambda_h,n_vals , p0=guess)
print("popt is ", popt)

plt.figure(figsize=(6, 4))
plt.scatter( calc_lambda_h,n_vals, label='Data')
plt.plot(calc_lambda_h, [func2(a, popt[0], popt[1]) for a in calc_lambda_h],
         label='Fitted function')

plt.legend(loc='best')

plt.show()
plt.clf()

'''
angles_measured = np.array([14.50514,19.00792,20.50299,20.50275])
#angles_measured = [  for m in angles_measured]
wavelengths_hg = np.array([4046.56, 5460.74, 5789.66, 5790.66])




def func(x1, a, b):
  return a * np.exp(b * x1)

guess = [100, -0.1]
popt = curve_fit(func, angles_measured, wavelengths_hg, p0 = guess)

print(popt)
print(popt[1])


# Hydrogen
# Measured Angles: 15.25, 17.24167, 23.75
# Wavelengths: 410.17, 434.05, 656.28

# Measured Hydrogen Angles
hydro = np.array([15.25, 17.24167, 23.75])

# Calculating Hydrogen Wavelengths
hydro = [ popt[0] * ( math.sin(math.radians(theta_m - popt[1])) - math.sin(math.radians(popt[1])) ) for theta_m in hydro]
hydro = [h**(-9) ]
print(hydro)

n_vals = np.array([6,5,3])

popt = curve_fit(func, hydro, wavelengths_hg, p0 = guess)
'''
