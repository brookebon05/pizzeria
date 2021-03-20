## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers.
salesArray = np.array(
    [
        [150.68, 207.99, 107.88, 58.99, 60.59],
        [20.89, 98.99, 258.62, 19.76, 101.59],
        [70.66, 190.10, 134.54, 200.14, 15.59],
        [10.52, 201.59, 140.55, 13.99, 45.98],
    ]
)

## Step 1: Print the total sales for the store.
print(
    "-----------------------------------------------   STEP ONE   -----------------------------------------------"
)
totalsales = salesArray.sum()

print("Total store sales: $", totalsales)

## Step 2: What was Superstore's smallest and largest sale? Print them.
print(
    "-----------------------------------------------   STEP TWO   -----------------------------------------------"
)
max1 = salesArray.max()
min1 = salesArray.min()

print("Largest sale: $", max1, "\n", "Smallest sale: $", min1)

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print(
    "-----------------------------------------------   STEP THREE  -----------------------------------------------"
)

temp = []
for x in salesArray:
    for i in x:
        if i >= 100:
            temp.append(round(i, 2))
sales1 = np.array(temp)
print("Array of sales greater than $100: ", sales1)

## Step 4: Print the total sales for each register.
print(
    "-----------------------------------------------   STEP FOUR   -----------------------------------------------"
)

counter = 1
for x in salesArray:
    print("Register", counter, "has sales", round(sum(x), 2))
    counter += 1

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print(
    "-----------------------------------------------   STEP FIVE  -----------------------------------------------"
)

temp2 = []
for i in salesArray:
    for x in i:
        temp2.append(round(x * 0.02, 2))
fees = np.array(temp2)
total = round(fees.sum(), 2)
print("An array of fees:", fees, "\n", "And the total fees are $", total)

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print(
    "-----------------------------------------------   STEP SIX  -----------------------------------------------"
)
profit = []
fees2 = fees.reshape(4, 5)
profit = salesArray - fees2
print("Profit array:", profit)


## Step 7: Print the sales only for the second and forth cash register
print(
    "-----------------------------------------------   STEP SEVEN  -----------------------------------------------"
)

print(
    "Second register sales:",
    salesArray[1, :],
    "\n",
    "Fourth register sales:",
    salesArray[3, :],
)

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print(
    "-----------------------------------------------   STEP EIGHT  -----------------------------------------------"
)
newRegister = np.array([17.89, 13.59, 107.89, 176.88, 56.78])
salesArray = np.vstack((salesArray, newRegister))
print("Updated array:", salesArray)

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print(
    "-----------------------------------------------   STEP NINE  -----------------------------------------------"
)
salesArray[2, 3] = 20.14
print("Updated array: ", salesArray)
