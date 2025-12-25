"""
How big is your dataset  ...shape
what are the names of columns   ... column
"""
import pandas as pd


data = {
    "Name" : ["Ram", "Shyam", "Gita", "Hari", "Muskan", "Sushil", "Dinesh","Babita"],
    "Age" : [10,20,30,40,50,60, 70,80],
    "Salary" : [5033,355,867543,5643,34657,900,75443,344],
    "Performance" : [22,45,67,89,8,76,4,33]
}

df = pd.DataFrame(data)

print(f"Shape: {df.shape}")
print(f"Column Name: {df.columns}")