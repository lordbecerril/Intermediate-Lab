
import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from scipy import stats



def new_grapher(ret, red, fed, fet, tit, savename):
    # This is for the better data
    # ret = rising edge time  (x-axis)
    # red = rising edge distance (y-axis)
    # fed = falling edge distance (y_axis)
    # fet = falling edge time (x_axis)
    #slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    slope_r, intercept_r, r_value_r, p_value_r, std_err_r = stats.linregress(ret,red)
    print("Sloper is ", slope_r)
    print("Interceptr is ", intercept_r)
    print("R valuer is ", r_value_r)
    print("P valuer is ", p_value_r)
    print("Standard Errorr is ", std_err_r)
    slope_f, intercept_f, r_value_f, p_value_f, std_err_f = stats.linregress(fet,fed)
    print("Slopef is ", slope_f)
    print("Interceptf is ", intercept_f)
    print("R valuef is ", r_value_f)
    print("P valuef is ", p_value_f)
    print("Standard Errorf is ", std_err_f)
    plt.scatter(ret, red,label='Rising Edge')
    plt.scatter(fet,fed, label = 'Falling Edge')
    plt.plot(ret, [intercept_r + slope_r * n for n in ret], 'b', label='fitted line(rising edge)')
    plt.plot(fet, [intercept_f + slope_f * n for n in fet], 'r', label='fitted line(falling edge)')
    plt.title(tit)
    plt.ylabel("Distance(m)")
    plt.xlabel("Time(ns)")
    plt.legend()
    #plt.show()
    plt.savefig(savename)
    plt.clf()

def grapher_of_old_data(ax, ay, px, py, wx, wy, tit, savename):
    plt.scatter(ax,ay, label ='In Air')
    slope, intercept, r_value, p_value, std_err = stats.linregress(ax,ay)
    print("In air")
    print("Slope is ", slope)
    print("Intercept is ", intercept)
    print("R value is ", r_value)
    print("P value is ", p_value)
    print("Standard Error is ", std_err)
    plt.plot(ax, [intercept + slope * n for n in ax], 'b', label='fitted line(air)')

    plt.scatter(px,py, label ='In Pyrex')
    slope, intercept, r_value, p_value, std_err = stats.linregress(px,py)
    print("In Pyrex")
    print("Slope is ", slope)
    print("Intercept is ", intercept)
    print("R value is ", r_value)
    print("P value is ", p_value)
    print("Standard Error is ", std_err)
    plt.plot(px, [intercept + slope * n for n in px], 'r', label='fitted line(pyrex)')

    plt.scatter(wx,wy, label ='In Water')
    slope, intercept, r_value, p_value, std_err = stats.linregress(wx,wy)
    print("In Water")
    print("Slope is ", slope)
    print("Intercept is ", intercept)
    print("R value is ", r_value)
    print("P value is ", p_value)
    print("Standard Error is ", std_err)
    plt.plot(wx, [intercept + slope * n for n in wx], 'g', label='fitted line(water)')
    plt.ylabel("Distance(m)")
    plt.xlabel("Time(ns)")
    plt.title(tit)
    plt.legend()
    #plt.show()
    plt.savefig(savename)
    plt.clf()


# For the better data do the following:
print("Better Data------------------------------------------")
rising_edge_dist = [1,2,3,4,5,6]
rising_edge_time = [0.6E-9, 4.4E-9, 7.3E-9, 10.6E-9,13.8E-9,17.6E-9]

falling_edge_dist = [1,2,3,4,5,6]
falling_edge_time = [3.5E-9, 3.6E-9, 7.3E-9, 10.6E-9, 13.6E-9, 17.6E-9]
print("In Air")
new_grapher(rising_edge_time, rising_edge_dist, falling_edge_dist, falling_edge_time,"LED λ = 632nm in Air", './inair.png')

rising_edge_dist = [4,5,5,6,6]
rising_edge_time = [7.6E-9, 3E-9, 4.6E-9, 16.5E-9, 17.8E-9]

falling_edge_dist = [4, 5, 5, 6, 6]
falling_edge_time = [12.8E-9, 12E-9, 13.5E-9, 12.6E-9, 16E-9,]
print("In Pyrex")

new_grapher(rising_edge_time, rising_edge_dist, falling_edge_dist, falling_edge_time,"LED λ = 632nm in Pyrex", './inpyrex.png')

rising_edge_dist = [4,5,6]
rising_edge_time = [12.6E-9,14.6E-9,20.2E-9]

falling_edge_dist = [4,5,6]
falling_edge_time = [15.6E-9, 17.1E-9, 22E-9]
print("In Water")

new_grapher(rising_edge_time, rising_edge_dist, falling_edge_dist, falling_edge_time,"LED λ = 632nm in Water", './inwater.png')

print("850 data------------------------------------------")

