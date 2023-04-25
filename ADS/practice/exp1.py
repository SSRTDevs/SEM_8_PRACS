import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../diamonds.csv")

# print(df.head(5))

df = df.drop('Unnamed: 0', axis = 1)

print(df.describe())
print(df['price'].median())
print(df['price'].max())
print(df['price'].min())

df_numerics_only = df.select_dtypes(include = np.number)
print(df_numerics_only.head(5))

corr = df_numerics_only.corr()
sns.heatmap(corr, cmap="Blues", annot=True)
plt.show()

graph = sns.distplot(df['depth'])
plt.show()

plt.scatter(df['carat'] , df['price'])
plt.show()

plt.boxplot(df['table'])
plt.show()

print('-No. of missing values-')
print(df.isnull().sum())