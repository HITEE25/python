import numpy as np

arr = np.array([1,4,5,6,7])

odd=arr[arr % 2 != 0]
print(odd)