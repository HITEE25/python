import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1,100,10)

mean = np.mean(data)
median = np.median(data)
stddev = np.std(data)

print(mean)
print(median)
print(stddev)

plt.hist(data,bins=10,histtype="bar",color="blue")
plt.xlabel("value")
plt.ylabel("frequency")
plt.title("histogram")
plt.show()