air_x = [11E-9, 12E-9, 12E-9, 11E-9,
     14.5E-9, 14.5E-9,
     18.5E-9, 17E-9, 19E-9, 18E-9, 17E-9, 18E-9,
     18E-9, 18.5E-9, 19E-9, 18E-9, 17E-9, 18E-9,
     19.5E-9, 19E-9, 19E-9, 19E-9, 20E-9, 19E-9,
     18.5E-9, 20E-9, 18E-9, 20E-9, 19E-9, 20E-9,
     19.5E-9, 19.5E-9, 20E-9, 20E-9, 20E-9, 21E-9,
     20E-9, 20E-9, 20E-9, 20E-9, 22E-9, 21E-9,22E-9, 21E-9, 20E-9, 21E-9, 20E-9, 21E-9, 21E-9, 21E-9] #rising edges

air_y = [3,3,3,3, 4,4, 5,5,5,5,5,5, 5.2,5.2,5.2,5.2,5.2,5.2,5.4,5.4,5.4,5.4,5.4,5.4, 5.6,5.6,5.6,5.6,5.6,5.6, 5.8,5.8,5.8,5.8,5.8,5.8, 6, 6,6,6,6,6,6,6,6,6,6,6,6,6,]

pyrex_x = [18E-9,19E-9,18E-9,18E-9,20E-9,20E-9,19E-9,19E-9,19E-9,19.5E-9,19.5E-9,20E-9,20E-9,20E-9,20E-9,20E-9,20E-9,21E-9,20E-9,21E-9,20E-9,20E-9,20E-9,20E-9,20E-9,22E-9,20E-9,22E-9,22E-9,20E-9,22E-9,23E-9,21E-9,20E-9,21E-9,21.5E-9,20.5E-9,22E-9,20E-9,20E-9,22E-9,22E-9,22E-9,22E-9,21E-9,21E-9,20E-9,21E-9,21E-9,21E-9] #rising edges

