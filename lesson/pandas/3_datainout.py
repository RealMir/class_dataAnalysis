import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {}
def extract_date(info):
  for num, key in enumerate(keys):
      if key.get_text() not in data:
        data[key.get_text()]=[info[num].get_text().strip()]
      else:
        data[key.get_text()].append(info[num].get_text().strip())
        
response = requests.get("https://finance.naver.com/sise/sise_market_sum.naver")
response.raise_for_status()
soup = BeautifulSoup(response.text,"lxml")

keys = soup.find_all("th",attrs={"scope":"col"})
stocks = soup.find_all("td",attrs={"class":"no"})
for num,stock in enumerate(stocks):
  if num == 7:break
  extract_date(stock.parent.find_all("td"))

df = pd.DataFrame(data,columns=["종목명","현재가","등락률","외국인비율","거래량","PER","ROE"])
df.index.name = "No"

# save data at csv, txt, excel
df.to_csv("stock.csv",encoding="utf-8-sig",index=False) 
df.to_csv("stock.txt",sep="\t") 
df.to_excel("stock.xlsx") 

# read data from csv, txt, excel
df = pd.read_csv("stock.csv")
print(df)
df = pd.read_csv("stock.txt",sep="\t")
print(df)
df = pd.read_excel("stock.xlsx")
print(df)

# read options
df = pd.read_csv("stock.csv",nrows=5) # bring rows
print(df)
df = pd.read_csv("stock.csv",skiprows=2) # skip rows
print(df)
df = pd.read_csv("stock.csv",skiprows=[2,4],nrows=3)
print(df)
df = pd.read_csv("stock.csv",index_col="종목명") # setting index
print(df)