# Can take any number of arguments, but only has one expression
remainder = lambda num: num % 2
print(remainder(5))

product = lambda x, y: x * y
print(product(2, 3))


def testfunc(num):
    return lambda x: x * num


result1 = testfunc(10)
result2 = testfunc(100)

print(result1(9))
print(result2(9))

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
# filter takes object, iterable
print(filtered_list)  # filters out the numbers less than 7


def addition(n):
    return n + n


# double all numbers using regular function
numbers = [1, "a", 3, 4]
numbers2 = (4, "bob", 2, 7, 5)
result = map(lambda x, y: x + y, numbers, numbers2)
# map applies function to
print(list(result))

import os

clear = lambda: os.system("clear")
clear()

product = lambda x, y: x * y
print(product(2, 3))
