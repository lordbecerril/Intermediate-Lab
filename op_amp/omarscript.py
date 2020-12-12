#!/usr/bin/env python
# coding: utf-8

# In[5]:


# THESE LIBRARIES ARE NECESSARY FOR THINGS TO RUN
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


from scipy import stats

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NEXT WE HAVE WHERE WE INPUT OUR DATA. USING THE FOLLOWING LINES TO INPUT DATA TAKEN
# DO NOT DELETE THESE LINES

# F = [250.0, 430.0, 1425.0, x 2337.0, x 4300.0, 10140.0, x 13300.0, 10, 7.92, 9, 12.5, 15.08, 17, 25, 34.9, 43, 62.3, 21800, 18800, 15100] # it is now in order

F = [250.0, 430.0, 1425.0, 10140.0, 10, 7.92, 9, 12.5, 15.08, 17, 25, 34.9, 43, 62.3, 21800, 18800, 15100]
print(len(F))

# Vi = [0.47, 0.45, 2.5, x 3.45, x 2.5, 2.8, x 2.16, 10.4, 10.35, 10.4, 10.4, 10.35, 10.4, 10.4, 10.4, 10.2, 10.2, 0.75, 0.75,  ] # it is now in order
# print(len(Vi))

# Vo = [12.9, 7.8, 13.2, x 11.9, x 4.8, 2.7, x 0.43, 1, 1.75, 1.12, 0.8, 0.65, 0.55, 0.415, 0.315, 0.28, 0.200, 0.75, 0.93,] # it is now in order
# print(len(Vo))
# PH = [0.0009599999999999999, 0.00057, 0.000168, x 0.000109, x 5.9999999999999995e-05, 2.3e-05, x 1.95e-05, 0.025, 0.033, 0.028, 0.020, 0.025, 0.017, 0.0144, 0.0104, 0.0074, 0.0059, 0.000011, 0.0000126, ]
# print(len(PH))
# R1 = [10000, 10000, 10000, x 10000, x 10000, 10000, x 10000, 10000000,10000000, 10000000,10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 11.1, 11.1, ]
# print(len(R1))
# R2 = [90.3, 90.3, 90.3, x 90.3, x 90.3, 90.3, x 90.3, 90.3, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, ]
# print(len(R2))
# R3 = [98.5, 98.5, 98.5, x 98.5, x 98.5, 98.5, x 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5,  98.5, ]
# print(len(R3))

Vi = [0.47, 0.45, 2.5, 2.8, 10.4, 10.35, 10.4, 10.4, 10.35, 10.4, 10.4, 10.4, 10.2, 10.2, 0.75, 0.75,  ] # it is now in order
print(len(Vi))

Vo = [12.9, 7.8, 13.2, 2.7, 1, 1.75, 1.12, 0.8, 0.65, 0.55, 0.415, 0.315, 0.28, 0.200, 0.75, 0.93,] # it is now in order
print(len(Vo))

PH = [0.0009599999999999999, 0.00057, 0.000168, 2.3e-05, 0.025, 0.033, 0.028, 0.020, 0.025, 0.017, 0.0144, 0.0104, 0.0074, 0.0059, 0.000011, 0.0000126, ]

print(len(PH))

R1 = [10000, 10000, 10000,10000, 10000000,10000000, 10000000,10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 11.1, 11.1, ]
print(len(R1))
R2 = [90.3, 90.3, 90.3,  90.3, 90.3, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, ]
print(len(R2))
R3 = [98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5,  98.5, ]
print(len(R3))
# how did we calculate the phase shift from the difference in time?

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NOW WE MAKE A DATAFRAME WHICH IS EXACTLY WHAT IT SOUNDS LIKE. A FRAME OF DATA.
# DO NOT DELETE THESE LINES

df = pd.DataFrame(list(zip(F, Vi, Vo, PH, R1, R2, R3)), columns =['frequency(Hz)', 'Vi(V)', 'Vo(V)', 'Phase(s)', 'Resistance1', 'Resistance2', 'Resistance3' ]) #df IS THE NAME OF OUR DATAFRAME
# we have now named the columns so if we want to call on them this is what they are called now
# print(df) # TEST PRINT TO SEE THE DATAFRAME. NOTICE HOW IT IS A FRAME OF DATA\
# this prints out measurements that we had collected, our initial dataframe(df); frequencty, input voltage, output voltage, and phase shift

df['Total Resistance']= np.divide(df['Resistance2'], (np.add(df['Resistance1'], df['Resistance2'])))
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

df['Real Vi']= np.multiply(df['Vi(V)'], df['Total Resistance'])
print(" ")

df['Gain']= np.divide(df['Vo(V)'], df['Real Vi'])
print(" ")

df['Open Loop Gain']= np.divide(df['Gain'], df['frequency(Hz)'])

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# # NOW LET US CALCULATE GAIN. RECALL GAIN = Vo/Vi.
# # WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# GAIN = np.divide(df['Vo(V)'], df['Vi(V)'])# USING np.divide(array1, array2) we can divide every element
# df['Gain']= GAIN # WE CAN NOW ADD A NEW COLUMN TO OUR DATAFRAME JUST BY SAYING df["Whatever Name you want"]= some_array[]
# # print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG GAIN COLUMN WHEN WE PRINT IT OUT
# we have now included the column Gain to the df


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NOW LET US CALCULATE log(GAIN) = LOG(GAIN/FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# ok so this is the gain of the system but since the open loop op amp is very frequency dependent then to take out the frequency dependency we divide it by the frequency and we should get a gain that is only from the Vo/Vi

# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]

print('open loop ')

df['Log Gain']= np.log(np.divide(df['Gain'], df['frequency(Hz)']))
# print(" ")

df['OL Log Gain']= np.log(np.divide(df['Open Loop Gain'], df['frequency(Hz)']))
# print(" ")


# ok so i first converted frequency into time, so that way i know the time it takes for the whole wavelength to pass
df['1/f']= np.divide(1,df['frequency(Hz)'])

# i then only wanted half the time because peak to peak should only account for half of the wavelength if it has not been shifted and only inverted
df['half (1/f)']= np.divide(df['1/f'],2)

# i then know that the original shift should be half (1/f) therefore, i substract the phase shift that we did get from the original and i get the time difference from peak to upside down peak haha
df['time shift']= np.subtract(df['half (1/f)'],df['Phase(s)'])

df['Angle']= np.multiply(df['time shift'], (np.multiply(df['frequency(Hz)'],360)))



# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT


# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)
df2 = df # df2 is the open loop

# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
ax = df.plot(kind='scatter',x='Log Frequency',y='OL Log Gain',color='red')
plt.title('Log ($A_{OL}$) vs Log($\\nu$)')
ax.set_xlabel("Log($\\nu$)")
ax.set_ylabel("Log ($A_{OL}$)")
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='OL Log Gain',color='red')
plt.title('Log ($A_{OL}$) vs Log($\\nu$)')
ax.set_xlabel("Log($\\nu$)")
ax.set_ylabel("Log ($A_{OL}$)")
plt.show()
plt.clf()


# add this to your script for phi vs nu

df = df.sort_values(['Angle'])
print(df)



# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
ax = df.plot(kind='line',x='frequency(Hz)',y='Angle',color='red')
ax.set_xlim([-1000,20000])

plt.title('$\phi$ vs $\\nu$')

ax.set_xlabel("$\\nu$")
ax.set_ylabel("$\phi$")

plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
ax = df.plot(kind='scatter',x='frequency(Hz)',y='Angle',color='red')
ax.set_xlim([-1000,20000])

plt.title('$\phi$ vs $\\nu$')

ax.set_xlabel("$\\nu$")
ax.set_ylabel("$\phi$")


plt.show()
plt.clf()


# In[ ]:





# In[ ]:





# In[4]:


# THESE LIBRARIES ARE NECESSARY FOR THINGS TO RUN
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


