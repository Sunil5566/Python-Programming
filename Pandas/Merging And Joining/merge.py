#pd.merge[df1, df2, on = "Column_NAme", how = "type of join"]
import pandas as pd

#customer-dataframe

df_customers = pd.DataFrame({
    'Customer_ID' : [1,2,3],
    'Name' : ["Ramesh", "Ganesh", "Prince"]
})

df_order = pd.DataFrame({
    "Customer_ID" : [1,2,4],
    "OrderAmount" : [250, 450, 350]
})

df_merge = pd.merge(df_customers, df_order, on="Customer_ID", how="inner")
print("inner join")
print(df_merge)