# Pandas의 주요 Object에는 Series와 DataFrame
# Series는 1차원 데이터
# DataFrame은 2차원 데이터 (Series들의 모음)

import pandas as pd

s = pd.Series(["10","-20","30"])
print(s)
print(s[1])
print(s[[0,2]])
print(s[0:2])

s2 = pd.Series([10,-20,30],index=["A","B","C"])
print(s2)
print(s2["B"])
print(s2[["A","C"]])
print(s2["A":"C"])

data = {
  "종목명":["삼성전자","LG에너지솔루션","삼성바이오로직스","SK하이닉스","삼성SDI","LG화학","삼성전자우"],
  "현재가":[57300,532000,876000,83400,727000,615000,51500],
  "PER":[8.69,883.72,116.50,5.29,33.91,21.68,7.81],
  "ROE":[13.92,10.68,8.21,16.84,51.07,18.47,'']
}

df = pd.DataFrame(data)
print(df)
print(df[["종목명","PER"]])

df2 = pd.DataFrame(data, index=["A","B","C","D","E","F","G"])
print(df2)

df3 = pd.DataFrame(data,columns=["종목명","PER"])
print(df3)