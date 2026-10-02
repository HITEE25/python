import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [1,5,2,6,4,7]

plt.scatter(x,y,label="star",marker="*",s=30,color="blue")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("my plot graph")
plt.legend()

plt.show()