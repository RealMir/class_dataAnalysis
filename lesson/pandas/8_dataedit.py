import pandas as pd

df = pd.read_excel("stock.xlsx",index_col="No")

""" delete row """
print(df.drop(index=1))
print(df) # delted data not applied
filt = df["PER"] > 100 # high evaluation filtering
df.drop(index=df[filt].index, inplace=True)
print(df)

""" add row """
df.loc[7] = ["현대차","163,000","+0.62%",28.99,"515,337",7.23,6.84]
print(df.tail(1))

""" edit value of cell """
df.loc[0,["현재가","PER"]] = ["59,400",9.01]
df.iloc[1,[1,5]] = ["84,500",5.36]
print(df.head(2))

""" edit column """
df["현재가"] = df["현재가"].str.replace(",","") # delete comma
df["현재가"] = pd.to_numeric(df["현재가"]) # data type changed from object to int64
print(df.현재가.info())
df["거래량"] = df["거래량"]+"주"
print(df)

""" add column """
df["BPS"] = [46937,97019,232283,399121,46937,312476]
df["PBR"] = df.현재가 / df.BPS
filt = df["PBR"]<1
df.loc[filt, "평가"] = "저평가"
df.loc[~(filt), "평가"] = "고평가"
print(df)

""" delte column """
df.drop(columns=["거래량","BPS"],inplace=True)
print(df)

""" edit name of column """
df.rename(columns={"평가":"result"},inplace=True)
print(df.columns)

""" edit column order """
col = list(df.columns)
print(df[[col[-1]]+col[:-1]])