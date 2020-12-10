#!/usr/bin/env python
# coding: utf-8
# THESE LIBRARIES ARE NECESSARY FOR THINGS TO RUN
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


from scipy import stats

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


F = [250.0, 430.0, 10, 7.92, 9, 12.5, 15.08, 17, 25, 34.9, 43, 62.3 ] # it is now in order
print(len(F))


Vi = [0.47, 0.45, 10.4, 10.35, 10.4, 10.4, 10.35, 10.4, 10.4, 10.4, 10.2  ] # it is now in order
print(len(Vi))

Vo = [12.9, 7.8, 1, 1.75, 1.12, 0.8, 0.65, 0.55, 0.415, 0.315, 0.28] # it is now in order
print(len(Vo))

PH = [0.0009599999999999999, 0.00057,  0.025, 0.033, 0.028, 0.020, 0.025, 0.017, 0.0144, 0.0104, 0.0074 ]
print(len(PH))
# 14 elements
# could the 10,000 actually be 1,000? we will see no lol
R1 = [10000, 10000,  10000000,10000000, 10000000,10000000, 10000000, 10000000, 10000000, 10000000, 10000000 ]
print(len(R1))

R2 = [90.3, 90.3,  90.3, 99, 99, 99, 99, 99, 99, 99, 99 ]
print(len(R2))

R3 = [98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5 ]
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

df['Gain']= np.divide(df['Vo(V)'], df['Total Resistance'])
print(" ")

#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:

# print(" ")

# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())


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
df['Log Gain']= np.log(np.divide(df['Gain'], df['frequency(Hz)']))
# print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

# omar put the following in

# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Ln Gain']= np.log(df['Gain'])
# # print(" ")
# # this cant be right since open loop gain is very frequency dependent
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT



df['Vi/frequency'] = np.divide(df['Vi(V)'], df['frequency(Hz)'])



# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT




# Omar put the following in

#  we are trying to find the resistance

# NOW LET US CALCULATE Total Resistance (RT)
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]


# NOW LET US CALCULATE Psuedo Gain
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Psuedo Gain']= np.divide(df['Gain'], (df['Total Resistance']))
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A PSUEDO GAIN COLUMN WHEN WE PRINT IT OUT


df['Psuedo Gain per frequency']= np.divide(df['Psuedo Gain'], (df['frequency(Hz)']))
print(" ")

df['log of Psuedo Gain per frequency'] = np.log(df['Psuedo Gain per frequency'])
print(" ")


df['Log Psuedo Gain']= np.log(df['Psuedo Gain'])
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A PSUEDO GAIN COLUMN WHEN WE PRINT IT OUT



df['Psuedo Gain frequency'] = np.divide(df['Psuedo Gain'], df['frequency(Hz)'])
print(" ")


df['Log Psuedo Gain per frequency']= np.divide(df['Log Psuedo Gain'],df['frequency(Hz)'])
print(" ")


# NOW LET US CALCULATE Psuedo Gain
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Psuedo Gain frequency']= np.log(df['Psuedo Gain frequency'])
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A Log PSUEDO GAIN COLUMN WHEN WE PRINT IT OUT




# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)






# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Log [(Vo/Vi)/frequency(Hz)](Log Gain)')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Log [(Vo/Vi)/frequency(Hz)] (Log Gain)')
plt.show()
plt.clf()


# add this to your script for phi vs nu

df['Angle'] = np.arctan(np.divide(df['frequency(Hz)'], df['Phase(s)']))
print(" ")

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
ax = df.plot(kind='line',x='frequency(Hz)',y='Angle',color='red')
ax.set_xlim([-1000,20000])

plt.title('angle vs frequency')
plt.show()
plt.clf()
# In[8]:


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

# F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

F = [250.0, 430.0, 1425.0, 2337.0, 4300.0, 10140.0, 13300.0, 10, 7.92, 9, 12.5, 15.08, 17, 25, 34.9, 43, 62.3, 21800, 18800, 15100, ] # it is now in order
print(len(F))

# Vi = [2.5, 2.5, 2.8, 2.16, 10.2, 3.45, 0.45, 0.47, 10.6, 10.6, 5.1, 10.6, 10.4, 10.6] #INPUT VOLTAGE IN VOLTS GOES HERE

