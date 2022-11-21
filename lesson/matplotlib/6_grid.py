import matplotlib.pyplot as plt

x = [x for x in range(1,4)]
y = [-2,0,4]

plt.plot(x,y)
plt.grid() # create grid
plt.show()

plt.plot(x,y)
plt.grid(axis="y") # setting grid axis
plt.show()

plt.plot(x,y)
plt.grid(axis="y",color="c",ls=":",lw=5,alpha=0.2) # setting grid style
plt.show()