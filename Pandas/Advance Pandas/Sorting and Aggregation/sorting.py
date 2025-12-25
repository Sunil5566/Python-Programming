#Sorting data
import pandas as pd

data = {
    "Name" : ["Arjun", "Bibek", "Shyam"],
    "Age" : [30,42,21],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)

df.sort_values(by= ["Age", "Salary"], ascending= [False, True], inplace=True)
print(df)