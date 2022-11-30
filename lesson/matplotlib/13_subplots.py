import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("stock.xlsx")
df.drop(index=6,inplace=True)

fig,graph = plt.subplots(2,2,figsize=(10,5)) # create 2X2 graphs

fig.suptitle("여러 그래프") # setting title

graph[0][0].plot(df.종목명, df.ROE)
graph[0,1].bar(df.종목명, df.ROE)
graph[1,0].pie(df.ROE)
graph[1,1].scatter(df.PER,df.ROE)
plt.show()