Vi = [0.47, 0.45, 2.5, 3.45, 2.5, 2.8, 2.16, 10.4, 10.35, 10.4, 10.4, 10.35, 10.4, 10.4, 10.4, 10.2, 10.2, 0.75, 0.75,  ] # it is now in order
print(len(Vi))
# Vo = [13.2, 4.8, 2.7, 1.6, 3.4, 11.9, 7.8, 12.9, 2.5, 1.8, 10.2, 0.43, 0.68, 0.88] #OUTPUT VOLTAGE IN VOLTS GOES HERE

Vo = [12.9, 7.8, 13.2, 11.9, 4.8, 2.7, 0.43, 1, 1.75, 1.12, 0.8, 0.65, 0.55, 0.415, 0.315, 0.28, 0.200, 0.75, 0.93,] # it is now in order
print(len(Vo))
# PH = [0.000168, 5.9999999999999995e-05, 2.3e-05, 1.95e-05, 1.05e-05, 0.000109, 0.00057, 0.0009599999999999999, 7.8e-06, 5.400000000000001e-06, 0.0047, 1.24e-06, 1.82e-06, 2.85e-06]#PHASE SHIFT IN SECONDS GOES HERE

PH = [0.0009599999999999999, 0.00057, 0.000168, 0.000109, 5.9999999999999995e-05, 2.3e-05, 1.95e-05, 0.025, 0.033, 0.028, 0.020, 0.025, 0.017, 0.0144, 0.0104, 0.0074, 0.0059, 0.000011, 0.0000126, ]
# 0.025, 0.033 was the time shift,
print(len(PH))
# 14 elements
# could the 10,000 actually be 1,000? we will see no lol
R1 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000000,10000000, 10000000,10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 11.1, 11.1, ]
print(len(R1))
R2 = [90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 90.3, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, ]
print(len(R2))
R3 = [98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5,  98.5, ]
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

#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:

# print(" ")

# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())


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
df['Log Gain']= np.log(np.divide(df['Gain'], df['frequency(Hz)']))
# print(" ")

df['OL Log Gain']= np.log(np.divide(df['Open Loop Gain'], df['frequency(Hz)']))
# print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

# omar put the following in

# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Ln Gain']= np.log(df['Gain'])
# # print(" ")
# # this cant be right since open loop gain is very frequency dependent
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT



# df['Vi/frequency'] = np.divide(df['Vi(V)'], df['frequency(Hz)'])



# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT




# # Omar put the following in

# #  we are trying to find the resistance

# # NOW LET US CALCULATE Total Resistance (RT)
# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]


# # NOW LET US CALCULATE Psuedo Gain
# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Psuedo Gain']= np.divide(df['Gain'], (df['Total Resistance']))
# print(" ")
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A PSUEDO GAIN COLUMN WHEN WE PRINT IT OUT


# df['Psuedo Gain per frequency']= np.divide(df['Psuedo Gain'], (df['frequency(Hz)']))
# print(" ")

# df['log of Psuedo Gain per frequency'] = np.log(df['Psuedo Gain per frequency'])
# print(" ")


# df['Log Psuedo Gain']= np.log(df['Psuedo Gain'])
# print(" ")
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A PSUEDO GAIN COLUMN WHEN WE PRINT IT OUT



# df['Psuedo Gain frequency'] = np.divide(df['Psuedo Gain'], df['frequency(Hz)'])
# print(" ")


# df['Log Psuedo Gain per frequency']= np.divide(df['Log Psuedo Gain'],df['frequency(Hz)'])
# print(" ")


# # NOW LET US CALCULATE Psuedo Gain
# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Log Psuedo Gain frequency']= np.log(df['Psuedo Gain frequency'])
# print(" ")
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A Log PSUEDO GAIN COLUMN WHEN WE PRINT IT OUT




# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)






# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Log Frequency',y='OL Log Gain',color='red')
plt.title('Log Frequency vs Open loop Log (Gain)')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='OL Log Gain',color='red')
plt.title('Log Frequency vs Open Loop Log(Gain)')
plt.show()
plt.clf()



df.plot(kind='scatter',x='Phase(s)',y='Open Loop Gain',color='red')
plt.title('Frequency vs Open loop Gain')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Phase(s)',y='Open Loop Gain',color='red')
plt.title('Frequency vs Open Loop Gain')
plt.show()
plt.clf()





# add this to your script for phi vs nu

