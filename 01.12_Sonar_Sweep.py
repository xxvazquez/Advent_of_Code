import pandas as pd
import os

# create the new dir
current_dir = os.getcwd()
new_dir = current_dir + '/inputs/' 

# read the measurements from the file and add a column name
col_name = ['Measurement']
measurements = pd.read_csv(new_dir + '01.12.csv', names=col_name)

# convert the dataframe into a list
measurements_list = measurements.values.tolist()

# define a function to count larger and smaller values 
def count_measurements_type(list_name):
    i_larger = 0
    i_smaller = 0
    # iterate over the list
    for index, value in enumerate(list_name):
        # exclude first value
        if (index > 0):
            if list_name[index] > list_name[index-1]:
                # add the count
                i_larger += 1
            else:
                i_smaller += 1
    # print the values
    print('Smaller values:', i_smaller)
    print('Larger values:', i_larger)

# call the function with the list name that was defined before
count_measurements_type(measurements_list)
