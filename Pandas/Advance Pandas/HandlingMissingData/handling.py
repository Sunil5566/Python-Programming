#deopna
import pandas as pd

data = {
    "Name" : ["Ram", None, "Gita", "Hari", "Muskan", "Sushil", "Dinesh","Babita"],
    "Age" : [10,None,30,40,50,60, 70,80],
    "Salary" : [5033,None,867543,5643,34657,900,75443,344],
    "Performance" : [22,None,67,89,8,76,4,33]
}

df = pd.DataFrame(data)
df.dropna(axis = 0, inplace = True)  # axis 0 row , axis 1 column
print(df)