pyrex_y = [5,5,5,5,5,5,5,5,5,5,5,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,] # Meters
print("in air")
plt.scatter(air_x, air_y, label='In Air')
slope, intercept, r_value, p_value, std_err = stats.linregress(air_x,air_y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
plt.plot(air_x, [intercept + slope * n for n in air_x], 'b', label='fitted line(air)')
print("in pyrex")
plt.scatter(pyrex_x, pyrex_y, label='In Pyrex')
slope, intercept, r_value, p_value, std_err = stats.linregress(pyrex_x,pyrex_y)
print("Slope is ", slope)
print("Intercept is ", intercept)
print("R value is ", r_value)
print("P value is ", p_value)
print("Standard Error is ", std_err)
plt.plot(pyrex_x, [intercept + slope * n for n in pyrex_x], 'r', label='fitted line(pyrex)')

plt.ylabel("Distance(m)")
plt.xlabel("Time(ns)")
plt.title('LED λ = 850nm')
plt.legend()
#plt.show()
plt.savefig('./850old.png')
plt.clf()



air_y = [3,3,4,4,5,5,5,5,5,5,5,5,5,5,5.2,5.2,5.2,5.2,5.2,5.2,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.6,5.6,5.8,5.8,5.8,5.8,5.8,5.8,6,6,6,6,6,6,6,6,6,6,6,6,] # Meters
#51

air_x = [15E-9,10E-9,14E-9,13.5E-9,18E-9,17E-9,17E-9,19E-9,17.5E-9,17.5E-9,17.5E-9,17E-9,18E-9,17E-9,19E-9,18E-9,20E-9,19E-9,18E-9,19E-9,19E-9,18E-9,20E-9,18E-9,20E-9,20E-9,20E-9,20E-9,20E-9,20E-9,20E-9,18.5E-9,19E-9,21E-9,21E-9,21E-9,20E-9,20.5E-9,19.5E-9,20E-9,19E-9,20E-9,21E-9,20E-9,19E-9,19E-9,20E-9,20E-9,20E-9,20E-9,19.5E-9] #rising edges
#50


pyrex_y = [5,5,5,5,5,5,5,5,5,5,5,5,5,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,] # Meters
#51

pyrex_x = [18E-9,18E-9,18E-9,20E-9,18E-9,20E-9,20E-9,18E-9,20E-9,18E-9,18E-9,18E-9,18E-9,20E-9,20E-9,20E-9,18E-9,18E-9,22E-9,20E-9,21E-9,19E-9,20E-9,20E-9,20E-9,19.5E-9,22E-9,20E-9,22E-9,22E-9,20E-9,20E-9,22E-9,22E-9,21E-9,20E-9,21E-9,19.5E-9,19E-9,20E-9,20E-9,20E-9,22E-9,20E-9,22E-9,21E-9,21E-9,21E-9,22E-9,22E-9,21E-9,] #rising edges

water_y = [5,5,5,5,5,5,5,5,5,5,5,5,5,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.2,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,6,6,6,6,6,6,6,6,6,6,6,6,6,] # Meters
#51


water_x = [24E-9,22E-9,22E-9,22E-9,20E-9,
     22E-9,23E-9,22E-9,20E-9,22E-9,23E-9,
     21.5E-9,21.5E-9,
     22E-9,22E-9,24E-9,22E-9,
     23E-9,23E-9,23E-9,22E-9,21E-9,
     21.5E-9,22.5E-9,24.5E-9,24E-9,21E-9,
     24E-9,24E-9,22E-9,22E-9,
     22E-9,23E-9,23E-9,23E-9,
     22E-9,22.5E-9,23E-9,22E-9,23E-9,
     22E-9,24E-9,22E-9,24E-9,
     22.5E-9,24E-9,25E-9,27E-9,25E-9,23E-9,
     23E-9,24E-9,25.5E-9,25.5E-9,
     24E-9,26E-9,24E-9,24E-9,
     25E-9,25E-9,25E-9,26E-9,
     24.5E-9,24.5E-9,25E-9,25E-9,
     24E-9,28E-9,26E-9,26E-9,
     26E-9,25E-9,24E-9,24E-9,
     25E-9,24E-9,23E-9,24E-9,25E-9,] #rising edges
print("632 old------------------------------------------")
grapher_of_old_data(air_x,air_y,pyrex_x,pyrex_y,water_x,water_y,'LED λ = 632nm','./632old.png')



air_y = [3,3,4,4,4,4,5,5,5,5,5,5,5,5,5.2,5.2,5.2,5.2,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.8,5.8,5.8,5.8,6,6,6,6,] # Meters
#51

air_x = [11.5E-9,9.5E-9,14E-9,14E-9,14E-9,14E-9,17E-9,18E-9,18E-9,18E-9,17E-9,18E-9,18E-9,17E-9,19E-9,19E-9,19E-9,17E-9,19E-9,19E-9,18E-9,19E-9,20E-9,20E-9,20E-9,21E-9,20E-9,21E-9,21E-9,21E-9,21E-9,21E-9,21E-9,21E-9,] #rising edges
#50
pyrex_y = [5,5,5,5,5,5,5,5,5,5,5,5,5,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.6,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,5.8,] # Meters
#51

pyrex_x = [18E-9,18E-9,18E-9,20E-9,18E-9,20E-9,20E-9,18E-9,20E-9,18E-9,18E-9,18E-9,18E-9,20E-9,20E-9,20E-9,18E-9,18E-9,22E-9,20E-9,21E-9,19E-9,20E-9,20E-9,20E-9,19.5E-9,22E-9,20E-9,22E-9,22E-9,20E-9,20E-9,22E-9,22E-9,21E-9,20E-9,21E-9,19.5E-9,19E-9,20E-9,20E-9,20E-9,22E-9,20E-9,22E-9,21E-9,21E-9,21E-9,22E-9,22E-9,21E-9,] #rising edges

water_y = [5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,5.6,5.8,5.8,5.8,6,6,6,6,6,6,6,]
#51

water_x = [22E-9,22E-9,22E-9,24E-9,23E-9,24E-9,24E-9,24E-9,22E-9,23E-9,25E-9,25E-9,24E-9,26E-9,26E-9,24E-9,26E-9,24E-9,25E-9,23E-9,]
#50
print("465 old------------------------------------------")
grapher_of_old_data(air_x,air_y,pyrex_x,pyrex_y,water_x,water_y,'LED λ = 465nm','./465old.png')



print("In Air")
wavelength = 632
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
#plt.savefig("./inair.png")
plt.clf()

plt.plot(wavelength,slope, 'o')
plt.errorbar(wavelength,slope, yerr=[std_err], ecolor= 'green')
plt.axhline(y=2.99E8)
plt.ylabel("Speed Of Light")
plt.xlabel("Wavelength")
plt.savefig("perfect.png")
plt.clf()


wavelengths = [465, 632, 850]
slopes = [265885860.30,288406198.11,307101500.64]
std_err = [9518498.17, 21993744.10, 11512844.57]
plt.scatter(wavelengths,slopes)
plt.errorbar(wavelengths,slopes, yerr=[9518498.17, 21993744.10, 11512844.57], ls='none')
plt.axhline(y=2.99E8)
plt.ylabel("Speed Of Light")
plt.xlabel("Wavelength")
plt.savefig("perfect2.png")
plt.clf()


##############################################
dist = [4,5,6] #Change for different distances
time = [15.6E-9, 17.1E-9,22E-9,] # Change for times

delta_t = []
for i in range(len(time)):
    V_avg = dist[i] / time[i] #Average Velocity calculation
    print(V_avg)
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
plt.title("Change of time in Water to find speed of light in water")
plt.ylabel("Distance")
plt.xlabel("Time")
plt.legend()
#plt.show()
plt.savefig("./indexofr.png")
plt.clf()
