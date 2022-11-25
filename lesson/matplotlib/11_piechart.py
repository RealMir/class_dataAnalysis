import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("stock.xlsx")

plt.pie(df["PER"]) # create pie chart
plt.show()

explode = [0.1] * len(df["PER"])
plt.pie(df["PER"],explode=explode) # set explode
plt.show()

plt.pie(df["PER"],labels=df["종목명"]) # set labels
plt.show()

colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff', '#da9bff']
plt.pie(df["PER"],colors=colors) # set colors
plt.show()

plt.pie(df["PER"],autopct="%.1f%%") # set autopct
plt.show()

def custom_pct(pct):
  return ("%.1f%%" % pct) if pct >= 5 else ""
plt.pie(df["PER"],autopct=custom_pct)
plt.show()

plt.pie(df["PER"],autopct="%.1f%%",pctdistance=0.8) # set pctdistance
plt.show()

plt.pie(df["PER"],explode=explode,shadow=True) # set shadow
plt.show()

plt.pie(df["PER"],labels=df["종목명"],labeldistance=1.5) # set labeldistance
plt.show()

plt.pie(df["PER"],startangle=90) # set startangle
plt.show()

plt.pie(df["PER"],radius=0.3) # set radius
plt.show()

plt.pie(df["PER"],counterclock=False) # set counterclock
plt.show()

wedgeprops = {"width":0.6, "edgecolor":"w", "linewidth":2, "linestyle":":"}
plt.pie(df["PER"],wedgeprops=wedgeprops) # set wedgeprops
plt.show()