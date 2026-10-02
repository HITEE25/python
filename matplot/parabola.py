import matplotlib.pyplot as plt

x = range(-100,100,10)
y1 = []
y2 = []

#upward parabola
for i in x:
    y1.append(i**2)


#downward parabola
for i in x:
    y2.append(-i**2)

#plotting
plt.plot(x,y1)
plt.plot(x,y2)

#labeling
plt.xlabel("x")
plt.ylabel("y")

plt.ylim(-2000,2000)
plt.axvline(0)
plt.axhline(0)

plt.savefig("plot.png")

plt.show()


