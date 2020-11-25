# Constant current
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


N = 130

df = pd.read_csv("4.csv") # Read data

#Getting Current for the Helmholtz Coils V=IR => I=V/R
cur = []
for i in range(len(df.index)):
    r = df.iloc[i,4]/df.iloc[i,5]
    cur.append(r)
df['Current (A)']=cur

# Getting the radius
rad = []
for i in range(len(df.index)):
    r = 16E-2
    rad.append(r)
df['Radius of Solenoids (m)'] = rad

#Averaging the left and right radius
ave = []
for i in range(len(df.index)):
    a = (df.iloc[i,6] + df.iloc[i,7])/2
    ave.append(a**-2)
df['Average Radius of beam (cm)'] = ave

#Calculating Magnetic field
mag_f = []
for i in range(len(df.index)):
    a = 4 * math.pi * 10**(-7) #𝜇
    a = a * 0.16**2 #𝜇𝑅^2
    a = a * N * df.iloc[i,8] #𝜇𝑅^2𝑁𝐼
    b = 0.16**2 + (0.16/2)**2 #
    b = b**(3/2)
    a = a/b
    mag_f.append(a)
df['Magnetic Field'] = mag_f

# Calculating e/m
ratio = []
for i in range(len(df.index)):
    a = (2 * df.iloc[i,2])/( (df.iloc[i,10])**2  *   (df.iloc[i,11])**2)
    ratio.append(a)
df['e/m'] = ratio


df.to_csv('DF.csv')

print(df)

x = []
for i in range(len(df.index)):
    a = df.iloc[i,2]
    x.append(a)

y = []
for i in range(len(df.index)):
    a = df.iloc[i,10]**2
    y.append(a)



m,b = np.polyfit(x, y, 1)
print(m)
print(b)

p, res, _, _, _ = np.polyfit(x, y, 1, full=True)
print(p)
print(res)


print(len(x))

slopes = []
for i in range(len(x)):
    slopes.append( m*x[i] + b)

plt.xlabel("Accelerating Voltage")
plt.ylabel("Radius Squared")
error = [1E-3,1E-3,1E-3,1E-3,1E-3,1E-3,]

plt.title("Radius Square as a function of V (A=1.11A$\pm$0.01A)")
plt.xlabel("Accelerating Voltage (B)")
plt.ylabel("Radius Squared (r^2)")
plt.plot(x, slopes)
plt.scatter(x, y)
plt.errorbar(x,y,yerr=error,ls='none')
#plt.errorbar(x,y,yerr=np.power(error,2),ls='none')
plt.show()
