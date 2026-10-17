import pandas as pd

df = pd.read_csv("Task1_Data_Cleaning/Titanic.csv")

print(df.head())

print(df.shape)
print(df.info())
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print(df.dtypes)
df["Age"] = df["Age"].fillna(df["Age"].median())
print("Missing Age values:", df["Age"].isnull().sum())
df=df.drop("Cabin",axis=1)
print("Cabin column removed.")
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Missing Embarked values:", df["Embarked"].isnull().sum())
print("Missing values after cleaning:")
print(df.isnull().sum())
df.to_csv("Task1_Data_Cleaning/Titanic_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")