df['Angle'] = np.arctan(np.divide(df['frequency(Hz)'], df['Phase(s)']))
print(" ")

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
ax = df.plot(kind='line',x='frequency(Hz)',y='Angle',color='red')
ax.set_xlim([-1000,20000])

plt.title('angle vs frequency')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
ax = df.plot(kind='scatter',x='frequency(Hz)',y='Angle',color='red')
ax.set_xlim([-1000,20000])

plt.title('angle vs frequency')
plt.show()
plt.clf()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




things to do,

lets find the peak gain with resistors 10,000, 90.3, and 98.5
we still have to find the knee, we have gotten to frequency 186,000 so lets keep going faster until i guess it starts to rail
why did we need the phase shift? lets figure this out too

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




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

# F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

F = [50, 100, 200, 448, 703, 1000, 1300, 1700, 2000, 4000, 6060, 8000, 10000, 13000, 16000, 20040, 25200, 32890, 40600, 60600, 85800, 100600,  198000, ] # it is now in order
print(len(F))

Vi = [1.16, 1.1, 1.05, 1.02, 1.02, 1.02, 1.02, 1.02, 1.015, 1.015, 1.015, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.015, 1.01, 1.01, 1.01, 1.01, 0.97, ] # it is now in order
print(len(Vi))


Vo = [0.515, 0.545, 0.505, 0.496, 0.49, 0.5, 0.5, 0.493, 0.490, 0.480, 0.472, 0.452, 0.436, 0.408, 0.380, 0.340, 0.288, 0.242, 0.204, 0.148, 0.108, 0.092, 0.045] # it is now in order
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

df = pd.DataFrame(list(zip(F, Vi, Vo, R1, R2, R3)), columns =['frequency(Hz)', 'Vi(V)', 'Vo(V)', 'Resistance1', 'Resistance2', 'Resistance3' ]) #df IS THE NAME OF OUR DATAFRAME
# we have now named the columns so if we want to call on them this is what they are called now
# print(df) # TEST PRINT TO SEE THE DATAFRAME. NOTICE HOW IT IS A FRAME OF DATA\
# this prints out measurements that we had collected, our initial dataframe(df); frequencty, input voltage, output voltage, and phase shift

df['Total Resistance']= np.divide(df['Resistance2'], (np.add(df['Resistance1'], df['Resistance2'])))
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

df['Gain']= np.multiply(df['Vo(V)'], df['Total Resistance'])
print(" ")

#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:

# print(" ")

# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())


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
df['Log Gain']= np.log(df['Gain'])
# print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

# omar put the following in

# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Ln Gain']= np.log(df['Gain'])
# # print(" ")
# # this cant be right since open loop gain is very frequency dependent
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT


df['Ratio Vo/Vi'] = np.divide( df['Vo(V)'], df['Gain'])
print(" ")




# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT






# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)






# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Log [(Vo/Vi)/frequency(Hz)](Log Gain)')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Log [(Vo/Vi)/frequency(Hz)] (Log Gain)')
plt.show()
plt.clf()












# In[2]:


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

# F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

F = [50, 100, 200, 448, 703, 1000, 1300, 1700, 2000, 4000, 6060, 8000, 10000, 13000, 16000, 20040, 25200, 32890, 40600, 60600, 85800, 100600,  198000, ] # it is now in order
print(len(F))

Vi = [1.16, 1.1, 1.05, 1.02, 1.02, 1.02, 1.02, 1.02, 1.015, 1.015, 1.015, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.015, 1.01, 1.01, 1.01, 1.01, 0.97, ] # it is now in order
print(len(Vi))


Vo = [0.515, 0.545, 0.505, 0.496, 0.49, 0.5, 0.5, 0.493, 0.490, 0.480, 0.472, 0.452, 0.436, 0.408, 0.380, 0.340, 0.288, 0.242, 0.204, 0.148, 0.108, 0.092, 0.045] # it is now in order
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

df = pd.DataFrame(list(zip(F, Vi, Vo, R1, R2, R3)), columns =['frequency(Hz)', 'Vi(V)', 'Vo(V)', 'Resistance1', 'Resistance2', 'Resistance3' ]) #df IS THE NAME OF OUR DATAFRAME
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

#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:

# print(" ")

# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())


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
# print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT






# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT






# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)






# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Log [(Vo/Vi)/frequency(Hz)](Log Gain)')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Log [(Vo/Vi)/frequency(Hz)] (Log Gain)')
plt.show()
plt.clf()












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

# NEXT WE HAVE WHERE WE INPUT OUR DATA. USING THE FOLLOWING LINES TO INPUT DATA T/AKEN
# DO NOT DELETE THESE LINES

# F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

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



#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:

# print(" ")

# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())


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
# print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT






# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT






# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['frequency(Hz)'])
print(df)






# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Closed loop Log Gain')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
plt.title('Log Frequency vs Closed loop Log Gain')
plt.show()
plt.clf()








print("If i assume that i did mess up the prob and it was set to 10x and if we were reading the output incorrectly by dividing it by 2 then we would get a closed loop gain of 51, still not the 110 that is expected. but the voltage output is still not close to the being saturated so there is still room for improvement, potentially. i will say though if we did not have to half the output then we probably didnt have to half the input thus this would reduce us back down to 33 gain")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




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

# F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

# Vi = [2.873, -2.870, -.264, 0.263, 0.506, -0.504, -.769, 0.767, 1.001, -1.000, -1.305, 1.304, 1.599, -1.598,  -1.903, 1.902, 2.204, -2.202, -2.503, 2.503, 2.797, -2.795, ]  # it is now in order

# Printing input voltages
Vi = [2.873, 2.797, 2.503, 2.204, 1.902, 1.599, 1.304, 1.001, 0.767, 0.506, 0.263, -2.205, -0.264, -0.504, -0.769, -1.0, -1.305, -1.598, -1.903, -2.503, -2.795, -2.87, -2.999, 2.997, 3.298, 3.608, -3.607, -3.918, -4.20, 4.20, 0]
print(len(Vi))


# Printing output voltages
Vo = [-1.16, -1.14, -1.02, -0.88, -0.74, -0.62, -0.48, -0.34, -0.24, -0.12, -0.02, 01.10, 0.22, 0.34, 0.46, 0.56, 0.7, 0.82, 0.96, 1.23, 1.36, 1.36, 1.36, -1.16, -1.16, -1.16, 1.36, 1.36, 1.36, -1.16, 0]

#  Printing Real Vin
# [-0.10449499545040945, -0.10269335759781618, -0.0918835304822566, -0.07927206551410373, -0.06666060054595087, -0.055850773430391264, -0.0432393084622384, -0.030627843494085535, -0.0216196542311192, -0.0108098271155596, -0.0018016378525932666, 0.0081073703366697, 0.019818016378525934, 0.030627843494085535, 0.041437670609645136, 0.05044585987261147, 0.06305732484076433, 0.07386715195632393, 0.0864786169244768, 0.1108007279344859, 0.12251137397634214, 0.1243130118289354]


# Vo = [-1.16, 1.38, 0.220, -0.020, -0.120, 0.340, 0.460, -0.240, -0.340, 0.560, 0.700, -0.480, -0.620, 0.820, 0.960, -0.740, -0.880, 0.090, 1.23, -1.02, -1.14, 1.36, ] # it is now in order
print(len(Vo))


# could the 10,000 actually be 1,000? we will see no lol
R1 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
print(len(R1))
R2 = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
print(len(R2))
R3 = [ 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5]
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

df['Gain']= np.multiply(df['Vo(V)'], df['Total Resistance'])
print(" ")

#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:

# print(" ")

# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())


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
# df['Log Gain']= np.log(df['Gain'])
# print(" ")

# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

# omar put the following in

# # AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Ln Gain']= np.log(df['Gain'])
# # print(" ")
# # this cant be right since open loop gain is very frequency dependent
# # print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT







# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
# df['Log Frequency']= np.log(df['frequency(Hz)'])
# print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT






# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['Vo(V)'])
print(df)






# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

print(" ")
print("Printing input voltages")
print(df['Vi(V)'].values.tolist())

print(" ")
print("Printing output voltages")
print(df['Vo(V)'].values.tolist())

