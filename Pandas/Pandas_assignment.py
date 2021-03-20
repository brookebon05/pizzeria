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
import numpy as np

print("\nPART ONE \n")
series1 = pd.Series([7, 11, 13, 17])
print("Panda series 1: \n\n", series1, sep="")
print("\n\n")

print("PART TWO \n")
series2 = pd.Series(100.0, range(5))
print("Panda series 2: \n\n", series2, sep="")
print("\n\n")

print("PART THREE \n")
numbers = np.random.randint(0, 101, size=20)
series3 = pd.DataFrame(numbers, columns=["Random numbers between 0 and 100"])
print("Series 3: \n\n", series3, sep="")
print("\nPanda series 3 described:\n\n", series3.describe())
print("\n\n")

print("PART FOUR \n")
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9])
temperatures.index = ["Julie", "Charlie", "Sam", "Andrea"]
print("Temperatures: \n\n", temperatures, sep="")
print("\n\n")

print("PART FIVE \n")
temps_dict = {
    "Julie": [98.6],
    "Charlie": [98.9],
    "Sam": [100.2],
    "Andrea": [97.9],
}
temps = pd.DataFrame(temps_dict)
print("Temperatures formed from a dictionary: \n\n", temps)
print("\n\n")
