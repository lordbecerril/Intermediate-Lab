# THESE LIBRARIES ARE NECESSARY FOR THINGS TO RUN
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy.optimize import curve_fit

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NEXT WE HAVE WHERE WE INPUT OUR DATA. USING THE FOLLOWING LINES TO INPUT DATA TAKEN
# DO NOT DELETE THESE LINES

F = [1425.0, 4300.0, 10140.0, 13300.0, 24100.0, 2337.0, 430.0, 250.0, 33000.0, 42700.0, 39.0, 186000.0, 130000.0, 86000.0] #ADD ALL FREQUENCY DATA IN HERTZ HERE... NOT KHz, NOT mHz, STR8 UP Hz

Vi = [2.5, 2.5, 2.8, 2.16, 10.2, 3.45, 0.45, 0.47, 10.6, 10.6, 5.1, 10.6, 10.4, 10.6] #INPUT VOLTAGE IN VOLTS GOES HERE

Vo = [13.2, 4.8, 2.7, 1.6, 3.4, 11.9, 7.8, 12.9, 2.5, 1.8, 10.2, 0.43, 0.68, 0.88] #OUTPUT VOLTAGE IN VOLTS GOES HERE

PH = [0.000168, 5.9999999999999995e-05, 2.3e-05, 1.95e-05, 1.05e-05, 0.000109, 0.00057, 0.0009599999999999999, 7.8e-06, 5.400000000000001e-06, 0.0047, 1.24e-06, 1.82e-06, 2.85e-06]#PHASE SHIFT IN SECONDS GOES HERE

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NOW WE MAKE A DATAFRAME WHICH IS EXACTLY WHAT IT SOUNDS LIKE. A FRAME OF DATA.
# DO NOT DELETE THESE LINES

df = pd.DataFrame(list(zip(F, Vi, Vo, PH)), columns =['frequency(Hz)', 'Vi(V)', 'Vo(V)', 'Phase(s)']) #df IS THE NAME OF OUR DATAFRAME
print(df) # TEST PRINT TO SEE THE DATAFRAME. NOTICE HOW IT IS A FRAME OF DATA\

#IF YOU JUST WANT TO PRINT OUT A COLUMN USE THE FOLLOWING LINE:
print(" ")
print("Printing input voltages")
print(df['Vi(V)'].values.tolist())



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# NOW LET US CALCULATE GAIN. RECALL GAIN = Vo/Vi.
# WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
GAIN = np.divide(df['Vo(V)'], df['Vi(V)'])# USING np.divide(array1, array2) we can divide every element
df['Gain']= GAIN # WE CAN NOW ADD A NEW COLUMN TO OUR DATAFRAME JUST BY SAYING df["Whatever Name you want"]= some_array[]
print(" ")

print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG GAIN COLUMN WHEN WE PRINT IT OUT


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NOW LET US CALCULATE log(GAIN) = LOG(GAIN/FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Gain']= np.log(np.divide(df['Gain'], df['frequency(Hz)']))
print(" ")

print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT



# NOW LET US CALCULATE log(FREQUENCY) <-------- SAW THIS ON THE BOARD SO I DONT KNOW IF IT IS RIGHT
# AGAIN, WE CAN USE NUMPY TO DO THIS QUICKLY AS HELL. WE CAN ACCESS A WHOLE COLUMN BY CALLING df["Column Name"]
df['Log Frequency']= np.log(df['frequency(Hz)'])
print(" ")

print(df) #NOTICE NOW HOW THE DATAFRAME HAS A LOG_FREAK COLUMN WHEN WE PRINT IT OUT

# SORTED THE VALUES BECAUSE IT MAKES MORE SENSE
df = df.sort_values(['frequency(Hz)'])
print(df)

# PLOTTING IS ALSO WAY EASIER, ALL YOU GOTTA DO IS SET X AXIS TO A COLUMN NAME, AND Y TO COLUMN NAME AND THEN BAM. DONE
df.plot(kind='scatter',x='Log Frequency',y='Log Gain',color='red')
plt.show()
plt.clf()

# FOR kind = '' you can pick whether you want a line plot or a scatter plot as seen below
df.plot(kind='line',x='Log Frequency',y='Log Gain',color='red')
plt.show()
plt.clf()



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
