# Advent_of_Code

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language. I've decided to solve them in Python.

---

### read_input.py

In this file, I define a function that takes the file name(i.e. '01.12.csv' in the _inputs_ folder) and the column names (i.e. ['Measurement']) as parameters to return a dataframe.

- own function 'read_file(_file_name, col_names_)'
- [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

---

### 01.12_Sonar_Sweep.py

#### [Instructions](https://github.com/xxvazquez/Advent_of_Code/blob/main/instructions/01.12.diff)

In **part I**, I define another function that returns the count of the largest and smallest values relative to the previous value of a specific column in the data frame. 

- own function 'count_trype(_df_name, column_name_)'
- [if statement](https://docs.python.org/3/tutorial/controlflow.html)
- [for statement](https://docs.python.org/3/tutorial/controlflow.html)
- [.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html)
   -  [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
- [tolist()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist)
- [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)

In **part II**, I add a new column (_sum_) to the original dataframe and use the rolling function with a defined window equal to three that calculates the moving sum.

- [.rolling()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
   - [window](https://pandas.pydata.org/docs/reference/window.html) 
- [.sum()](https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.sum.html)

---

### 02.12_Dive.py

At first, right after reading the file with my own function, I split the commands and the values into two columns and convert the values into integers. Then I define another function that returns the _calculated position_ (**part I**) if the _final_position_ is _False_ or the _final position_ (**part II**) if the _final_position_ is _True_. The function first groups the values by _command_, defines the _horizontal position_ and _depth_ and then calculates the position depending on the selected parameter. If _False_, the _calculated position_ is equal to the _horizontal position_ times the _depth_. If _True_, the _aim_ and _depth_ are set to 0 and the function iterates over the rows of the data frame. If the value is _up_, the aim will decrease its value; if the value is _down_, the aim will increase its value; and if the value is _forward_, the _depth_ will be equal to the value times the _aim_. The _final position_ is calculated by multiplying the _depth_ by the _horizontal position_.

- own function 'calculate_position(_df_name, commands_col, values_col, final_position=False_)'
- [.str.split](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html)
- [.astype()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)
- [.groupby()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
- [.get_group()](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.get_group.html)
- [iterrows()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html?highlight=iterrows#pandas.DataFrame.iterrows)
- .sum()
- for statement
- if statement

