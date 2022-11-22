import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

x = [1,2,3]
y = [-2,0,4]
plt.plot(x,y)
plt.xlabel("X축")
plt.ylabel("Y축")
plt.show()

plt.plot(x,y)
plt.xlabel("X축", color="blue", loc="right") # loc = location
plt.ylabel("Y축", color="#00FF00", loc="top")
plt.show()

plt.plot(x,y)
plt.xlabel("X축", color="blue", loc="right") # loc = location
plt.ylabel("Y축", color="#00FF00", loc="top", rotation=0)
plt.show()

plt.plot(x,y)
plt.xticks([1,2,3])
plt.yticks([])
plt.show()

z = ["1번","2번","3번"]
plt.plot(x,y)
plt.xticks(x,z)
plt.yticks(rotation=45)
plt.show()

plt.plot(x,y)
plt.xlim(0,5) # setting x range to 0~5
plt.ylim(-5,5) # setting y range to -5~5
plt.show()