import pandas as pd
import numpy as np

df = pd.read_csv("data.csv") # Read data


# Calculate Resistance
res =[]
for i in range(len(df.index)):
    r = df.iloc[i,0]/df.iloc[i,1]
    res.append(r)
df['Resistance (Ω)']=res


# Calculate power below with P = I^2*R
power = []
for i in range(len(df.index)):
    x = (df.iloc[i,1])**2  * (df.iloc[i,2])
    power.append( x)

# Append power to Dataframe
df['Power'] = power
#print(df)


ratio = 1.68E-9 # The ratio of len over area from R = RHO * (len/Cross sectional Area)

resistivity = []
for i in range(len(df.index)):
    x = df.iloc[i,2] * ratio
    resistivity.append(x)

df['Resistivity'] = resistivity
#print(df)

# Using RHOt = RHOo[2 + a(T-To)] solve for T and plug in calced resistivites
# Source https://www.askiitians.com/iit-jee-electric-current/temperature-dependence-of-resistivity/#temperature-dependence-of-resistivity
temperature = []
for i in range(len(df.index)):
    T = df.iloc[i,4] / (5.64E-8)
    T = T-1
    T = T / 0.0045
    T = T + 26.85
    T = T+273.15
    temperature.append(T)
#print(temperature)
df['Temperature'] = temperature


print(df)


f= open("for_omar.txt","w+")
dummy = "Voltage:" + df['Voltage(V)'].to_string(index=False)
f.write(dummy)
