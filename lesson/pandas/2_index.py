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
print(f"Original Data\n{df}\n")

# index : 데이터에 접근할 수 있는 주소 값
print("Index of data: {}\n" .format(df.index))

df.index.name = "No"
print(f"Setting index name\n{df}\n")

df.reset_index(drop=True)
print(f"Remove index name\n {df.reset_index(drop=True)} \n") # 실제 데이터에는 적용이 안됨
df.reset_index(drop=True,inplace=True)
print(f"Remove index name\n {df} \n") # inplace에 의해 실제 데이터에 적용됨

df.set_index("종목명",inplace=True)
print(f"Setting index name with column\n {df}")