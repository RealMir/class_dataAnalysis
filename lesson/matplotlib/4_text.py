import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.size"] = 15

x=[1,2,3]
y=[-2,0,4]

plt.plot(x,y)
for num, txt in enumerate(y):
  plt.text(x[num],y[num],txt) # create text
plt.show()

plt.plot(x,y)
for i in range(len(y)):
  txt = f"({x[i]},{y[i]})"
  plt.text(x[i],y[i]+0.2,txt,ha="center") # show coordinates
plt.show()