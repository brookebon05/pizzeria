import numpy as np
import random

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
# gives averages for all students across Test 1 = COLS
# AXIS = 1 calculates averages of rows

print(g)

numbers = np.array([1, 4, 8, 16, 25, 36])
sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1, 7) * 10  # does 1,2,3,4,5,6 times 10
np_add = np.add(numbers, numbers2)
np_multiple = np.multiply(numbers2, 5)
print(np_multiple)
numbers3 = numbers.reshape(2, 3)
print("num3", numbers3)
numbers4 = np.array([2, 4, 6])
np_mult2 = np.multiply(numbers3, numbers4)
print(np_mult2)


# grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
# Single element
a = grades[0, 1]  # this is 96, 0 = first row, 1 is second column

# Single row, all columns
b = grades[1]

# Multiple rows sequential
c = grades[0:2]

rows = grades[[0, 2]]
element = grades[0, 2]
print(d)

# get test 1 and 3 for all students
f = grades[:, [0, 2]]
h = grades[:, 0:1]
print(f)
print(h)

grade_ex = np.array([random.randint(60, 100) for x in range(12)])
print(grade_ex)

res = grade_ex.reshape(3, 4)
print(res)

# grades = np.random.randint(60,101,12).reshape(3,4)

print("test ave:", np.average(res))

# or grades.mean(axis = 0)
for x in range(4):
    print(np.average(res[:, x]))

for x in range(3):
    print(np.average(res[x, :]))

# shallow copies(view)
numbers = np.arange(1, 6)
print(numbers)
numbers2 = numbers.view()

numbers[1] *= 10
print(numbers2)  # numbers2 updates!

numbers2 = numbers2[0:3]  # creates a shallow copy
numbers[1] *= 20
print(numbers2)

numbers2 = numbers.copy()  # Creates a whole new array
numbers[1] *= 10
print(numbers)
print(numbers2)

a = grades.reshape(1, 12)  # does not affect original
print(grades)
b = grades.resize(1, 12)  # DOES affect original
print(grades)

# produces deep copy
flattened = grades.flatten()

# produces shallow copy--changes grades
raveled = grades.ravel()
raveled[0] = 100
raveled[5] = 99
print(grades)

t = grades.T
print(t)

matrices_horz = np.hstack((numbers2, numbers2))  # adds columns
print(matrices_horz)
mat_vert = np.vstack((numbers, numbers))  # adds rows
print(mat_vert)
