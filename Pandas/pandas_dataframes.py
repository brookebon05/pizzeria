import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}
print(grades_dict)
grades = pd.DataFrame(grades_dict)

print(grades)

grades.index = ["test1", "test2", "test3"]

print(grades)

print(grades["eva"])
print(grades.Sam)
print(grades.loc["test1"])
print(grades.iloc[1])
print(grades.loc["test1":"test3"])  # Does include upper bound!
print(grades.iloc[0:2])

# View only Eva and Katie's grades for test1 and test2
print(grades.loc["test1":"test2", ["eva", "Katie"]])
print(grades.iloc[0:2, [1, 3]])

above_90 = grades[grades > 90]
print(above_90)
bees = grades[(grades >= 80) & (grades < 90)]
print(bees)

print(grades.at["test1", "eva"])
print(grades.iat[1, 2])
grades.at["test2", "eva"] = 100
print(grades)
print(grades.describe())

pd.set_option("precision", 2)
print(grades.describe())
grades = grades.T  # transposes to get stats by test instead
print(grades.T.describe())
print(grades.T.mean())

grades.sort_index(ascending=False)  # default order is by rows
print(grades)

grades.sort_index(axis=1)
grades.sort_values(by="test1", axis=1, ascending=False)
