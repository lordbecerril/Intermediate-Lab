import matplotlib.pyplot as plt



def graphmaker(x_axis, y_axis, title, y_label):

    fig = plt.figure() # This line is needed to create a figure

    ax = fig.add_axes([0,0,1,1]) # This makes a 2d bar graph

    ax.set_ylabel(y_label)

    ax.set_title(title)


    ax.bar(x_axis,y_axis) # the .bar() creates the bar graph

    plt.show() # finally this command, shows the plot



print("6 second stuff")
title = 'Counts with voltage set at 900V'
x_axis = ['0','1','2','3','4','5','6','7','8','9','10','11'] # here we have what we want on our x axis
y_axis = [6,10,38,36,42,25,20,16,4,1,1,1] # and here we have what we want on our y axis
y_label = 'cnts/0.1 min'
graphmaker(x_axis, y_axis, title, y_label)
