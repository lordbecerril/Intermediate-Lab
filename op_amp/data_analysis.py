import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


df = pd.read_csv("data.csv") # Read data

g=[]
for i in range(len(df.index)):
    r = df.iloc[i,2]/df.iloc[i,1]
    g.append(r)
df['Gain']=g



df['Log Gain']= np.log(df['Gain'])

g=[]
for i in range(len(df.index)):
    r = df.iloc[i,5]/df.iloc[i,0]
    d = r * 360
    g.append(d)
df['True Phase Shift']=g

print(df)

df = df.sort_values(['frequency(Hz)'])
print(df)




fig, axes = plt.subplots(nrows=2, ncols=1)
plt.subplots_adjust(wspace=0.5, hspace=0.5);
x = df.set_index('frequency(Hz)').rename_axis(None)
x['Log Gain'].plot(ax=axes[0], title='Gain', legend=True, linestyle=' ',marker=".")
x['True Phase Shift'].plot(ax=axes[1], title='Phase', legend=True, linestyle=' ',marker=".")
plt.show()
plt.clf()


df.plot(kind='scatter',x='frequency(Hz)',y='Log Gain',color='red')
plt.show()
plt.clf()

df.plot(kind='line',x='frequency(Hz)',y='True Phase Shift',color='red')
plt.show()
plt.clf()
