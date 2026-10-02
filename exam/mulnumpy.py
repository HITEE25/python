import numpy as np

class Multiplication:
    def __init__(self,a,b):
        self.a = np.array(a)
        self.b = np.array(b)

    def display(self):
        result = np.dot(self.a,self.b)
        print(self.a)
        print(self.b)
        print(result)

arr1 = [[1,2],
        [3,4]]
arr2 = [[5,6],
        [7,8]]

m = Multiplication(arr1,arr2)
m.display()