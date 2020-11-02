import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit

def func(x, a, b,c,d,e,f):
    return a * b * (c**-5) * np.exp((-1*d*e) / (c*f*x))


def blue_mercury(x,a,b):
    return a * b * (435E-9**-5) * np.exp((-1*6.626E-34*2.99E9) / (435E-9*1.38E-23*x))

def red_mercury(x,a,b,c):
    return a * b * (656E-9**-5) * np.exp((-1*c*2.99E9) / (656E-9*1.38E-23*x))

def red_mercury2(x,a,b):
    return a * 12.48 * (656E-9**-5) * np.exp((-1*b*2.99E9) / (656E-9*1.38E-23*x))


def func3(x, a, b,c,d):
    return a + np.log(b*c*656-5)- ((d*2.99E9)/(656E-5*1.38E-23*x))



df = pd.read_csv("lambdaequal656.csv") # Read data

cur = []
for i in range(len(df.index)):
    r = df.iloc[i,1]/6.5
    cur.append(r)
df['Current (A)']=cur

res =[]
for i in range(len(df.index)):
    r = df.iloc[i,0]/df.iloc[i,3]
    res.append(r)
df['Resistance (Ω)'] = res

# Calculate power below with P = I^2*R
power = []
for i in range(len(df.index)):
    x = (df.iloc[i,3])**2  * (df.iloc[i,4])
    power.append( x)
# Append power to Dataframe
df['Power(Watts)'] = power


ratio = 1.68E8 #1/m unit
# Calculating Resistivities with RHO = R/ratio
resistivity = []
for i in range(len(df.index)):
    x = df.iloc[i,4] / ratio
    x = x*1E8
    resistivity.append(x)
df['Resistivity (μΩcm)'] = resistivity

df.to_csv('stuff.csv')



# Using readlines() -----------------------
file1 = open('thing3forred.txt', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
temps = []
for line in Lines:
    temps.append(int(line))
print(temps)
print(len(temps))
temps = np.array(temps)



power = []
for i in range(len(df.index)):
    m = df.iloc[i,2]
    power.append(m)
print(power)
print(len(power))
power = np.array(power)

'''
p0 =[4.30739944e-13,4.30739944e-13, 435E-9, 6.626E-34, 2.99E8,1.38E-23]
popt, pcov = curve_fit(func, temps, power, maxfev=1000)
print(popt)
print(pcov)
print('r(λ)=', popt[0])
print('ε(λ;T)=', popt[1])
print('λ=', popt[2])
print('h=', popt[3])
print('c=', popt[4])
print('kB=', popt[5])

plt.scatter(temps, power)
plt.plot(temps, func(temps, popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('Power(Watts)')
plt.legend()
plt.show()
plt.clf()
'''
#Blue Mercury is 435 nm
p0 =[4.30739944e-13,12.48,6.626E-34]
popt, pcov = curve_fit(red_mercury, temps, power, maxfev=1000)
print(popt)
print(pcov)
print('r(λ)=', popt[0])
print('ε(λ;T)=', popt[1])
print('h=', popt[2])
plt.scatter(temps, power)
plt.plot(temps, red_mercury(temps, popt[0],popt[1],popt[2]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('Power(Watts)')
plt.legend()
plt.show()
plt.clf()


#Blue Mercury is 435 nm
p0 =[4.30739944e-13,6.626E-34]
popt, pcov = curve_fit(func3, temps, np.log(power), maxfev=1000)
print(popt)
print(pcov)
print('constant=', popt[0])
print('r=', popt[1])
print('epsilon=', popt[2])
print('h=', popt[3])
plt.scatter(temps, np.log(power))
plt.plot(temps, func3(temps, popt[0],popt[1],popt[2],popt[3]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('Power(Watts)')
plt.legend()
plt.show()
plt.clf()




#Red Hydrogen 656 nm
print(df)
