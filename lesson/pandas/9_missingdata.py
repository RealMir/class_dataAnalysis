import pandas as pd
import numpy as np

df = pd.read_excel("stock.xlsx",index_col="No")

df.현재가 = np.nan
print(df.isna()) # check the value of nan

df.현재가.fillna("없음",inplace=True) # add value at nan of 현재가
print(df)

df.fillna("없음",inplace=True) 
print(df)

df = pd.read_excel("stock.xlsx",index_col="No")

df.현재가 = np.nan

# delete nan
# axis : index or columns
# how : any or all
df.dropna(axis="columns", how="all", inplace=True)
print(df)

df.dropna(axis="index",how="any",inplace=True)
print(df)
