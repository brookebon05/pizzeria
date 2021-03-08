import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
# each row is a student, each column is a test
a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

# works on the matrix level
g = grades.mean(axis=0)
# gives averages for all students across Test 1
# AXIS = 1 calculates averages of rows

print(g)