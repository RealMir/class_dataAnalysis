import pandas as pd
import numpy as np

df = pd.read_excel("stock.xlsx",index_col="No")

print(df["PER"]>10) # result is boolean
print(df[df["PER"]>10]) # result is table

# NOT condition
filt = df["PER"]>10
print(df[~filt])

# AND condition
filt = (df["PER"]>10) & (df["ROE"]>10) 
print(df[filt])

# OR condition
filt = ~(df["PER"]>10) | (df["ROE"]<10)
print(df[filt])

# STR condition
filt = df["종목명"].str.startswith("삼성")
print(df[filt])

filt = df["종목명"].str.contains("바이오")
print(df[filt])

langs = ["삼성전자","SK하이닉스"]
filt = df["종목명"].isin(langs)
print(df[filt])

df.iloc[0,0] = np.NaN # set "삼성전자" to NaN for na
filt = df["종목명"].str.contains("삼성", na=True) # set boolean of NaN to True
print(filt)
print(df[filt])