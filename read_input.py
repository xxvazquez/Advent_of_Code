import os
import pandas as pd

# define a function that reads a file and converts it to a dataframe
def read_file(file_name, col_names, converters=None):
    # create the new dir
    current_dir = os.getcwd()
    new_dir = current_dir + '/inputs/' 
    # define a global dataframe
    global df
    # read the values from the file and assign them to a df
    df = pd.read_csv(new_dir + file_name, names=col_names, converters=converters)
    return(df)
