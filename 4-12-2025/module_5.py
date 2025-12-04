#exercise 1
import pandas as pd

df = pd.read_csv('Retail_dataset.csv')

total_orders = df['order_id'].nunique()

df['revenue'] = df['quantity'] * df['price']
total_revenue = df['revenue'].sum()

top_5_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)

print(f"Total Orders: {total_orders}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print("\nTop 5 Products by Quantity Sold:")
print(top_5_products)

#exercise 2
import pandas as pd

df = pd.read_csv('Retail_dataset.csv')
missing_values = df.isnull().sum()
print(f"Missing values in each column:\n{missing_values}")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
missing_values_after = df.isnull().sum()
print(f"\nMissing values after filling:\n{missing_values_after}")

#exercise 3
df['total_sales'] = df['quantity'] * df['price']
grouped_by_category = df.groupby('product_name').agg(
    total_sales=('total_sales', 'sum'),
    order_count=('order_id', 'nunique'),
    avg_price=('price', 'mean')
).reset_index()

print(grouped_by_category)

#exercise 4
df['discounted_price'] = df['price'] * 0.9
print(df[['product_name', 'price', 'discounted_price']].head())

#exercise 5
customers_df = pd.read_csv('customers.csv')
orders_df = pd.read_csv('orders.csv')
combined_df = pd.merge(orders_df, customers_df, on='customer_id', how='inner')
print(combined_df.head())

#exercise 6
import json
from pandas import json_normalize

with open('customers.json') as f:
    data = json.load(f)
normalized_df = json_normalize(data, sep='_')
print(normalized_df.head())

#exercise 7
df['total_spent'] = df['quantity'] * df['price']
customer_spend = df.groupby('customer_id')['total_spent'].sum()
high_spending_customers = customer_spend[customer_spend > 5000]
print(high_spending_customers)

#exercise 8
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
pivot_table = pd.pivot_table(df, values='total_sales', index='product_name', columns='month', aggfunc='sum', fill_value=0)
print(pivot_table)

#exercise 9
Q1 = df['quantity'].quantile(0.25)
Q3 = df['quantity'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_cleaned = df[(df['quantity'] >= lower_bound) & (df['quantity'] <= upper_bound)]
print(df_cleaned)

