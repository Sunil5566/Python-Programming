import pandas as pd

data = {
    "Name" : ["Ram", "Shyam", "Gita", "Hari", "Muskan", "Sushil", "Dinesh","Babita"],
    "Age" : [10,20,30,40,50,60, 70,80],
    "Salary" : [5033,355,867543,5643,34657,900,75443,344],
    "Performance" : [22,45,67,89,8,76,4,33]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"]  > 50000]
print(high_salary)

#filtering roes salary more than 50k and age more than 30

filtered = df[(df["Age"] > 30) & (df["Salary"] > 5000)]
print(filtered)

#using or condition
Filtered_or  = df[(df["Age"] > 30) & (df["Salary"] > 5000)]
print(Filtered_or)