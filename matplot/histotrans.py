import matplotlib.pyplot as plt

ages = [2,4,10,11,12,21,34,56,33,44,47,46,55,79,78,77,70,81,83,92,99]

plt.hist(ages,bins=10,color="blue",alpha=0.1)

plt.xlabel("age")
plt.ylabel("number of people")

plt.show()