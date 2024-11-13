import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('train1.csv')
df.head()

df.info()
df.describe()

df.isnull().sum()
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

numerical_cols = df.select_dtypes(include=np.number).columns

for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lowerBound = Q1 - 1.5 * IQR
    upperBound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lowerBound) | (df[col] > upperBound)]
    if not outliers.empty:
        print(f"Outliers in '{col}': ")
        print(outliers[[col]])
        print("\n")

scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
df.head()

df = pd.get_dummies(df, columns=['Sex', 'Embarked'], dtype=int)
df.head()

df.to_csv('modified_titanic_dataset.csv', index=False)
