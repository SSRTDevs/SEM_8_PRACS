import pandas as pd
import numpy as np

df = pd.read_csv("../loan_data_set.csv")

# freq/mode imputation
# for col in df.columns:
#     df[col] = df[col].fillna(df[col].mode()[0])

# mean/median imputation
# num_cols = df.select_dtypes(exclude='object').columns

# for col in num_cols:
    # df[col] = df[col].fillna(df[col].mean())

# Removing missing data
# remove_na_rows = df.dropna(axis = 0)

# Random imputation
# df_imputed = df.copy()
# col = 'Education'
# non_missing_education = df[col][df[col].notnull()]
# imputed_education = np.random.choice(non_missing_education, size=df_imputed[col].isnull().sum())
# df_imputed.loc[df_imputed[col].isnull(), col] = imputed_education