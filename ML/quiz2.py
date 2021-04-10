"""
MACHINE LEARNING SUPERVISED CLASSIFICATION MODEL
You are to apply skills you have acquired in Machine Learning 
to correctly predict the classification of a group of animals. 
The data has been divided into 3 files.
Classes.csv  download- is a file describing the class an animal 
belongs to as well as the name of the class. The class number 
and class type are the two values that are of most importance 
to you.
animals_train.csv  download - is the file you will use to train
 your model. There are 101 samples with 17 features. The last 
 feature is the class number (corresponds to the class number 
 from the classes file). This should be used as your target 
 attribute. However, we want the target attribute to be the 
 class type (Mammal, Bird, Reptile, etc.) instead of the class 
 number (1,2,3,etc.).
animals_test.csv  download- is the file you will use to test 
your model to see if it can correctly predict the class that
 each sample belongs to. The first column in this file has 
 the name of the animal (which is not in the training file). 
  Also, this file does not have a target attribute since the 
  model should predict the target class.
Your program should produce a csv file that shows the name 
of the animal and their corresponding class as shown in this 
file -predictions.csv 
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np

# LOAD FILES
animals_train = pd.read_csv("animals_train.csv")
animals_test = pd.read_csv("animals_test.csv")
animal_classes = pd.read_csv("animal_classes.csv")

# DEFINE TRAINER AND TEST
train_x = animals_train.iloc[:, 0:16]
train_y = animals_train["class_number"]
test_x = animals_test.iloc[:, 1:17]

"""
print(train_x)
print(train_y)
print(train_y.shape)
print(train_x.shape)
print(test_x.shape)
"""
# CREATE MODEL
regr = LinearRegression()
regr.fit(train_x, train_y)
y_pred = regr.predict(test_x)

# ROUND THE VALUES AND MAKE IT THE RIGHT TYPE
y_pred2 = np.rint(y_pred)
print(y_pred)
int_array = y_pred2.astype(int)
print(int_array)

# CREATE LIST OF PREDICTIONS
type1 = []
for x in int_array:
    type1.append(animal_classes.iloc[x - 1]["Class_Type"])

# CREATE SERIES OF NAMES
names = animals_test.iloc[:, 0]

# WRITE TO  THE FILE
outfile = open("predictions2.csv", "w")
outfile.write("animal_name, prediction")
for i in range(36):
    outfile.write(names.iloc[i])
    outfile.write(", ")
    outfile.write(type1[i])
    outfile.write("\n")
outfile.close()
