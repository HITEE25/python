import numpy as np

def DiagCalc(M):
    arr = np.array(M)

    print(np.trace(arr))
    print(np.trace(np.fliplr(arr)))

M = [[1,2,3],
     [3,4,5],
     [6,7,81]]

print(DiagCalc(M))