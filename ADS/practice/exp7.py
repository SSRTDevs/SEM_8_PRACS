import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

df = pd.read_csv("../Iris.csv")
df = df.drop(["Id"], axis = 1)

# Boxplot
df.boxplot()
plt.show()

# Create Arrays
target_col = "Species"
X = df.drop([target_col], axis = 1).values

nearestNeighbors = NearestNeighbors(n_neighbors = 3)
nearestNeighbors.fit(X)

# distances and indexes of k-neaighbors from model outputs
distances, indexes = nearestNeighbors.kneighbors(X)

# plot mean of k-distances of each observation
plt.plot(distances.mean(axis = 1))
plt.show()

# visually determine cutoff values > 0.15
outlier_index = np.where(distances.mean(axis = 1) > 0.3)

# filter outlier values
outlier_values = df.iloc[outlier_index]
print(outlier_values)