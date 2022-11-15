import matplotlib.pyplot as plt

# create graph
plt.plot([1,2,3],[-1,0,2])
plt.show()

x = [1,2,3]
y = [-1,0,2]
plt.plot(x,y)
plt.title("graph") # create title
plt.show()

plt.plot(x,y)
plt.title("꺾은선 그래프") # broken font
plt.show()

import matplotlib.font_manager as fm
print([f.name for f in fm.fontManager.ttflist]) # print possible font to use

import matplotlib
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
plt.plot(x,y) 
plt.title("꺾은선 그래프") 
plt.show()

plt.plot(x,y) # broken minus mark
plt.title("꺾은선 그래프",fontdict={"family":"HYGungSo-Bold", "size":30}) 
plt.show()

matplotlib.rcParams["axes.unicode_minus"] = False
plt.plot(x,y)
plt.show()