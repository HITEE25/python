import numpy as np

arr = np.array([1,4,5,6,7])

even = arr[arr % 2 == 0]
print(even)
