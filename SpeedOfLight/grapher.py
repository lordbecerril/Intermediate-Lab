import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from scipy import stats

print("In Air")

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
plt.title("Linear Fit of Rising Edge in Air")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.savefig("./inair.png")
plt.clf()




print("In pipe")

y = [4,5,5,6,6] # Meters
x = [7.6E-9, 3E-9, 4.6E-9, 16.5E-9, 17.8E-9] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[2.6, 5.3, 4.3, 0.3, 2.6], fmt = 'o')
plt.title("Linear Fit of Rising Edge in Pipe")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.savefig("./inpipe.png")

plt.clf()

print("In water")
y = [4,5,6] # Meters
x = [12.6E-9,14.6E-9,20.2E-9] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[1.5,2.5,0.9], fmt = 'o')
plt.title("Linear Fit of Rising Edge in Water")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.savefig("./inwater.png")

plt.clf()


print("Averages from Air")

y = [1,2,3,4,5,6] # Meters
x = [2.1E-9, 4.0E-9, 7.3E-9, 10.6E-9,13.7E-9,17.6E-9] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[1.5,0.5,0.2,0.2,0.1,0.2], fmt = 'o')
plt.title("Linear Fit of Rising Edge in Air")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.clf()

print("Averages from Pipe")

y = [4,5,5,6,6] # Meters
x = [10.2E-9, 8.3E-9, 8.3E-9, 16.3E-9, 15.2E-9] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[2.6, 5.3, 4.3, 0.3, 2.6], fmt = 'o')
plt.title("Linear Fit of Rising Edge in Pipe")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.clf()


print("Averages from water")
y = [4,5,6] # Meters
x = [14.1E-9,17.1E-9,21.1E-9] #rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[1.5,2.5,0.9], fmt = 'o')
plt.title("Linear Fit of Rising Edge in Water")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.clf()


##############################################
dist = [4,5,6] #Change for different distances
time = [15.6E-9, 17.1E-9,22E-9,] # Change for times

delta_t = []
for i in range(len(time)):
    V_avg = dist[i] / time[i] #Average Velocity calculation
    t = (3.17)/(3* V_avg - 2.99E8 - 2.028E8)
    delta_t.append(t)

print(delta_t)


y = dist  # Meters
x = delta_t#rising edges

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
#plt.plot(x,y,  'o', label='original data')
plt.plot(x, [intercept + slope * n for n in x], 'r', label='fitted line')
plt.errorbar(x,y,yerr=[1.5,2.5,0.9], fmt = 'o')
plt.title("Linear Fit of Rising Edge in Water")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
plt.show()
plt.clf()
