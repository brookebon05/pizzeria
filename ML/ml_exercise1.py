from sklearn.datasets import fetch_california_housing
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# FETCH DATA
california = fetch_california_housing()
california_df = pd.DataFrame(california.data, columns=california.feature_names)

# GRAPH
g = sns.pairplot(california_df)
plt.show()
