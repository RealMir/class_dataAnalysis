import pandas as pd

df = pd.read_excel("stock.xlsx",index_col="No")

""" basic select """
# select by name of column
print(df["종목명"]) #same
print(df.종목명) #same
print(df[["종목명", "현재가", "PER"]])

# select by index of column
print(df.columns[0])
print(df[df.columns[0]])
print(df[df.columns[[0,2]]])
print(df[df.columns[0:2]])

# select by slicing
print(df["종목명"][3])
print(df["종목명"][[0,3]])
print(df["종목명"][0:3])
print(df[:3]) # print(df[3]) is error because '3' is recognized by column not index
changed_df = pd.read_excel("stock.xlsx",index_col="종목명") # change index
print(changed_df[:"SK하이닉스"]) #same
print(changed_df[:df["종목명"][3]]) #same



""" loc select """
# think like coordinates 
# x is name of index, y is name of column
print(df.loc[0])
print(df.loc[0,"종목명"])
print(df.loc[[0,2],["종목명","현재가"]])
print(df.loc[0:2,"종목명":"현재가"])
# when use slicing at loc, the back number is included ,unlike general method



""" iloc select """
# same like coordinates
# x is number of index, y is number of column
print(df.iloc[0])
print(df.iloc[0,0])
print(df.iloc[[0,2],[0,1]])
print(df.iloc[0:2,0:1])