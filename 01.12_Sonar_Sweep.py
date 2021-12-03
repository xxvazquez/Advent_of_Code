import pandas as pd
import os

# PART I
# create the new dir
current_dir = os.getcwd()
new_dir = current_dir + '/inputs/' 

# read the measurements from the file and add a column name
col_name = ['Measurement']
measurements = pd.read_csv(new_dir + '01.12.csv', names=col_name)

# define a function to count larger and smaller values 
def count_measurements_type(df_name, column):
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
    print('Smaller:', i_smaller)
    print('Larger:', i_larger)

# call the function with the list name that was defined before
print('Measurements:')
count_measurements_type(measurements, 'Measurement')


# PART II
# add one column with the sum of three records
measurements['sum'] = measurements['Measurement'].rolling(3).sum()
print('Sum:')
count_measurements_type(measurements, 'sum')
