import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * x**b

df = pd.read_csv("data.csv") # Read data

# Calculating Current I = (Voltage Drop Across Resistor)/(Resistor Resistance)
cur = []
for i in range(len(df.index)):
    r = df.iloc[i,1]/df.iloc[i,2]
    cur.append(r)
df['Current (A)']=cur


# Calculate Resistance R = V/I
res =[]
for i in range(len(df.index)):
    r = df.iloc[i,0]/df.iloc[i,3]
    res.append(r)
df['Resistance (Ω)']=res


# Calculate power below with P = I^2*R
power = []
for i in range(len(df.index)):
    x = (df.iloc[i,3])**2  * (df.iloc[i,4])
    power.append( x)
# Append power to Dataframe
df['Power(Watts)'] = power

#ratio = 1.68E-9 # The ratio of len over area from R = RHO * (len/Cross sectional Area)
ratio = 1.68E8 #1/m unit

# Calculating Resistivities with RHO = R/ratio
resistivity = []
for i in range(len(df.index)):
    x = df.iloc[i,4] / ratio
    resistivity.append(x)
df['Resistivity (Ωm)'] = resistivity


# Using RHOt = RHOo[2 + a(T-To)] solve for T and plug in calced resistivites
# Source https://www.askiitians.com/iit-jee-electric-current/temperature-dependence-of-resistivity/#temperature-dependence-of-resistivity
temperature = []
for i in range(len(df.index)):
    T = df.iloc[i,6] / (5.64E-8)
    T = T-1
    T = T / 0.0045
    T = T + 26.85
    T = T + 273.15
    temperature.append(T)
#print(temperature)
df['Temperature(K)'] = temperature

res_in_mocm = []
for i in range(len(df.index)):
    m = df.iloc[i,6] * 1E8
    res_in_mocm.append(m)
df['Resistivity in μΩcm'] = res_in_mocm



########################################################################## PLOTTING SHIT
#Book data shti
df2 = pd.read_csv("bookdata.csv") # Read data
#print(df2)
fig, ax = subplots()
ax = df2.plot(x = 'Temperature(K)', y = 'Resistivity(μΩcm)')
#ax.legend(["$a_j$ = 3.20336","$a_j$ = 4.20336", "$a_j$ = 5.20336", "$a_j$ = 6.20336","$a_j$ = 7.20336","$a_j$ = 8.20336"],bbox_to_anchor=(1.05, 1))#title='Jupiter Inclinations'
ax.set_xlabel("Temperature(K)")
ax.set_ylabel("Resistivity(μΩcm)")
plt.tight_layout()
#plt.show()
plt.clf()

########################################################################## PLOTTING SHIT
# Our very own data shit
fig, ax = subplots()
ax = df.plot(x = 'Power(Watts)', y = 'Resistivity (Ωm)')
#ax.legend(["$a_j$ = 3.20336","$a_j$ = 4.20336", "$a_j$ = 5.20336", "$a_j$ = 6.20336","$a_j$ = 7.20336","$a_j$ = 8.20336"],bbox_to_anchor=(1.05, 1))#title='Jupiter Inclinations'
ax.set_xlabel("Power(Watts)")
ax.set_ylabel("Resistivity (Ωm)")
plt.tight_layout()
#plt.show()
plt.clf()
##########################################################################
#FITTING TIME
temps = [500, 600, 700, 800, 900, 1000, 1050, 1075, 1200, 1250,1300,1350, 1450, 1475, 1500, 1550, 1575,1600, 1650, 1700, 1725,1750,1775,1800,]
##########################################################################

# Using readlines()
file1 = open('thing.txt', 'r')
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
    m = df.iloc[i,5]
    power.append(m)
print(power)
print(len(power))
power = np.array(power)

p0 =[4.14E-27, 4]
popt, pcov = curve_fit(func, temps, power,maxfev=1000)
print(popt)
print(pcov)
plt.scatter(temps, power)
plt.plot(temps, func(temps, popt[0],popt[1]), label="Fitted Curve", color ='r')
plt.xlabel('Temperature(K)')
plt.ylabel('Power(Watts)')
plt.legend()
plt.show()

# Save to a CSV file
df.to_csv('DF.csv')

print(df)
