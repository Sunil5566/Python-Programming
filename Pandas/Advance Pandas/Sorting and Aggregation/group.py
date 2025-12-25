import pandas as pd

data = {
    "Name" : ["Arjun", "Bibek", "Shyam", "Samu", "Hari"],
    "Age" : [30,42,21,33,67],
    "Salary" : [10000,20000,30000,45000,5432]
}

df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)