import pandas as pd

# Read data from csv file into a dataframe

#To read csv file
df = pd.read_csv("wepass here path", encoding="latin1") #encoding also can be utf-8 like this

#To read excel file
df = pd.read_excel("path")

#To read json file
df = pd.read_json("path")

print(df)


#google cloud storage can be read by using gcsfs library


