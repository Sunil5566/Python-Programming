#fillna method
#fillna(value, inplace = True)
import pandas as pd

data = {
    "Name" : ["Ram", None, "Gita", "Hari", "Muskan", "Sushil", "Dinesh","Babita"],
    "Age" : [10,None,30,40,50,60, 70,80],
    "Salary" : [5033,None,867543,5643,34657,900,75443,344],
    "Performance" : [22,None,67,89,8,76,4,33]
}

df = pd.DataFrame(data)

# df.fillna(0, inplace=True)  #it fill default value which is 0

#To fill calculated value: 
df["Age"].fillna(df["Age"].mean(), inplace=True)

print(df)