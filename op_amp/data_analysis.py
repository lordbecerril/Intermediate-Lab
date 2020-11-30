#11.92,1.28,4.3,1E6,90.3, 22.2E-3

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


df = pd.read_csv("data.csv") # Read data

print("frequency(Hz) is ")


print(df['frequency(Hz)'].values.tolist())
print("Vi(V) is ")
print(df['Vi(V)'].values.tolist())
print("Vo(V) is ")
print(df['Vo(V)'].values.tolist())
print("Phase(s) is ")
print(df['Phase(s)'].values.tolist())



g=[]
for i in range(len(df.index)):
    r = df.iloc[i,2]/df.iloc[i,1]
    g.append(r)
df['Gain']=g

dummy = np.divide(df['Gain'], df['frequency(Hz)'])
df['Log Gain']= np.log(dummy)

g=[]
for i in range(len(df.index)):
    r = df.iloc[i,5]
    d = math.atan(r)
    g.append(d)
df['True Phase Shift']=g

df['Log Frequency']= np.log(df['frequency(Hz)'])


print(df)

df = df.sort_values(['frequency(Hz)'])
print(df)

df.to_csv("DF.csv")



fig, axes = plt.subplots(nrows=2, ncols=1)
plt.subplots_adjust(wspace=0.5, hspace=0.5);
x = df.set_index('frequency(Hz)').rename_axis(None)
x['Log Gain'].plot(ax=axes[0], title='Gain', legend=True, linestyle=' ',marker=".")
x['Phase(s)'].plot(ax=axes[1], title='Phase', legend=True, linestyle=' ',marker=".")
plt.show()
plt.clf()


df.plot(kind='scatter',x='frequency(Hz)',y='Log Gain',color='red')
plt.show()
plt.clf()

df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
plt.show()
plt.clf()

df.plot(kind='line',x='frequency(Hz)',y='Phase(s)',color='red')
plt.show()
plt.clf()