print(" ")
print(" Printing Real Vin")
print(df['Gain'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Vi(V)',y='Gain',color='red')
plt.title('')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Vi(V)',y='Gain',color='red')
plt.title('')
plt.show()
plt.clf()

# left hand side voltage setting is at 14.38
# right hand side voltage setting is at 14.51


















# In[ ]:





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

# F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

# Vi = [2.873, -2.870, -.264, 0.263, 0.506, -0.504, -.769, 0.767, 1.001, -1.000, -1.305, 1.304, 1.599, -1.598,  -1.903, 1.902, 2.204, -2.202, -2.503, 2.503, 2.797, -2.795, ]  # it is now in order

# Printing input voltages
Vi = [2.873, 2.797, 2.503, 2.204, 1.902, 1.599, 1.304, 1.001, 0.767, 0.506, 0.263, -2.205, -0.264, -0.504, -0.769, -1.0, -1.305, -1.598, -1.903, -2.503, -2.795, -2.87, -2.999, 2.997, 3.298, 3.608, -3.607, -3.918, -4.20, 4.20]
print(len(Vi))


# Printing output voltages
Vo = [-1.16, -1.14, -1.02, -0.88, -0.74, -0.62, -0.48, -0.34, -0.24, -0.12, -0.02, 01.10, 0.22, 0.34, 0.46, 0.56, 0.7, 0.82, 0.96, 1.23, 1.36, 1.36, 1.36, -1.16, -1.16, -1.16, 1.36, 1.36, 1.36, -1.16]

#  Printing Real Vin
# [-0.10449499545040945, -0.10269335759781618, -0.0918835304822566, -0.07927206551410373, -0.06666060054595087, -0.055850773430391264, -0.0432393084622384, -0.030627843494085535, -0.0216196542311192, -0.0108098271155596, -0.0018016378525932666, 0.0081073703366697, 0.019818016378525934, 0.030627843494085535, 0.041437670609645136, 0.05044585987261147, 0.06305732484076433, 0.07386715195632393, 0.0864786169244768, 0.1108007279344859, 0.12251137397634214, 0.1243130118289354]


# Vo = [-1.16, 1.38, 0.220, -0.020, -0.120, 0.340, 0.460, -0.240, -0.340, 0.560, 0.700, -0.480, -0.620, 0.820, 0.960, -0.740, -0.880, 0.090, 1.23, -1.02, -1.14, 1.36, ] # it is now in order
print(len(Vo))


# could the 10,000 actually be 1,000? we will see no lol
R1 = [ 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
print(len(R1))
R2 = [ 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
print(len(R2))
R3 = [  98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5, 98.5]
print(len(R3))

df = pd.DataFrame(list(zip( Vi, Vo, R1, R2, R3)), columns =['Vi(V)', 'Vo(V)', 'Resistance1', 'Resistance2', 'Resistance3' ]) #df IS THE NAME OF OUR DATAFRAME

df['Total Resistance']= np.divide(df['Resistance2'], (np.add(df['Resistance1'], df['Resistance2'])))
print(" ")
# print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

df['Real Vi']= np.multiply(df['Vi(V)'], df['Total Resistance'])
print(" ")

df['Gain']= np.divide(df['Vo(V)'], df['Real Vi'])
print(" ")






# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
# by sort we mean were ordering the frequencies from lowest to longest
df = df.sort_values(['Vo(V)'])
print(df)




# Omar put the following in

# when these are printed these will now be in order

# print(" ")
# print("Printing frequencies")
# print(df['frequency(Hz)'].values.tolist())

# print(" ")
# print("Printing input voltages")
# print(df['Vi(V)'].values.tolist())

# print(" ")
# print("Printing output voltages")
# print(df['Vo(V)'].values.tolist())

# print(" ")
# print(" Printing Real Vin")
# print(df['Gain'].values.tolist())

# print(" ")
# print("Printing phases")
# print(df['Phase(s)'].values.tolist())








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

print("Left hand side voltage setting is at 14.38,  right hand side voltage setting is at 14.51")
print("I am confused, if the op-amp becomes saturated near the operational voltages , 15 volts, then why is it railing at an input voltage of 0.259 and an output of 1.16 volts.")
print("If we assume that the prob was on 10x then we would multiply the V output by 10, now we end up around 44 gain, i thought we were only supposed to read half the voltage but if we double the output voltage then that gets us to 88 gain, close to what the gain should be for our closed loop op-amp, the only thing is that if we do these things then the Voutput gets to be around 23 volts, i am then confused as to why it was able to go this high without railing if our operational voltage for the op-amp was about 14 volts")
















# In[ ]:





# In[ ]:





# In[ ]:
