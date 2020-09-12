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


def histogram(data, x_axis, y, name):
    # Create the figure
    plt.hist(data)
    #plt.show()
    plt.clf()

    # Graphing poisson
    fig, ax = plt.subplots(1, 1)
    mu = statistics.mean(data)
    print("average is ", mu)
    mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
    ax.plot(data, poisson.pmf(data, mu), 'bo', ms=8, label='poisson pmf')
    ax.vlines(data, 0, poisson.pmf(data, mu), colors='b', lw=5, alpha=0.5)
    plt.savefig(name+"_poisson.png")
    plt.clf()

    poisson_pts = poisson.pmf(data, mu)
    print("Chi Square is ", chisquare(poisson_pts))
    poisson_pts = [i * len(data) for i in poisson_pts]



    print("Poisson stuff is ", poisson_pts)

    # Graph with errorbars, histo and poisson
    #plt.bar(x_axis,y, yerr = statistics.stdev(data))
    plt.hist(data)
    plt.plot(
        data,
        poisson_pts,
        marker='o', linestyle='',
        label='Fit result',
    )
    plt.legend()
    plt.savefig(name+"_poisson2.png")
    plt.clf()

    # Fit a normal distribution to the data:
    mu, std = norm.fit(data)
    plt.hist(data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    list = p
    list = [i * len(data) for i in p]
    print("Chi Square of the normal distribution is ", chisquare(p))

    print("p is ", list)
    plt.plot(x, list, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    plt.savefig(name+"_normal.png")
    plt.clf()



    # Now normal with poisson, error and bar graph
    print(x)
    print(y)
    plt.hist(data)
    plt.plot(data,poisson_pts,marker='o', linestyle='',label='Fit result')
    plt.plot(x, list, 'k', linewidth=2)
    plt.savefig(name+"normal_poisson.png")

def voltage_grapher(x,y):
    fig = plt.figure() # This line is needed to create a figure

    ax = fig.add_subplot(1,1,1) # This makes a 2d bar graph

    ax.set_ylabel('Counts / 0.1 min')
    ax.set_xlabel('Voltage')
    ax.set_title('Gieger-Muller Plateau')
    ax.plot(x,y,linestyle='solid', color= 'blue') # the .bar() creates the bar graph
    plt.savefig("./NewGraphs/voltage.png", dpi = 600) # finally this command, shows the plot
    plt.clf()

def latex_table_creator(x,y):
    length = len(x)
    for i in range(length):
        print(str(x[i]) +" & "+str( y[i])+ " \\\ ")

def all_three(d1,d2,d3):

    plt.hist(d1)
    plt.hist(d2)
    plt.hist(d3);
    plt.show()

def analysis(data):
    print("Total Elements are ", len(data))
    print("Mean from statistics.mean ", statistics.mean(data))
    print("Variance from statistics.mean is ", statistics.variance(data))
    print("Standard Deviation form statistics.stdev is ", statistics.stdev(data))


def cleaning(x_axis,y_axis, name):

    data = []
    count = 0
    # For every element 'y' in the list y_axis which is the number of times each Count/Time was observed, append the corresponding x element (Count per time) a y amount of times
    for y in y_axis:
        for i in range(y):
            data.append(x_axis[count])
        count = count + 1

    print(data)

    analysis(data)
    histogram(data, x_axis, y_axis, name)


def main():
    # Graphing the voltage
    #x_axis = [500, 600, 700,800,810,820,850,900,950,1000,1100,1200] # here we have what we want on our x axis
    #y_axis = [0,0,0,0,3,4,3,4,7,10,11,152] # and here we have what we want on our y axis
    #voltage_grapher(x_axis, y_axis)
    #latex_table_creator(x_axis,y_axis)

    print("6 second stuff-----------------------------------------------") #Print message to terminal
    cleaning([0,1,2,3,4,5,6,7,8,9,10,11], [6,10,38,36,42,25,20,16,4,1,1,1], "6_second")


    print("1 min stuff-----------------------------------------------") #Print message to terminal
    x_axis = ['24','25','27','28','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','54','55'] # here we have what we want on our x axis # here we have what we want on our x axis
    for i in range(0, len(x_axis)):
        x_axis[i] = int(x_axis[i])
    cleaning(x_axis, [2,1,1,1,5,4,7,7,7,5,5,7,9,11,12,3,14,6,11,9,7,11,6,3,1,1,1,2], "1_minute")


    print("10 minute stuff----------------------------------------------")

    x_axis = ['343','358','363','364','367','371','372','373','374','377','379','380','382','392','395','399','400','403','404','412','414','417','421','432'] # here we have what we want on our x axis # here we have what we want on our x axis # here we have what we want on our x axis
    for i in range(0, len(x_axis)):
        x_axis[i] = int(x_axis[i])

    cleaning(x_axis, [1,1,1,1,2,1,2,1,1,2,1,1,4,2,1,2,1,2,2,1,1,1,1,1], "10_minute")




if __name__== "__main__":
    main()
