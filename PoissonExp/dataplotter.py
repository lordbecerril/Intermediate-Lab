import matplotlib.pyplot as plt
import numpy as np
from math import exp
from math import factorial
from math import log
from statistics import mean
from statistics import variance
from statistics import stdev
from decimal import Decimal

def new_list_creator(x_axis, y_axis):
    # The following function creates a list where there are each element in x_axis is repeated a y_axis amount of times
    new_list = []
    count = 0
    for y in y_axis:
        for i in range(y):
            new_list.append(x_axis[count])
        count = count +1
    return(new_list)

def histogram_creator(x_axis, y_axis, title, y_label, name):

    fig = plt.figure() # This line is needed to create a figure

    #ax = fig.add_axes([0,0,1,1]) # This makes a 2d bar graph
    ax = fig.add_subplot(111)

    ax.set_ylabel(y_label)

    ax.set_title(title)

    ax.bar(x_axis,y_axis) # the .bar() creates the bar graph

    fig.savefig(name) # finally this command, shows the plot

def histogram_w_error_bar(x_axis, y_axis, error, title, y_label,name, flag):
    #https://stackoverflow.com/questions/11774822/matplotlib-histogram-with-errorbars
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
    plt.savefig(name) # Use plt.show() here

def histogram_w_poisson_dist(x_axis, y_axis, title, y_label, name, N,average):
    poisson_pts = []

    for x in range(N):
        y = (  (average**x)    *    (exp(-1*average))    ) / (Decimal(factorial(x)))
        y = y * 100
        poisson_pts.append(y)

    fig = plt.figure() # This line is needed to create a figure

    ax = fig.add_subplot(111)

    ax.set_ylabel(y_label)

    ax.set_title(title)

    ax.bar(x_axis,y_axis) # the .bar() creates the bar graph
    ax.plot(x_axis, poisson_pts,linestyle='solid',color='green')

    fig.savefig(name) # finally this command, shows the plot

def binned_histogram(N):
    #sturges_rule
    bins_k = 1 + 3.322 * log(N)
    print(int(bins_k))

def main():
    # Starting graph for Counts per 0.1 min #####################################################################
    print("6 second stuff-----------------------------------------------") #Print message to terminal

    x_axis = [0,1,2,3,4,5,6,7,8,9,10,11] # Values for our x-axis before dividing to 4

    quotients = [number / 4 for number in x_axis] #Values of our x-axis after dividing by 4

    y_axis = [6,10,38,36,42,25,20,16,4,1,1,1] # Values of our y axis

    # The following function creates a basic histogram
    histogram_creator(x_axis, y_axis, 'Counts with voltage set at 900V', 'counts/0.1 min',"6_second_count_histo.png")

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
    histogram_w_error_bar(x_axis, y_axis,standard_dev, 'Counts with voltage set at 900V', 'counts/0.1 min',"6_second_count_histo_w_error.png", False)
    histogram_w_error_bar(quotients, y_axis,stdev(new_list2), 'Counts with voltage set at 900V', 'counts/0.1 min',"6_second_count_histo_w_error_div4.png",True)

    histogram_w_poisson_dist(x_axis, y_axis, 'Counts with voltage set at 900V', 'counts/0.1 min',"6_second_count_histo_w_poisson.png",N,average)
    binned_histogram(N)

    # Starting graph for counts per 1 min #####################################################################
    print("1 minute stuff-----------------------------------------------")
    title = 'Counts with voltage set at 900V'

    x_axis = ['24','25','27','28','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','54','55'] # here we have what we want on our x axis # here we have what we want on our x axis
    for i in range(0, len(x_axis)):
        x_axis[i] = int(x_axis[i])
    quotients = [number / 4 for number in x_axis]

    y_axis = [2,1,1,1,5,4,7,7,7,5,5,7,9,11,12,3,14,6,11,9,7,11,6,3,1,1,1,2]

    y_label = 'counts/1 min'
    histogram_creator(x_axis, y_axis, title, y_label, "1_min_count_histo.png")

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
    histogram_w_error_bar(x_axis, y_axis,standard_dev, title, y_label,"1_min_count_histo_w_error.png",False)
    histogram_w_error_bar(quotients, y_axis,stdev(new_list2), title, y_label,"1_min_count_histo_w_error_div4.png",True)

    # Starting graph for counts per 10 min #####################################################################
    print("10 minute stuff----------------------------------------------")
    title = 'Counts with voltage set at 900V'

    x_axis = x_axis = ['343','358','363','364','367','371','372','373','374','377','379','380','382','392','395','399','400','403','404','412','414','417','421','432'] # here we have what we want on our x axis # here we have what we want on our x axis # here we have what we want on our x axis
    for i in range(0, len(x_axis)):
        x_axis[i] = int(x_axis[i])
    quotients = [number / 4 for number in x_axis]

    y_axis = y_axis = [1,1,1,1,2,1,2,1,1,2,1,1,4,2,1,2,1,2,2,1,1,1,1,1] # and here we have what we want on our y axis

    y_label = 'counts/10 min'
    histogram_creator(x_axis, y_axis, title, y_label,"10_min_count_histo.png")

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
    histogram_w_error_bar(x_axis, y_axis,standard_dev, title, y_label,"10_min_count_histo_w_error.png",False)
    histogram_w_error_bar(quotients, y_axis,stdev(new_list2), title, y_label,"10_min_count_histo_w_error_div4.png",True)


if __name__== "__main__":
    main()
