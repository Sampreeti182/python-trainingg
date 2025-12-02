import pandas as pd
df=pd.read_csv("data.csv")
#print(df.head())

#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

df["Date"]=pd.to_datetime(df["Date"])
print(df.info())
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day
print(df)

high_elec=df[(df["Category"]=="Electronics") & (df["TotalPrice"]>10000)]
print(high_elec)
sorted_df=df.sort_values("TotalPrice",ascending=False)
catagory_sales=df.groupby("Category")["TotalPrice"].sum()
print(catagory_sales)

store_avg=df.groupby("Store")["TotalPrice"].mean()
print(store_avg)

city_orders=df.groupby("City")["TotalPrice"].count()
print(city_orders)

#3
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day

customers=pd.DataFrame({
    "CustomerType": ["New","Returning"],
    "Discount":[5,10]
})
merged=df.merge(customers,"left","CustomerType")
print(merged)
