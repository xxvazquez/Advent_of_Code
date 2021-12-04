# Advent_of_Code

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language. I've decided to solve them in Python.

---

### read_input.py

In this file, I define a function that takes the file name(i.e. '01.12.csv' in the _inputs_ folder) and the column names (i.e. ['Measurement']) as parameters to return a dataframe.

- own function 'read_file()'
- [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

---

### 01.12_Sonar_Sweep.py

#### [Instructions](https://github.com/xxvazquez/Advent_of_Code/blob/main/instructions/01.12.diff)

In **part I**, I define another function that returns the count of the largest and smallest values relative to the previous value of a specific column in the data frame. The parameters required are _dataframe name_ and _column name_. 

- own function 'count_trype()'
- [if statement](https://docs.python.org/3/tutorial/controlflow.html)
- [for statement](https://docs.python.org/3/tutorial/controlflow.html)
- [.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html)
   -  [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
- [tolist()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist)
- [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)

In **part II**, I add a new column ('sum') to the original dataframe and use the rolling function with a defined window equal to three that calculates the moving sum.

- [.rolling()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
   - [window](https://pandas.pydata.org/docs/reference/window.html) 
- [.sum()](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.sum.html)

---

### 02.12_Dive.py

In **part I**, I split the commands and the values into two columns and I convert the values to integers. Then I group the _values_ by _command_, sum them and calculate the depth (down-up) and the horizontal position. The calculated position is equal to the horizontal position times the depth.

- [.str.split](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html)
- [.astype()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)
- [.groupby()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
- [.get_group()](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.get_group.html)
