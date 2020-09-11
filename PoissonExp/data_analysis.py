'''
######################################
AUTHOR:
    Eric Becerril-Blas

PURPOSE:
    This code is for experiment 1 of the Physics 413 lab. More info can be found
    in the README.md
######################################
'''
# Libraries used below
import matplotlib.pyplot as plt

import numpy as np

from math import exp
from math import factorial
from math import log
import statistics

from scipy.stats import poisson
from scipy.stats import norm


from scipy.stats import norm
from scipy.stats import chisquare


def histogram(data, x_axis, y, bin):
    # Create the figure
    plt.hist(data)
    #plt.show()
    plt.clf()


    plt.hist(data, bins = bin)
    plt.show()
    plt.clf()
    # Graphing poisson
    fig, ax = plt.subplots(1, 1)
    mu = statistics.mean(data)
    print("average is ", mu)
    mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
    ax.plot(data, poisson.pmf(data, mu), 'bo', ms=8, label='poisson pmf')
    ax.vlines(data, 0, poisson.pmf(data, mu), colors='b', lw=5, alpha=0.5)
    plt.show()
    plt.clf()

    poisson_pts = poisson.pmf(data, mu)
    print("Chi Square is ", chisquare(poisson_pts))
    poisson_pts = [i * len(data) for i in poisson_pts]

    #print("Poisson stuff is ", poisson_pts)

    # Graph with errorbars, histo and poisson
    #plt.bar(x_axis,y, yerr = statistics.stdev(data))
    plt.hist(data, bins = bin)
    plt.plot(
        data,
        poisson_pts,
        marker='o', linestyle='',
        label='Fit result',
    )
    plt.legend()
    plt.show()
    plt.clf()

    # Fit a normal distribution to the data:
    mu, std = norm.fit(data)
    plt.hist(data, bins = bin)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    list = p
    list = [i * len(data) for i in p]

    print("p is ", list)
    plt.plot(x, list, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    plt.show()
    plt.clf()
    print("Chi Square of the normal distribution is ", chisquare(list))

    # Now normal with poisson, error and bar graph
    print(x)
    print(y)
    plt.hist(data, bins = bin)
    plt.plot(data,poisson_pts,marker='o', linestyle='',label='Fit result')
    plt.plot(x, list, 'k', linewidth=2)
    plt.show()

def main():

    # Starting graph for Counts per 0.1 min #####################################################################
    print("6 second stuff-----------------------------------------------") #Print message to terminal

    x_axis = [0,1,2,3,4,5,6,7,8,9,10,11] # Values for our x-axis before dividing to 4
    y_axis = [6,10,38,36,42,25,20,16,4,1,1,1] # Values of our y axis

    #data = np.random.randn(1000)
    #print(data)

    data = []
    count = 0
    # For every element 'y' in the list y_axis which is the number of times each Count/Time was observed, append the corresponding x element (Count per time) a y amount of times
    for y in y_axis:
        for i in range(y):
            data.append(x_axis[count])
        count = count + 1

    print(data)

    histogram(data, x_axis, y_axis, 12)






if __name__== "__main__":
    main()
