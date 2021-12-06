from read_input import read_file

# read the file from the third day 
diagnostic_report = read_file('03.12.csv', ['Binary'], converters={'Binary': lambda x: str(x)})


# PART I
# split the column with the values into separate columns selecting all columns but the first and the last empty ones
diagnostic_report = diagnostic_report['Binary'].str.split(pat= '\s*', expand=True).iloc[:,1:-1]

# define two empty strings for the rates
gamma_rate = ""
epsilon_rate = ""
# iterate over the columns of the dataframe
for index, column in diagnostic_report.iteritems():
    # calculate the median of each column to find out which value is the most common
    gamma_rate += str(int(column.median(axis=0)))

# iterate over gamma rate string and create epsilon rate reversing the numbers as per the conditional statement
for character in gamma_rate:
    if character == '0':
        epsilon_rate += '1'
    else:
        epsilon_rate += '0'

# convert the binary strings into integers
gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)
# calculate the power consumption
power_consumption = gamma_rate_dec*epsilon_rate_dec

# print the results
print('-----',
      'Gamma rate binary: {}'.format(gamma_rate),
      'Gamma rate decimal: {}'.format(gamma_rate_dec),
      '-----',
      'Epsilon rate binary: {}'.format(epsilon_rate),
      'Epsilon rate decimal: {}'.format(epsilon_rate_dec), 
      '-----',
      'Power consumption: {}'.format(power_consumption), 
      '-----',
      sep='\n')