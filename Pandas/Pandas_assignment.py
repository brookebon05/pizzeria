"""
Create a Series from the list [7, 11, 13, 17].

Create a Series with five elements that are all 100.0.

Create a Series with 20 elements that are all random 
numbers in the range 0 to 100. Use method describe to 
produce the Series’ basic descriptive statistics.

Create a Series called temperatures of the floating-point values 
98.6, 98.9, 100.2 and 97.9. 
Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.

Form a dictionary from the names and values in Part (4), then use it to initialize a Series.
"""
import pandas as pd
import random as r

print("PART ONE \n\n")
series1 = pd.Series([7, 11, 13, 17])
print("Panda series 1:\n", series1)

print("PART TWO \n\n")
series2 = pd.Series(100.0, range(5))
print("Panda series 2:\n", series2)

print("PART THREE \n\n")
series3 = pd.Series(r.randint(1, 100, size=20))
print("Panda series 3:\n", series3)

print("PART FOUR \n\n")
print("PART FIVE \n\n")