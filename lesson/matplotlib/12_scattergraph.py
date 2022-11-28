import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("stock.xlsx")
df.drop(index=6,inplace=True)

def sort_company(company):
  if company == "삼성":
    return 1
  elif company == "LG":
    return 2
  elif company == "SK":
    return 3
df["계열사"] = [sort_company(company) for company in df["종목명"].str[0:2]]

plt.scatter(df["ROE"],df["PER"]) # create scatter graph
plt.xlabel("ROE")
plt.ylabel("PER")
plt.show()

size = np.random.rand(6) * 1000
plt.scatter(df["ROE"],df["PER"],s=size) #setting size
plt.show()

plt.scatter(df["ROE"],df["PER"],c="g") # setting color
plt.show()

plt.scatter(df["ROE"],df["PER"],c=df["계열사"]) # setting color by df["계열사"]
plt.show()

plt.scatter(df["ROE"],df["PER"],c=df["계열사"],cmap="winter") # setting colormap
plt.show()

plt.scatter(df["ROE"],df["PER"],c=df["계열사"],cmap="winter") 
for num, txt in enumerate(df["종목명"]):
  plt.text(df["ROE"][num],df["PER"][num],txt)
plt.show()

plt.scatter(df["ROE"],df["PER"],c=df["계열사"],cmap="winter") 
# create color bar
plt.colorbar(ticks=[1,2,3],label="계열사", orientation='horizontal',shrink=0.5)
for num, txt in enumerate(df["종목명"]):
  plt.text(df["ROE"][num],df["PER"][num],txt)
plt.show()