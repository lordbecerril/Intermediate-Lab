Volt1 = [22.81, 24.24, 25.48, 26.76, 28.06, 29.35, 30.65, 31.97, 33.25, 34.56, 35.86, 37.17, 38.47, 39.76, 41.6, 42.4, 43.7, 45.0, 46.3, 47.6, 48.6, 50.2, 51.5, 52.8, 54.6, 55.4, 55.9]
print(len(Volt1))
Volt2 = [2.089, 2.153, 2.208, 2.265, 2.322, 2.379, 2.434, 2.490, 2.542, 2.596, 2.649, 2.701, 2.752, 2.802, 2.873, 2.902, 2.952, 2.998, 3.046, 3.094, 3.129, 3.186, 3.234, 3.278, 3.339, 3.366, 3.383]
# i(omar) switched to a shorter bnc cord at 1.89.
print(len(Volt2))

power_reading = [0.11, 0.17, 0.22, 0.28, 0.35, 0.47, 0.59, 0.78, 0.94, 1.18, 1.49, 1.84, 1.89, 2.30, 2.99, 3.36, 4.02, 4.82, 5.70, 6.73, 7.52, 9.09, 10.70, 12.31, 14.84, 16.29, 17.11] #This is S in nanoWatts
print(len(power_reading))


#print(len(x))
for i in range(len(Volt1)):
    print(str(Volt1[i])+','+str(Volt2[i])+','+str(power_reading[i]))
