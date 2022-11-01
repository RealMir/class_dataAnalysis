import pandas as pd

df = pd.read_excel("stock.xlsx",index_col="No")

# sort index
print(df.sort_index(ascending=False)) # True : ascend / False : descand
print(df.sort_index(axis=1)) # 0 : index / 1 : columns

# sort value
print(df["ROE"].sort_values(ascending=False))
print(df.sort_values("ROE", ascending=False))
print(df.sort_values(["ROE","PER"],ascending=[True,False]))
# 처음 정렬 이후 같은 값 중에서만 다음 컬럼 정렬 의해 순서 변함