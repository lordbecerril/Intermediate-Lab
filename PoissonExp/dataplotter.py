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

from statistics import mean
from statistics import variance
from statistics import stdev

from scipy.stats import norm
from scipy.stats import chisquare

def new_list_creator(x_axis, y_axis):
    '''
        FUNCTION PURPOSE:
            The following function creates a list where  each element of the
            x_axis list is repeated a y_axis amount of times to create a list of N
            elements where N is the number of observations we took
    '''
    # Create an empty list
    new_list = []
    # Dummy Variable used as an increment place holder
    count = 0
    # For every element 'y' in the list y_axis which is the number of times each Count/Time was observed, append the corresponding x element (Count per time) a y amount of times
    for y in y_axis:
        for i in range(y):
            new_list.append(x_axis[count])
        count = count + 1

    # Return the newly created list
    return(new_list)

def histogram_creator(x_axis, y_axis, title, y_label, x_label, name):
    '''
        PURPOSE:
            The following function creates a basic histogram of the raw data
            we gathered where the x_axis is a list with the counts/time and
            the y_axis is amount of times each was observed
    '''
    # Create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Set the labels and title
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

    # Create the actual bar graph
    ax.bar(x_axis,y_axis) # the .bar() creates the bar graph

    # Save the figure
    fig.savefig(name, dpi = 600) # finally this command, shows the plot
    # Clear the plot
    plt.clf()


