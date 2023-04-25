# encoding_dict = {index: label for index, label in enumerate(le.classes_)}

import math
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../Churn_Modelling.csv")

for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

target_col = "Exited"
X = df.drop(target_col, axis = 1)
y = df[[target_col]]

X_train, X_test, y_train, y_test = train_test_split(X, y)

decisionTree = DecisionTreeClassifier()
decisionTree.fit(X_train, y_train)

y_pred = decisionTree.predict(X_test)

# # Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
# sns.heatmap(cm, annot=True)
# plt.show()

# Accuracy
accu = (tn + tp)/(tn + tp + fp + fn)

# Error Rate
err = (fn + fp)/(tn + tp + fp + fn)

# Precision
pr = tp/(tp + fp)

# Sensitivity
sn = tp/(tp + fn)

# Specifity
sp = tn/(tn + fp)

# ROC
roc = math.sqrt( (sn**2) + (sp**2)/ 2)

# MSE
y_test = np.array(y_test)
y_pred = np.array(y_pred)
mse = np.sum((y_test - y_pred)**2) / np.size(y_test)

# RMSE
rmse = math.sqrt(mse)

# MAE
mae = np.sum(abs(y_test-y_pred)) / np.size(y_test)

# fnr
fnr = 1 - sn

# fpr
fpr = 1- sp

# F1 Score
f1_score = (2 * pr * sn)/(pr + sn)

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=0)
auc_score = roc_auc_score(y_test, y_pred)

plt.plot(fpr, tpr, label="AUC"+str(auc_score))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

