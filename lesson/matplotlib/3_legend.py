import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"]="Malgun Gothic"
matplotlib.rcParams["font.size"]=15
matplotlib.rcParams["axes.unicode_minus"]=False

x=[1,2,3]
y=[-2,0,4]

plt.plot(x,y, label="data")
plt.legend() # create legend
plt.show()

plt.plot(x,y, label="data")
plt.legend(loc="upper right") # setting location
plt.show()

plt.plot(x,y, label="data")
plt.legend(loc=1) # setting location with location code
plt.show()

plt.plot(x,y, label="data")
plt.legend(loc=(0.75,0.5)) # setting location with coordinates
plt.show()