import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("stock.xlsx")
df.drop(index=6,inplace=True)
df["현재가"] = df["현재가"].str.replace(",","")
df["현재가"] = pd.to_numeric(df["현재가"])
df["BPS"] = [49387,82576,120980,99868,417614,244348]
df["PBR"] = df.현재가 / df.BPS

# basic graph
plt.bar(df["종목명"],df["PER"],label="PER")
plt.bar(df["종목명"],df["ROE"],label="ROE")
plt.bar(df["종목명"],df["PBR"],label="PBR")
plt.legend()
plt.show()

# create cumulative graph
plt.bar(df["종목명"],df["PER"],label="PER")
plt.bar(df["종목명"],df["ROE"],bottom=df["PER"],label="ROE")
plt.bar(df["종목명"],df["PBR"],bottom=df["PER"]+df["ROE"],label="PBR")
plt.legend()
plt.show()

plt.barh(df["종목명"],df["PER"],label="PER")
plt.barh(df["종목명"],df["ROE"],left=df["PER"],label="ROE")
plt.barh(df["종목명"],df["PBR"],left=df["PER"]+df["ROE"],label="PBR")
plt.legend()
plt.show()

# create multiple graph
idx = np.arange(df.shape[0])
length = 0.25

plt.bar(idx-length,df["PER"],width=length,label="PER")
plt.bar(idx,df["ROE"],width=length,label="ROE")
plt.bar(idx+length,df["PBR"],width=length,label="PBR")
plt.xticks(idx,df["종목명"])
plt.legend()
plt.show()

plt.barh(idx-length,df["PER"],height=length,label="PER")
plt.barh(idx,df["ROE"],height=length,label="ROE")
plt.barh(idx+length,df["PBR"],height=length,label="PBR")
plt.yticks(idx,df["종목명"])
plt.legend()
plt.show()