import pandas as pd
df=pd.read_csv("store.csv")

#A
print(df.head(10))
print("shape of the dataframe:",df.shape)
print("Data types of each column:", df.dtypes)
print("Columns containing missing values:", df.isnull().sum())



#B
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')  # 'coerce' will turn invalid dates into NaT
df['ShipDate'] = pd.to_datetime(df['ShipDate'], errors='coerce')


df['ShippingDays'] = (df['ShipDate'] - df['OrderDate']).dt.days


df['ProfitMargin'] = df['Profit'] / df['Sales']
df['CustomerName'] = df['CustomerName'].str.title()

df = df[df['Sales'] > 0]


df['Discount'] = df['Discount'] * 100
print(df.head())

#C
west_orders = df[df['Region'] == 'West']
print(west_orders)

technology_sales_above_400 = df[(df['Category'] == 'Technology') & (df['Sales'] > 400)]
print(technology_sales_above_400)

returned_products = df[df['Returned'] == 'Yes']
print(returned_products)

df['ShipDate'] = pd.to_datetime(df['ShipDate'])  # Ensure ShipDate is datetime
furniture_after_2024_01_20 = df[(df['Category'] == 'Furniture') & (df['ShipDate'] > '2024-01-20')]
print(furniture_after_2024_01_20)

low_profit_orders = df[df['Profit'] < 20]
print(low_profit_orders)

#D
sales_descending = df.sort_values(by='Sales', ascending=False)
print(sales_descending)

profit_margin_sorted = df.sort_values(by='ProfitMargin', ascending=False)
print(profit_margin_sorted)


region_city_sorted = df.sort_values(by=['Region', 'City'], ascending=[True, True])
print(region_city_sorted)


shipping_days_sorted = df.sort_values(by='ShippingDays', ascending=False)
print(shipping_days_sorted)

customer_name_sorted = df.sort_values(by='CustomerName', ascending=True)
print(customer_name_sorted)

#E
total_sales_per_region = df.groupby('Region')['Sales'].sum().reset_index()
print("Total Sales per Region:")
print(total_sales_per_region)

average_profit_per_category = df.groupby('Category')['Profit'].mean().reset_index()
print("\nAverage Profit per Category:")
print(average_profit_per_category)


orders_per_customer = df.groupby('CustomerID').size().reset_index(name='OrderCount')
print("\nCount of orders per Customer:")
print(orders_per_customer)

sum_sales_per_segment = df.groupby('Segment')['Sales'].sum().reset_index()
print("\nSum of Sales per Segment:")

total_quantity_per_subcategory = df.groupby('SubCategory')['Quantity'].sum().reset_index()
print("\nTotal Quantity sold per SubCategory:")
print(total_quantity_per_subcategory)

mean_shipping_days_per_category = df.groupby('Category')['ShippingDays'].mean().reset_index()
print("\nMean ShippingDays grouped by Category:")
print(mean_shipping_days_per_category)


