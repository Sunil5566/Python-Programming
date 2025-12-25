import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Hari'],
    "Age" : [10,20,30],
    "City" : ['Kathmandu', 'Pokhara', 'Butwal']
}
df = pd.DataFrame(data)
print(df)

# #Converting data to csv file
# df.to_csv("output.csv", index=False)

# #converting to excel file
# df.to_excel("output.xlsx", index=False)

# #converting to json file
# df.to_json("output.json", index = False)
