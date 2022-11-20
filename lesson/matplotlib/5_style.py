import matplotlib.pyplot as plt

x=[1,2,3]
y=[-2,0,4]

# setting graph color
plt.plot(x,y,color="green") #same
plt.plot(x,y,color="g") #same
plt.plot(x,y,color="#008000") #same
plt.show()

# setting graph marker
plt.plot(x,y,marker="*")
plt.show()
plt.plot(x,y,marker="*",markersize=20)
plt.show()
plt.plot(x,y,marker="*",ms=20,markerfacecolor="y")
plt.show()
plt.plot(x,y,marker="*",ms=20,mfc="y",markeredgecolor="r")
plt.show()

# setting graph line
plt.plot(x,y,linestyle="-.")
plt.show()
plt.plot(x,y,ls="-.",linewidth=10)
plt.show()

# use format string
plt.plot(x,y,"go:") # color="g", marker="o", linestyle=":"
plt.show()
plt.plot(x,y,"y+") # color="y", marker="+", linestyle="None"
plt.show()

# setting graph size
plt.figure(figsize=(5,5))
plt.plot(x,y)
plt.show()
plt.figure(figsize=(5,5),dpi=50)
plt.plot(x,y)
plt.show()

# setting background color
plt.figure(facecolor="g")
plt.plot(x,y)
plt.show()

# setting graph transparency
plt.plot(x,y,alpha=0.3)
plt.show()