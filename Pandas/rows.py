import pandas as pd

# head and tail 2 methods to look rows

# head(n)- first n row it shows
#tail(n)- last n rows display else shoes 5 default value

df = pd.read_json(r"Pandas\sample_Data.json")

print("Display 10 rows of first")
print(df.head(10))

print("Display 10 rows of last")
print(df.tail(10))