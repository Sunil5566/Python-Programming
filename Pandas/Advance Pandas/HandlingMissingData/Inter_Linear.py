import pandas as pd

data = {
    "Time" : [1,2,3,4,5],
    "Value" : [10,None,30,40,None]
}

df = pd.DataFrame(data)
print("Before interpolation: ")
print(df)

print("After Interpolation: ")
df["Value"] = df["Value"].interpolate(method="linear")
print(df)