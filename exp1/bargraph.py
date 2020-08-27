import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')

x = [2,3,5,3,5,4]
energy = [5, 6, 15, 22, 24, 8]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='green')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x, x_pos)

plt.show()
