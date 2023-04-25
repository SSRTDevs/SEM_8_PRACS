import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

df = pd.read_csv('../Churn_Modelling.csv')

for col in df.columns:
    if df[col].dtypes == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

X = df.drop('Exited', axis = 1)
y = df['Exited']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 100)

cls = DecisionTreeClassifier()
cls.fit(X_train, y_train)

y_pred = cls.predict(X_test)

print(classification_report(y_test, y_pred))

# SMOTE 
smote = SMOTE(sampling_strategy = 'auto', k_neighbors = 5, random_state = 100)
X_oversample, y_oversample = smote.fit_resample(X_train, y_train)

cls.fit(X_oversample, y_oversample)

y_pred = cls.predict(X_test)

print(classification_report(y_test, y_pred))




data = df[['CreditScore', 'Age', 'Exited',]]
sns.scatterplot(data = data, x ='CreditScore', y = 'Age', hue = 'Exited')
plt.show()

smote = SMOTE(random_state = 100)

X,y = smote.fit_resample(df[['CreditScore', 'Age']], df['Exited'])

df_oversample = pd.DataFrame(X, columns = ['CreditScore', 'Age'])
df_oversample['Exited'] = y

sns.scatterplot(data = df_oversample, x = 'CreditScore', y = 'Age', hue = 'Exited')
plt.show()

sns.countplot(data = df_oversample, x = 'Exited')
plt.show()