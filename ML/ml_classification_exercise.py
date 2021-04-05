# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features.
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris
# virginica. Each sample’s features are the sepal length, sepal width, petal
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower
# that protect the smaller inside petals before the flower buds bloom.

# EXERCISE
# load the iris dataset and use classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

iris_data = load_iris()
# print(data.DESCR)

# to see if the expected and predicted species
# match up
data_train, data_test, target_train, target_test = train_test_split(
    iris_data.data, iris_data.target, random_state=11
)
print(data_train.shape)
print(target_train.shape)
print(data_test.shape)

knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train)
# returns array containing predicted class of each test image

predicted = knn.predict(X=data_test)
pred_names = []
for i in predicted:
    if i == 0:
        pred_names.append("setosa")
    if i == 1:
        pred_names.append("versicolor")
    if i == 2:
        pred_names.append("virginica")

# give target value for data set

expected = target_test
exp_names = []
for i in expected:
    if i == 0:
        exp_names.append("setosa")
    if i == 1:
        exp_names.append("versicolor")
    if i == 2:
        exp_names.append("virginica")

print(pred_names[:10])
print(exp_names[:10])


# display the shape of the data, target and target_names
print(iris_data.data.shape)
print(iris_data.target.shape)
print(iris_data.target_names.shape)

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)
print(predicted[:10])
print(expected[:10])

# display the values that the model got wrong
wrong = [(p, e) for (p, e) in zip(pred_names, exp_names) if p != e]
# prints expected vs what we actually got that's wrong (9,8)
print(wrong)
# visualize the data using the confusion matrix

confusion = confusion_matrix(y_true=exp_names, y_pred=pred_names)
print(confusion)
confusion_df = pd.DataFrame(confusion, index=range(3), columns=range(3))
figure = plt2.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.show()

print("done")