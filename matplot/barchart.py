import matplotlib.pyplot as plt

x = [1,4,6,2,8]
name = ['one','two','three','four','five']

colors = ['g','k']
plt.bar(name,x,width=0.8,color=colors)

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("my bar chart")
plt.show()