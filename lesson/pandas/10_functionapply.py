import pandas as pd

df = pd.read_excel("stock.xlsx",index_col="No")

def convert_num(value):
  return int(value.replace(",",""))
    
print(df.info())

df.현재가 = df.현재가.apply(convert_num)
df.거래량 = df.거래량.apply(convert_num)

print(df.info())

def compare_rate(roe):
  interest_rate = 10
  if pd.notnull(roe):
    profit = roe-interest_rate 
    if profit>0:
      return str(roe)+ "=> 이득"
    else:
      return str(roe)+ "=> 손해"
  else: return roe

# when interest rate is 10, print actual profit utilizing roe    
df.ROE = df.ROE.apply(compare_rate)
print(f"기준금리가 10일때\n {df.ROE}")