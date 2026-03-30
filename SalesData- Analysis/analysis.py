import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")
print(df.head())

print(df.isnull().sum())   # check nulls

df.drop_duplicates(inplace=True)
print("Total Sales:", df["Sales"].sum())

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
print(top_products)

region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.savefig("sales_by_region.png")
plt.show()


top_products.plot(kind='bar')
plt.title("Top 5 Products")
plt.savefig("top_products.png")
plt.show()