from scipy import stats

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NEXT WE HAVE WHERE WE INPUT OUR DATA. USING THE FOLLOWING LINES TO INPUT DATA T/AKEN
# DO NOT DELETE THESE LINES



F = [50, 100, 200, 448, 703, 1000, 1300, 1700, 2000, 4000, 6060, 8000, 10000, 13000, 16000, 20040, 25200, 32890, 40600, 60600, 85800, 100600,  198000, ] # it is now in order
print(len(F))

Vi = [1.16, 1.1, 1.05, 1.02, 1.02, 1.02, 1.02, 1.02, 1.015, 1.015, 1.015, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.015, 1.01, 1.01, 1.01, 1.01, 0.97, ] # it is now in order
print(len(Vi))


Vo = [0.515 , 0.545, 0.505, 0.496, 0.49, 0.5, 0.5, 0.493, 0.490, 0.480, 0.472, 0.452, 0.436, 0.408, 0.380, 0.340, 0.288, 0.242, 0.204, 0.148, 0.108, 0.092, 0.045] # it is now in order
print(len(Vo))


# could the 10,000 actually be 1,000? we will see. no lol
R1 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, ]
print(len(R1))

R2 = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, ]
print(len(R2))

R3 = [98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, ]
print(len(R3))

Ra = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, ]
print(len(Ra))

Rb= [90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3]
print(len(Rb))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NOW WE MAKE A DATAFRAME WHICH IS EXACTLY WHAT IT SOUNDS LIKE. A FRAME OF DATA.
# DO NOT DELETE THESE LINES

df = pd.DataFrame(list(zip(F, Vi, Vo, R1, R2, R3, Ra, Rb)), columns =['frequency(Hz)', 'Vi(V)', 'Vo(V)', 'Resistance1', 'Resistance2', 'Resistance3', 'ResistanceA', 'ResistanceB' ]) #df IS THE NAME OF OUR DATAFRAME
# we have now named the columns so if we want to call on them this is what they are called now
# print(df) # TEST PRINT TO SEE THE DATAFRAME. NOTICE HOW IT IS A FRAME OF DATA\
# this prints out measurements that we had collected, our initial dataframe(df); frequencty, input voltage, output voltage, and phase shift

df['Total Resistance']= np.divide(df['Resistance2'], (np.add(df['Resistance1'], df['Resistance2'])))
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

df['Real Vi']= np.multiply(df['Vi(V)'], df['Total Resistance'])
print(" ")

df['A']= np.divide(df['Vo(V)'], df['Real Vi'])
print(" ")

df['Aol']= np.divide(df['A'],df['frequency(Hz)'])
print(" ")

df['RA/RB']= np.divide(df['ResistanceA'], df['ResistanceB'])
print(" ")

# df['Gain']= np.divide(df['RA/RB'], np.add(1, np.divide(np.add(1, (df['RA/RB'])),df['Aol']) ))
# print(" ")

df['Gain']= np.divide(df['RA/RB'], np.add(1, np.divide(np.add(1, (df['RA/RB'])),df['A']) ))
print(" ")




