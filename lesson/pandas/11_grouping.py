import pandas as pd

df = pd.read_excel("stock.xlsx",index_col="No")
df["계열사"] = df.종목명.str[0:2]
df["액면가"] = [100,500,5000,2500,5000,5000,100]

grouping = df.groupby("계열사")
print(grouping.size())
print(grouping.count())

print(grouping.mean()) # mean in all parts 
print(grouping["PER","ROE","액면가"].max()) # max in column section
select = grouping.get_group("삼성")
print(select)
print(select.min()) # min in index section

print(grouping["액면가"].max().sort_values(ascending=False))

# 1.계열사group 2.액면가gorup
grouping2 = df.groupby(["계열사","액면가"])
print(grouping2.size())
print(grouping2.count())

print(grouping2.mean())
print(grouping2["PER","ROE","액면가"].max())
select2 = grouping2.get_group(("삼성",100)) # tuple
print(select2)
print(select2.min())

print(grouping2["PER"].max().sort_values(ascending=False))