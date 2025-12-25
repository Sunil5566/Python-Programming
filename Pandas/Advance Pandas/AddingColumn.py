import pandas as pd

data = {
    "Name" : ["Ram", "Shyam", "Gita", "Hari", "Muskan", "Sushil", "Dinesh","Babita"],
    "Age" : [10,20,30,40,50,60, 70,80],
    "Salary" : [5033,355,867543,5643,34657,900,75443,344],
    "Performance" : [22,45,67,89,8,76,4,33]
}

df = pd.DataFrame(data)

#Adding column: square brackets df["Column Name"] = some_Data

print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

#Using insert method
#df.insert(location, "Column namee", data)

print("New Data Frame")

df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])
print(df)

