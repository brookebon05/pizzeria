import numpy as np
import random

# cntrl shift P, start REPL
integers = np.array([1, 2, 3])
print(type(integers))
# prints

# create 1D array producing list of ints 2-20

new_ints = np.array([i for i in range(2, 21, 2)])
print(new_ints)

# 2d array
ints = np.array([[1, 2, 3], [4, 5, 6]])  # two rows of 3 columns
ints2 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])  # 1D row of floats 0 = 0.
print(ints, ints2)

a = ints.dtype
b = ints.ndim
c = ints.shape
d = ints.size

print()

for row in ints:
    print(row)
    for col in row:
        print(col, end=" ")

for i in ints.flat:  # Prints out 6 elements in a vertical line
    print(i)

# 2D array of 5 random ints

# 1.
ints3 = np.array(
    [
        [random.randint(1, 10) for x in range(5)],
        [random.randint(1, 10) for x in range(5)],
    ]
)
print(ints3)

b = np.array(
    np.random.randint(1, 10, size=(2, 5))
)  # pick numbers between 1, 10. and two rows and 5 cols

c = np.zeros(5)  # 5 0's
d = np.ones(5)
e = np.ones((2, 4), dtype=int)
print(e)
f = np.full((3, 5), 13)
g = np.arange(5)
h = np.arange(5, 10)
i = np.arange(10, 1, -2)

print()

# evenly-spaced floating point numbers
print(np.linspace(0.0, 1.0, num=5))  # 0, 0.25, 0.5, 0.75, 1

array1 = np.arange(1, 21)  # not incuding 21
array2 = array1.reshape(4, 5)  # Must match up exactly
print(array1)
print(array2)
array3 = np.arange(1, 100001).reshape(4, 25000)
array4 = np.arange(1, 100001).reshape(100, 1000)
print(array3)
print(array4)

numbers = np.arange(1, 6)
numbers += 10  # Changes elements in the array to 11, 12, etc...
print(numbers)
print(numbers * 2)  # prints 2, 4, etc...

# multiplying int arrays with floating point arrays gets you a floating pt array
numbers2 = np.linspace(1.1, 5.5, 5)
print(numbers * numbers2)

print(numbers >= 13)  # yields true and false values
print(numbers == numbers2)  # yields true and false values
