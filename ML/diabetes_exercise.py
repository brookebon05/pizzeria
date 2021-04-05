""" Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line """

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
# how many sameples and How many features?
print(diabetes.data.shape)  # 442 samples, 10 features


# What does feature s6 represent?
print(diabetes.DESCR)  # glu, blood sugar level


# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
# diabetes.data, diabetes.target
# print out the intercept

# expected = y_test
# plt.plot(eexpected, predicted, ".")
# create a scatterplot with regression line

# Create linear regression object
regr = LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# print out the intercept
# The coefficients
print("Coefficients: \n", regr.coef_)
print("intercepts: \n", regr.intercept_)


# Plot outputs

plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

# create a scatterplot with regression line
