import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../Iris.csv")
df = df.drop(["Id"], axis = 1)
target_col = "Species"
le = LabelEncoder()
df[target_col] = le.fit_transform(df[target_col])

y = df[[target_col]]
X = df.drop([target_col], axis = 1)

print(X.head(5))
print(y.head(5))

kmeans = KMeans(n_clusters = 3, random_state=1).fit(X)
y_kmeans = kmeans.fit_predict(y)

# #Intrinsic Method
# silhouette_score(X, y_kmeans, metric = 'euclidean')

# #Adjusted Rand Index
# adjusted_rand_score(y, y_kmeans)

# #Mutual Information
# normalized_mutual_info_score(y, y_kmeans)

# # Scatter Plot
# plt.scatter(X[y_kmeans == 0, 1] , X[y_kmeans == 0, 2], label='Iris-setosa')
# plt.scatter(X[y_kmeans == 1, 1] , X[y_kmeans == 1, 2], label='Iris-versicolour')
# plt.scatter(X[y_kmeans == 2, 1] , X[y_kmeans == 2, 2], label='Iris-virginica')
# plt.show()