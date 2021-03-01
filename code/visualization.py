# importing matplotlib module 
from matplotlib import pyplot as plt 

def line_plot():
	# x-axis values 
	x = [5, 2, 9, 4, 7] 

	# Y-axis values 
	y = [10, 5, 8, 4, 2] 

	# Function to plot 
	plt.plot(x,y) 

	# function to show the plot 
	plt.show() 

def bar_plot():
	# x-axis values 
	x = [5, 2, 9, 4, 7] 

	# Y-axis values 
	y = [10, 5, 8, 4, 2] 

	# Function to plot the bar 
	plt.bar(x,y) 

	# function to show the plot 
	plt.show() 

def histogram():
	# Y-axis values 
	y = [10, 5, 8, 4, 2] 

	# Function to plot histogram 
	plt.hist(y) 

	# Function to show the plot 
	plt.show() 


def scatter_plot():
	# x-axis values 
	x = [5, 2, 9, 4, 7] 

	# Y-axis values 
	y = [10, 5, 8, 4, 2] 

	# Function to plot scatter 
	plt.scatter(x, y) 

	# function to show the plot 
	plt.show() 


line_plot()
bar_plot()
histogram()
scatter_plot()