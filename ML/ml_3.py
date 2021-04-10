from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt2


california = fetch_california_housing()  # Bunch object
# print(california.DESCR)
print(california.data.shape)
print(california.target_names)  # target is one dimensional, only one target value
print(california.feature_names)

pd.set_option("precision", 4)
pd.set_option("max_columns", 9)
pd.set_option("display.width", None)  # autodetect width for wrapping

california_df = pd.DataFrame(california.data, columns=california.feature_names)
california_df["MedHouseValue"] = pd.Series(california.target)
# print(california_df.head())  # cap for 500k or below just FYI

sample_df = california_df.sample(frac=0.1, random_state=17)
sns.set(font_scale=2)
sns.set_style("whitegrid")

for feature in california.feature_names:
    plt.figure(figsize=(8, 4.5))
    sns.scatterplot(
        data=sample_df,
        x=feature,
        y="MedHouseValue",
        hue="MedHouseValue",
        palette="cool",
        legend=False,
    )

# plt.show()

# TRAIN MODEL
data_train, data_test, target_train, target_test = train_test_split(
    california.data, california.target, random_state=11
)

print(data_train.shape)
print(target_train.shape)
print(data_test.shape)
print(target_test.shape)

linear_regression = LinearRegression()
linear_regression.fit(X=data_train, y=target_train)
print(linear_regression.coef_)
print(linear_regression.intercept_)

for i, name in enumerate(california.feature_names):
    print(f"{name}: {linear_regression.coef_[i]}")

# positive correlation? positive, feature goes up as y-value increases
predicted = linear_regression.predict(data_test)
print(predicted[:5])
expected = target_test
print(expected[:5])
"""
for p, e in zip(
    predicted[::5], expected[::5]
):  # double colons say print every 5th element
    print(f"Predicted: {p:.2f}, expected: {e:.2f}")
"""
df = pd.DataFrame()
df["Expected"] = pd.Series(expected)
df["Predicted"] = pd.Series(predicted)
print(df[:10])

predict = lambda x: linear_regression.coef_ * x + linear_regression.intercept_
# BOTH DATA AND SOMETHING ELSE MUST BE CATEGORICAL

figure = plt2.figure(figsize=(9, 9))
axes = sns.scatterplot(
    data=df,
    x="Expected",
    y="Predicted",
    hue="Predicted",
    palette="cool",
    legend=False,
)

start = min(expected.min(), predicted.min())
print(start)
end = max(expected.min(), predicted.min())
print(end)
axes.set_xlim(start, end)
axes.set_ylim(start, end)  # scale y-axis
line = plt2.plot([start, end], [start, end], "k--")
plt2.show()

"""
# scale y-axis
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
print(x)
y = predict(x)
print(y)
"""
