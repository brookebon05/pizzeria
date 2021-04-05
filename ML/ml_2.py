import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

nyc = pd.read_csv("ave_hi_nyc_jan_1895-2018.csv")
print(nyc.head(2))  # shows top 2 rows
# One column is a series

print(nyc.Date.values)
print(nyc.Date.values.reshape(-1, 1))  # Makes first column one row

print(nyc.Temperature.values)

X_train, X_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11
)
print(X_train.shape)  # data
print(X_test.shape)  # data
print(y_train.shape)  # target
print(y_test.shape)  # target


linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)
print(linear_regression.coef_)
print(linear_regression.intercept_)

predicted = linear_regression.predict(X_test)
expected = y_test

for p, e in zip(
    predicted[::5], expected[::5]
):  # double colons say print every 5th element
    print(f"Predicted: {p:.2f}, expected: {e:.2f}")

# lambda implements y = mx + b
predict = lambda x: linear_regression.coef_ * x + linear_regression.intercept_

print(predict(2021))
print(predict(1899))

axes = sns.scatterplot(
    data=nyc,
    x="Date",
    y="Temperature",
    hue="Temperature",
    palette="winter",
    legend=False,
)

axes.set_ylim(10, 70)  # scale y-axis
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
print(x)
y = predict(x)
print(y)

line = plt.plot(x, y)
plt.show()