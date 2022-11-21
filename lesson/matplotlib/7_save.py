import matplotlib.pyplot as plt

x = [x for x in range(1,4)]
y = [-2,0,4]

plt.plot(x,y)
plt.savefig("graph.png") # save graph to img file

plt.plot(x,y)
plt.savefig("graph2.png", dpi=200)

plt.plot(x,y)
plt.savefig("graph3.png", facecolor="g")

plt.figure(linewidth=5)
plt.plot(x,y)
plt.savefig("graph4.png", edgecolor="r")