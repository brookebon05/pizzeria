import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

nyc2 = pd.read_csv("ave_yearly_temp_nyc_1895-2017.csv")
# One column is a series

X_train, X_test, y_train, y_test = train_test_split(
    nyc2.Date.values.reshape(-1, 1), nyc2.Value.values, random_state=11
)

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

axes = sns.scatterplot(
    data=nyc2,
    x="Date",
    y="Value",
    hue="Value",
    palette="winter",
    legend=False,
)

axes.set_ylim(10, 70)  # scale y-axis
x = np.array([min(nyc2.Date.values), max(nyc2.Date.values)])
print(x)
y = predict(x)
print(y)

line = plt.plot(x, y)
plt.show()