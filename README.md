# Advent_of_Code

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language. I've decided to solve them in Python.

### read_input.py

In this file, I define a function that takes the file name(i.e. '01.12.csv' in the 'inputs' folder) and the column names (i.e. ['Measurement']) as parameters to return a dataframe.

- own function 'read_file()'
- [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

### 01.12_Sonar_Sweep.py

#### [Instructions](https://github.com/xxvazquez/Advent_of_Code/blob/main/instructions/01.12.diff)

In part I, I define another function to count the larger and smaller values in a dataframe column. The parameters required are 'dataframe name' and 'column name'. It returns the smaller and larger values.

- own function 'count_trype()'
- [.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html)
   -  [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
- [tolist()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist)
- [for loop](https://docs.python.org/3/tutorial/controlflow.html)
- [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)

In part II, I add a new column ('sum') to the original dataframe and use the rolling function with a defined window equal to three that calculates the moving sum.

- [.rolling()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
   - [window](https://pandas.pydata.org/docs/reference/window.html) 
- [.sum()](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.sum.html)
