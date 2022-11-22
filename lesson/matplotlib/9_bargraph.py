import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("stock.xlsx",index_col="No")
df.drop(index=6,inplace=True)

plt.bar(df["종목명"],df["ROE"]) # create bar graph
plt.show()

plt.bar(df["종목명"],df["ROE"],color="g")
plt.show()

plt.bar(df["종목명"],df["ROE"],hatch="/")
plt.show()

plt.bar(df["종목명"],df["ROE"],width=0.3)
plt.show()

bar = plt.bar(df["종목명"],df["ROE"])
for num, rect in enumerate(bar):
  plt.text(num,rect.get_height()+0.3,df["ROE"][num],ha="center")
plt.ylim(5,20)
bar[0].set_color("g")
bar[1].set_hatch("*")
bar[2].set_width(0.3)
bar[2].set_width(2)
plt.show()

plt.barh(df["종목명"],df["ROE"]) # create horizontal graph
plt.show()

bar = plt.barh(df["종목명"],df["ROE"])
for num, rect in enumerate(bar):
  plt.text(rect.get_width()+0.3,num,df["ROE"][num])
plt.xlim(5,20)
plt.show()