import pandas as pd
df = pd.DataFrame({
    "OrderID":[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020],
    "Date":["2024-01-05","2024-01-05","2024-01-06","2024-01-06","2024-01-07","2024-01-07","2024-01-08","2024-01-08","2024-01-09","2024-01-09","2024-01-10","2024-01-10","2024-01-11","2024-01-11","2024-01-12","2024-01-12","2024-01-12","2024-01-13","2024-01-13","2024-01-13"],
    "Store":["Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B"],
    "City":["Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi"],
    "Product":["Laptop","Shampoo","Jeans","Smartphone","Bread","T-Shirt","Milk","Perfume","Headphones","Rice","Shoes","Milk","Charger","Notebook","Smartwatch","Biscuits","Jacket","Soap","Keyboard","Shirt"],
    "Category":["Electronics","Personal Care","Apparel","Electronics","Grocery","Apparel","Grocery","Personal Care","Electronics","Grocery","Apparel","Grocery","Electronics","Stationery","Electronics","Grocery","Apparel","Personal Care","Electronics","Apparel"],
    "Quantity":[1,3,2,1,5,4,10,1,2,3,1,12,2,10,1,6,1,4,1,2],
    "UnitPrice":[55000,120,1500,25000,40,800,50,2500,1500,90,3000,48,600,35,8000,25,4500,45,1200,1100],
    "TotalPrice":[55000,360,3000,25000,200,3200,500,2500,3000,270,3000,576,1200,350,8000,150,4500,180,1200,2200],
    "PaymentMethod":["Credit Card","Cash","Credit Card","UPI","Cash","Credit Card","UPI","Credit Card","Cash","Credit Card","UPI","Cash","Credit Card","Cash","UPI","Credit Card","UPI","Cash","UPI","Credit Card"],
    "CustomerType":["New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning"]
})
print(df)
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())


print("\nColumn names:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)
#2
df["Date"] = pd.to_datetime(df["Date"])


df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day


print(df.head())

#total sales
print("Total Sales by Store:")
print(total_sales_by_store)

print("\nTotal Sales by City:")
print(total_sales_by_city)

print("\nTotal Sales by Category:")
print(total_sales_by_category)
#top 5 highest value
top_5_orders = df.sort_values(by='TotalPrice', ascending=False).head(5)
print(top_5_orders[['OrderID', 'Store', 'City', 'Product', 'TotalPrice']])
# quantity >1
electronics_filtered = df[(df['Category'] == 'Electronics') & (df['Quantity'] > 1)]
print(electronics_filtered[['OrderID', 'Store', 'City', 'Product', 'Quantity', 'TotalPrice']])

#add new coloumn
df['Discount'] = df['CustomerType'].apply(lambda x: 0.10 if x == 'Returning' else 0.05)
df['FinalPrice'] = df['TotalPrice'] * (1 - df['Discount'])
print(df[['OrderID', 'Store', 'City', 'Product', 'CustomerType', 'TotalPrice', 'Discount', 'FinalPrice']])

#find how many orders were paid
payment_method_counts = df['PaymentMethod'].value_counts()
print(payment_method_counts)

#group by catagory and compute
category_sales = df.groupby('Category').agg(
    TotalQuantitySold=('Quantity', 'sum'),
    TotalRevenue=('TotalPrice', 'sum')
).reset_index()
print(category_sales)
#Identify the store with the highest total sales.
store_sales = df.groupby('Store')['TotalPrice'].sum()
highest_sales_store = store_sales.idxmax()
highest_sales_value = store_sales.max()
print(f"The store with the highest total sales is {highest_sales_store} with total sales of {highest_sales_value}.")
#Filter rows where Product name contains the letter “a” or “A”.
df = pd.read_csv(StringIO(data))
filtered_df = df[df['Product'].str.contains('a', case=False, na=False)]

print(filtered_df)

#Sort the dataset by Date and then by TotalPrice.
sorted_df = df.sort_values(by=['Date', 'TotalPrice'], ascending=[True, False])
print(sorted_df.tail())

# avg revenue
avg_revenue_per_customer_type = df.groupby('CustomerType')['TotalPrice'].mean().reset_index()
print(avg_revenue_per_customer_type)

#pivot tables
pivot_table = pd.pivot_table(df,
                             values='TotalPrice',
                             index='Category',
                             columns='PaymentMethod',
                             aggfunc='sum',
                             fill_value=0)

print(pivot_table)

