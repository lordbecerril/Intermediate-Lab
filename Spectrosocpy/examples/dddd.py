import numpy as np

x = np.array([14.50514,19.00792,20.50299,20.50275])
y = np.array([4046.56, 5460.74, 5789.66, 5790.66])

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print(z)
print(p)
#plotting
import matplotlib.pyplot as plt
xp = np.linspace(x[0], x[-1], 50)
plt.plot(x, y, '.', xp, p(xp))
plt.show()
