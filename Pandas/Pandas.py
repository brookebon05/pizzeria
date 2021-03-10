import pandas as pd

grades = pd.Series([87, 100, 94])
print(grades)

same_grade = pd.Series(98.6, range(3))
print(same_grade)

print(grades[0])
grades.count()

print(grades.describe())  # gives stats

grades = pd.Series([87, 100, 94], indexes=["Wally", "eva", "sam"])
print(grades)

grades = pd.Series({"wally": 87, "eve": 90, "sam": 60})
print(grades)
print(grades.Wally)
print(grades.values)