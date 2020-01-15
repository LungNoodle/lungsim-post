========================================
Example 1: Reading and manipulating data
========================================

This example simply reads in a terminal solution (an exnode file commonly written by lungsim) and calculates
the coefficient of variation of the solution field of your choice. You can find this example within the
lungsim-post source code, in the 'examples' directory.

Requirements
------------
You'll need lungsim-post installed on your machine, as well as numpy (which was a requirement of lungsim-post so
should be automatically satisfied!).

How to run this example
-----------------------

Navigate to the 'example1' directory, and simply run the code in python:

.. code-block:: console

    python read_terminal_calc_COV.py

If all is well, the following should print to your screen:

.. code-block:: console

    The mean value of your field is:  2.093857892750033
    The standard deviation of your field is:  0.7205034720617964
    This means that the cofficient of variation is:  34.410332934079925 %

What is the code doing?
-----------------------

The code is reading the file 'solution_terminal.exnode' from the 'example_inputs directory. Let's have a look at the
first few lines of that file to understand what is inside it:

.. code-block:: text

     Group name: perf_model
     #Fields=3
     1) coordinates, coordinate, rectangular cartesian, #Components=3
      x.  Value index=1, #Derivatives=0
      y.  Value index=2, #Derivatives=0
      z.  Value index=3, #Derivatives=0
     2) flow, field, rectangular cartesian, #Components=1
      1.  Value index=4, #Derivatives=0
     3) pressure, field, rectangular cartesian, #Components=1
      1.  Value index=5, #Derivatives=0
     Node:           81
         202.491200
         155.026700
        -102.544300
           0.853527
        1862.766929

This is a typical output from a model (in this case the perfusion model. The file tells us that there are 3 fields
(including coordinates) so each node will be have 6 numbers associated with it (the node number, 3 coordinate fields,
and two solution fields). Let's say we are interested in calculating the coefficient of variation in the first solution
field - the 'flow' field. This is how we use lungsim-post to do that.

Like any python file, the first thing we need to do is to import any libraries that might help us. In this case
we need numpy to make calculating means and standard deviations easy, and lungsim-post

.. code-block:: python

    import numpy as np
    import lungsimpost as lsp


We first identify the file we want to analyse. As discussed above this is an exnode file which contains information on
node location and fields containing values predicted by the model at each node point.

.. code-block:: python

    file_to_analyse = '../example_inputs/solution_terminal.exnode'

Remember,  each node is defined by its node number, three coordinate fields and a number of other solution fields.
We can pick the field that we want to calculate the coefficient of variation of (in this case it is the 'flow' field

.. code-block:: python

    field_to_average = 4 #indexing starts at zero, but first field will always be node number

We now use lungsim-post to import our solution file:

.. code-block:: python

    model_results = lsp.import_exnode_tree('../example_inputs/solution_terminal.exnode')

Next we pull out the field we want to analyse

.. code-block:: python

    field = model_results['nodes'][:,field_to_average

Finally we calculate the mean and standard deviation of this field and combine them to calculate the coefficient
of variation

.. code-block:: python

    mean_field = np.mean(field)
    std_field = np.std(field)
    cov_field = std_field/mean_field*100. # in percent

Now, we'll print to screen and our job is done

.. code-block:: python

    print("The mean value of your field is: ", mean_field)
    print("The standard deviation of your field is: ", std_field)
    print("This means that the cofficient of variation is: ", cov_field, "%")
