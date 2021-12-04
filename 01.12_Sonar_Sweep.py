import pandas as pd
from read_input import read_file

# read the file from the first day 
measurements = read_file('01.12.csv',['Measurement'])

# PART I
# define a function to count larger and smaller values 
def count_type(df_name, column):
    # convert the dataframe into a list
    list_name = df_name[column].values.tolist()
    # set the counter to 0 
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
    print('Smaller -->', i_smaller)
    print('Larger -->', i_larger)

# call the function with the list name that was defined before
print('Measurements:')
count_type(measurements, 'Measurement')


# PART II
# add one column with the sum of three records
measurements['sum'] = measurements['Measurement'].rolling(3).sum()
print('Sum:')
count_type(measurements, 'sum')
