import pandas as pd

df = pd.read_csv(r"DataHandlingPractice\data.csv")
print(df)


print("\n Missing data")
missing_data = df.isnull().sum()
print(missing_data)

print("\nFilling data")

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Gender'].fillna(method = 'ffill', inplace= True)
df["Email"] = df.apply(
    lambda row: f"{row['Name'].lower()}@example.com" if pd.isna(row['Email']) else row['Email'], axis = 1

)
df['JoinDate'].fillna(pd.to_datetime(df['JoinDate']).median(), inplace = True)
print(df)

df["TotalPurchase"].fillna(df['TotalPurchase'].mean(), inplace=True)
df['LastPurchaseDate'].fillna(pd.to_datetime(df['LastPurchaseDate']).median(), inplace=True)

df['City'].fillna(df['City'].mode()[0], inplace=True)


print("\n Missing data")
missing_data = df.isnull().sum()
print(missing_data)
