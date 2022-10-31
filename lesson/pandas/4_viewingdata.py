import pandas as pd

df = pd.read_excel("stock.xlsx",index_col="No")

print(f"Shape : {df.shape}")
print(f"Index : {df.index}")
print(f"Columns : {df.columns}")

print(f"checking top of data\n{df.head(3)}") 
print(f"checking bottom of data\n{df.tail(1)}")

# show data info
print(df.info())
print(df.describe())

print(df["PER"].count())
print(df["PER"].unique())
print(df["PER"].nunique())
print(df["PER"].mean())
print(df["PER"].sum())
print(df["PER"].max())
print(df["PER"].min())
print(df["PER"].nlargest(3))