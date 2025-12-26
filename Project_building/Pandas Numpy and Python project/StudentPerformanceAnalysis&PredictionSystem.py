import numpy as np
import pandas as pd

df = pd.read_csv(r"Project_building\Pandas Numpy and Python project\student_dataset.csv")
print("Original Data Frame")
print(df)

numeric_cols = df.select_dtypes(include=np.number).columns
print(numeric_cols)

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

for col in ["Math","Physics", "Chemistry", "English"]:
    df = df[(df[col] >=0) & (df[col] <=100)]

df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]


df.dropna(how='all', inplace = True)

print(df)
df.to_csv("student_dataset_cleaned.csv", index=False)


#Total marks per student
df["Total"] = df[["Math","Physics","Chemistry","English"]].sum(axis=1)
print(df["Total"])

#Average marks per student
df["Average"] = df[["Math", "Physics", "Chemistry", "English"]].mean(axis=1)
print(df["Average"])

#Average pre subject
df["Average_sub"] = df[["Math", "Physics", "Chemistry", "English"]].mean()
print(df["Average_sub"])
