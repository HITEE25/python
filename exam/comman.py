import numpy as np

arr1 = np.array([78,1,2])
arr2 = np.array([65,78,34])

common = np.intersect1d(arr1,arr2)

print(common)