#Using drop method

import pandas as pd

data = {
    "Name" : ["Ram", "Shyam", "Gita", "Hari", "Muskan", "Sushil", "Dinesh","Babita"],
    "Age" : [10,20,30,40,50,60, 70,80],
    "Salary" : [5033,355,867543,5643,34657,900,75443,344],
    "Performance" : [22,45,67,89,8,76,4,33]
}

df = pd.DataFrame(data)

#Removing

#df.drop(columns = ["Column Name"], inplace = True)

print("Modified dataset")

df.drop(columns= ["Performance", "Age"], inplace= True)
print(df)
