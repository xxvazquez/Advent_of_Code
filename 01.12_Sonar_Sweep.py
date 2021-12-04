from read_input import read_file

# read the file from the first day 
measurements = read_file('01.12.csv',['Measurement'])

# PART I
# define another function that returns the count of the largest and smallest values relative to the previous value of a specific column in the data frame.
def count_type(df_name, column_name):
    # convert the dataframe to ndarray and then to a list
    list_name = df_name[column_name].values.tolist()
    # create two lists that will contain the values that are larger or smaller
    larger  = []
    smaller = []
    # iterate over the list name and append values to the list depending on the condition
    for index, value in enumerate(list_name):
        # exclude the firt record 
        if index > 0:
            # if the second, (third...) record is greater than the first (second...)
            if (list_name[index] > list_name[index-1]):
                # append to the list 'larger'
                larger.append(value)
            # otherwise append to the list 'smaller'
            else:
                smaller.append(value)
    # print the values
    print('Smaller -->', len(smaller))
    print('Larger -->', len(larger))

# call the function with the list name that was defined before
print('Part I - Measurements:')
count_type(measurements, 'Measurement')


# PART II
# add one column with the sum of three records and use the rolling function with a defined window equal to three that calculates the moving sum
measurements['sum'] = measurements['Measurement'].rolling(3).sum()
print('Part Two - Sum:')
#call the function and pass the new column in the column_name parameter
count_type(measurements, 'sum')