#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# # NOW LET US CALCULATE GAIN. RECALL GAIN = Vo/Vi.
# # WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# GAIN = np.divide(df['Vo(V)'], df['Vi(V)'])# USING np.divide(array1, array2) we can divide every element
# df['Gain']= GAIN # WE CAN NOW ADD A NEW COLUMN TO OUR DATAFRAME JUST BY SAYING df["Whatever Name you want"]= some_array[]
# # print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG GAIN COLUMN WHEN WE PRINT IT OUT
# we have now included the column Gain to the df


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NOW LET US CALCULATE log(GAIN) = LOG(GAIN/FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT


# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Gain']= np.log(df['Gain'])


# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])


# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)

# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
ax = df.plot(kind='scatter',x='Log Frequency',y='Log Gain',color='red')


plt.title('Log ($A_{CL}$) vs Log($\\nu$)')
ax.set_xlabel("Log($\\nu$)")
ax.set_ylabel("Log ($A_{CL}$)")

plt.show()
plt.clf()






# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
ax = df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')

plt.title('Log ($A_{CL}$) vs Log($\\nu$)')
ax.set_xlabel("Log($\\nu$)")
ax.set_ylabel("Log ($A_{CL}$)")

plt.show()
plt.clf()





ax = df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
df2.plot(ax=ax,kind='line',x='Log Frequency',y='OL Log Gain',color='blue')

plt.title('Gain vs Frequency')
ax.set_xlabel("Frequency")
ax.set_ylabel("Gain")
ax.legend(["Closed Loop","Open Loop" ])
plt.show()
plt.clf()




print("Closed Loop")


# In[ ]:





# In[ ]:





# In[3]:


# THESE LIBRARIES ARE NECESSARY FOR THINGS TO RUN
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


from scipy import stats

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NEXT WE HAVE WHERE WE INPUT OUR DATA. USING THE FOLLOWING LINES TO INPUT DATA TAKEN
# DO NOT DELETE THESE LINES

# Printing input voltages
Vi = [2.873, 2.797, 2.503, 2.204, 1.902, 1.599, 1.304, 1.001, 0.767, 0.506, 0.263, -2.205, -0.264, -0.504, -0.769, -1.0, -1.305, -1.598, -1.903, -2.503, -2.795, -2.87, -2.999, 2.997, 3.298, 3.608, -3.607, -3.918, -4.20, 4.20]

print(len(Vi))


# Printing output voltages
Vo = [-1.16, -1.14, -1.02, -0.88, -0.74, -0.62, -0.48, -0.34, -0.24, -0.12, -0.02, 01.10, 0.22, 0.34, 0.46, 0.56, 0.7, 0.82, 0.96, 1.23, 1.36, 1.36, 1.36, -1.16, -1.16, -1.16, 1.36, 1.36, 1.36, -1.16]

print(len(Vo))


R1 = [ 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
print(len(R1))

R2 = [ 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
print(len(R2))

R3 = [  98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5]
print(len(R3))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NOW WE MAKE A DATAFRAME WHICH IS EXACTLY WHAT IT SOUNDS LIKE. A FRAME OF DATA.
# DO NOT DELETE THESE LINES

df = pd.DataFrame(list(zip( Vi, Vo, R1, R2, R3)), columns =['Vi(V)', 'Vo(V)', 'Resistance1', 'Resistance2', 'Resistance3' ]) #df IS THE NAME OF OUR DATAFRAME
# we have now named the columns so if we want to call on them this is what they are called now
# print(df) # TEST PRINT TO SEE THE DATAFRAME. NOTICE HOW IT IS A FRAME OF DATA\
# this prints out measurements that we had collected, our initial dataframe(df); frequencty, input voltage, output voltage, and phase shift

df['Total Resistance']= np.divide(df['Resistance2'], (np.add(df['Resistance1'], df['Resistance2'])))
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

df['Real Vi']= np.multiply(df['Vi(V)'], df['Total Resistance'])
print(" ")

df['Gain']= np.divide(df['Vo(V)'], df['Real Vi'])
print(" ")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# # NOW LET US CALCULATE GAIN. RECALL GAIN = Vo/Vi.
# # WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# GAIN = np.divide(df['Vo(V)'], df['Vi(V)'])# USING np.divide(array1, array2) we can divide every element
# df['Gain']= GAIN # WE CAN NOW ADD A NEW COLUMN TO OUR DATAFRAME JUST BY SAYING df["Whatever Name you want"]= some_array[]
# # print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG GAIN COLUMN WHEN WE PRINT IT OUT
# we have now included the column Gain to the df


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Log Gain']= np.log(df['Gain'])
# print(" ")




# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
df = df.sort_values(['Vo(V)'])
print(df)



# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Real Vi',y='Vo(V)',color='red')
plt.title('V output vs V input')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Real Vi',y='Vo(V)',color='red')
plt.title('V output vs V input')
plt.show()
plt.clf()

print("Closed loop D.C.")