def histogram_w_error_bar(x_axis, y_axis, error, title, y_label,name, flag):
    '''
        PURPOSE:
            Builds histogram with error bars that are the size of the standard_dev
    '''
    # Helpful link I found :https://stackoverflow.com/questions/11774822/matplotlib-histogram-with-errorbars
    # Build the plot
    fig, ax = plt.subplots()
    if flag == True:
        ax.bar(x_axis, y_axis, width =0.2,yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
    else:
        ax.bar(x_axis, y_axis,yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel(y_label)
    ax.set_xticks(x_axis)
    ax.set_title(title)
    ax.yaxis.grid(True)

    # Save the figure
    plt.tight_layout()
    #plt.show()
    plt.savefig(name, dpi = 600) # Use plt.show() here
    plt.clf()

def histogram_w_poisson_dist(x_axis, y_axis, title, y_label, name, N,average,tot_counts):
    '''
        PURPOSE:
            Builds a Histogram with a Poisson Distribution over it
    '''
    poisson_pts = []
    for x in range(N):
        a = (average**(x))
        b =(exp(-1*average))
        c = (factorial(x))
        y = (  a    *    b    ) / c
        y = y * tot_counts
        poisson_pts.append(y)

    print("Poisson stuff is ", poisson_pts)
    fig = plt.figure() # This line is needed to create a figure

    ax = fig.add_subplot(111)

    ax.set_ylabel(y_label)

    ax.set_title(title)

    ax.bar(x_axis,y_axis) # the .bar() creates the bar graph
    ax.plot(x_axis, poisson_pts,linestyle='solid',color='green')

    fig.savefig(name, dpi = 600) # finally this command, shows the plot
    plt.clf()

    print("Taking Chi Square of Poisson")
    print("Chi Square of Poisson is, ", chisquare(f_obs = y_axis, f_exp = poisson_pts) )
    print(" ")

def binned_histogram(N,average, standard_dev, data,name):
    '''
        PURPOSE:
            Makes a Histogram with binned data
    '''
    #sturges_rule
    bins_k = 1 + 3.322 * log(N)
    #print("Bins used by sturges_rule is: ", int(bins_k))

    # Fit a normal distribution to the data:
    mu, std = norm.fit(data)

    # Plot the histogram.
    plt.hist(data, bins=6, density=True, alpha=0.6, color='g')

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    plt.savefig(name, dpi = 600)

    plt.clf()


def main():

    # Starting graph for Counts per 0.1 min #####################################################################
    print("6 second stuff-----------------------------------------------") #Print message to terminal

    x_axis = [0,1,2,3,4,5,6,7,8,9,10,11] # Values for our x-axis before dividing to 4

    quotients = [number / 4 for number in x_axis] #Values of our x-axis after dividing by 4

    y_axis = [6,10,38,36,42,25,20,16,4,1,1,1] # Values of our y axis

    # The following function creates a basic histogram
    histogram_creator(x_axis, y_axis, 'Counts with voltage set at 900V', "Number of Times Observed",'counts/0.1 min',"6_sec_data/6_second_count_histo.png")

    new_list = new_list_creator(x_axis, y_axis)

    new_list2 = new_list_creator(quotients, y_axis)

    N = len(new_list)
    average = mean(new_list)
    var = variance(new_list)
    standard_dev = stdev(new_list)
    print("Number of observations: ", N)
    print("Mean is: ", average)
    print("Variance is :", var)
    print("Standard Deviation is :", standard_dev)
    print(" ")
    histogram_w_error_bar(x_axis, y_axis,standard_dev, 'Counts with voltage set at 900V', 'counts/0.1 min',"6_sec_data/6_second_count_histo_w_error.png", False)

    histogram_w_poisson_dist(x_axis, y_axis, 'Counts with voltage set at 900V', 'counts/0.1 min',"6_sec_data/6_second_count_histo_w_poisson.png",len(x_axis),average,N)

    binned_histogram(N,average, standard_dev, new_list,"6_sec_data/6_second_count_histo_w_gaussian_bin.png")

    # Starting graph for counts per 1 min #####################################################################
    print("1 minute stuff-----------------------------------------------")
    title = 'Counts with voltage set at 900V'

    x_axis = ['24','25','27','28','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','54','55'] # here we have what we want on our x axis # here we have what we want on our x axis
    for i in range(0, len(x_axis)):
        x_axis[i] = int(x_axis[i])
    quotients = [number / 4 for number in x_axis]

    y_axis = [2,1,1,1,5,4,7,7,7,5,5,7,9,11,12,3,14,6,11,9,7,11,6,3,1,1,1,2]

    y_label = 'counts/1 min'
    histogram_creator(x_axis, y_axis, title, "Number of Times Observed",'counts/1 min' , "1_min_data/1_min_count_histo.png")

    new_list = new_list_creator(x_axis, y_axis)
    new_list2 = new_list_creator(quotients, y_axis)

    N = len(new_list)
    average = mean(new_list)
    var = variance(new_list)
    standard_dev = stdev(new_list)
    print("Number of observations: ", N)
    print("Mean is: ", average)
    print("Variance is :", var)
    print("Standard Deviation is :", standard_dev)
    print(" ")
    histogram_w_error_bar(x_axis, y_axis,standard_dev, title, y_label,"1_min_data/1_min_count_histo_w_error.png",False)

    histogram_w_poisson_dist(x_axis, y_axis, 'Counts with voltage set at 900V', 'counts/1 min',"1_min_data/1_min_count_histo_w_poisson.png",len(x_axis),average,N)

    binned_histogram(N,average, standard_dev, new_list,"1_min_data/1_min_count_histo_w_gaussian_bin.png")

    # Starting graph for counts per 10 min #####################################################################
    print("10 minute stuff----------------------------------------------")
    title = 'Counts with voltage set at 900V'

    x_axis = x_axis = ['343','358','363','364','367','371','372','373','374','377','379','380','382','392','395','399','400','403','404','412','414','417','421','432'] # here we have what we want on our x axis # here we have what we want on our x axis # here we have what we want on our x axis

    for i in range(0, len(x_axis)):
        x_axis[i] = int(x_axis[i])
    quotients = [number / 4 for number in x_axis]

    y_axis = y_axis = [1,1,1,1,2,1,2,1,1,2,1,1,4,2,1,2,1,2,2,1,1,1,1,1] # and here we have what we want on our y axis

    histogram_creator(x_axis, y_axis, title, "Number of Times Observed" , "Counts Per 10 min." ,"10_min_data/10_min_count_histo.png")

    new_list = new_list_creator(x_axis, y_axis)
    new_list2 = new_list_creator(quotients, y_axis)

    N = len(new_list)
    average = mean(new_list)
    var = variance(new_list)
    standard_dev = stdev(new_list)
    print("Number of observations: ", N)
    print("Mean is: ", average)
    print("Variance is :", var)
    print("Standard Deviation is :", standard_dev)
    print(" ")
    histogram_w_error_bar(x_axis, y_axis,standard_dev, title, "Number of Times Observed","10_min_data/10_min_count_histo_w_error.png",False)

    histogram_w_poisson_dist(x_axis, y_axis, 'Counts with voltage set at 900V', 'counts/10 min',"10_min_data/10_min_count_histo_w_poisson.png",len(x_axis),average,N)
    binned_histogram(N,average, standard_dev, new_list,"10_min_data/10_min_count_histo_w_gaussian_bin.png")



if __name__== "__main__":
    main()
