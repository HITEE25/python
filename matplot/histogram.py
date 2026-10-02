import matplotlib.pyplot as plt

ages = [2,4,10,11,12,21,34,56,33,44,47,46,55,79,78,77,70,81,83,92,99]

age_range = (0,100)
div = 10

plt.hist(ages,bins=div,range=age_range,color="green",rwidth=0.8,histtype="bar")

plt.xlabel("age")
plt.ylabel("number of people")

plt.title("histogram")

plt.show()