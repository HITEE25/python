import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,4,8,2,7])

common = np.intersect1d(arr1,arr2)
print(common)