#!/usr/bin/env python
'''
This example simply reads in a terminal solution (an exnode file commonly written by lungsim) and calculates
the coefficient of variation of the solution field of your choice
'''
# We need to import numpy to calculate means and standard deviations easily
import numpy as np
#We also need to import the lungsimpost for post-processing specific tools
import lungsimpost as lsp

#We first identify the file we want to analyse, this is an exnode file which contains information on node location
# and fields containing values predicted by the model at each node point.
file_to_analyse = '../example_inputs/solution_terminal.exnode'
#If you open the exnode file and take a look, you'll see that each node is defined by its node number, three coordinate
# fields and a number of other solution fields. We can pick the field that we want to calculate the coefficient of
# variation of (in this case it is the 'flow' field
field_to_average = 4 #indexing starts at zero, but first field will always be node number
#We now use lungsim-post to import our solution file
model_results = lsp.import_exnode_tree('../example_inputs/solution_terminal.exnode')
#Next we pull out the field we want to analyse
field = model_results['nodes'][:,field_to_average]
#Finally we calculate the mean and standard deviation of this field and combine them to calculate the coefficient
# of variation
mean_field = np.mean(field)
std_field = np.std(field)
cov_field = std_field/mean_field*100. # in percent
#Now, we'll print to screen and our job is done
print("The mean value of your field is: ", mean_field)
print("The standard deviation of your field is: ", std_field)
print("This means that the cofficient of variation is: ", cov_field, "%")
