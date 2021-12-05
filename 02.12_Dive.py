from read_input import read_file
import pandas as pd

# read the file from the second day 
commands = read_file('02.12.csv',['Command'])

# split the commands and the values into two separate columns
commands[['Command', 'Value']] = commands['Command'].str.split(' ', 1, expand=True)
# convert values from strings to integers
commands['Value'] = commands['Value'].astype(int)

# define a function that returns the calculated or final position depending on the bool selected in the final_position parameter
def calculate_position(df_name, commands_col, values_col, final_position=True):
    # group values by 'command' 
    down = df_name.groupby(commands_col)[values_col].get_group('down')
    up = df_name.groupby(commands_col)[values_col].get_group('up')
    forward = df_name.groupby(commands_col)[values_col].get_group('forward')
    # define the horizontal position 
    horizontal_position = forward.sum()
    # define the depth        
    depth = down.sum()-up.sum()
    
    # PART I
    # conditional - the final position is not required
    if final_position == False:
        # define the calculated position and print it if the final_position is set to False
        position_calc = horizontal_position*depth
        print('Calculated position: ', position_calc)
    
    # PART II
    # set the aim to 0
    aim = 0
    # reassign depth to 0
    depth = 0

    # conditional - the final position is required
    if final_position == True:
        # iterate over the data frame's rows with conditional statements and calculate depth and aim
        for index, command_value in df_name.iterrows():
            if command_value[0] == 'up':
                aim -= command_value[1]
            elif command_value[0] == 'down':
                aim += command_value[1]
            elif command_value[0] == 'forward':
                depth += command_value[1]*aim
                
        # calculate the final position
        final_position_calc = horizontal_position*depth
        print('Final position:', final_position_calc)

# call the function to reveal the position of the planned course
calculate_position(commands, 'Command', 'Value', final_position=False)

