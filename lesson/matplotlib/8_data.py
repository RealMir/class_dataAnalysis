import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"]="Malgun Gothic"
matplotlib.rcParams["font.size"]=15
matplotlib.rcParams["axes.unicode_minus"]=False

df = pd.read_excel("stock.xlsx")
df.ROE.fillna(0,inplace=True)

plt.plot(df["종목명"],df["PER"],"g+-.",label="PER",ms=10)
plt.plot(df["종목명"],df["ROE"],"y*:",label="ROE",ms=10)
plt.grid(axis="x",alpha=0.2)
plt.legend(loc=0,ncols=2)
plt.yticks([x*50 for x in range(6)])
plt.show()
