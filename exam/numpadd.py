import numpy as np

class Addtion:
    def __init__(self,a,b):
        self.a = np.array(a)
        self.b = np.array(b)

    def display(self):
        result = self.a + self.b
        print(self.a)
        print(self.b)
        print(result)

arr1 = [1,2,3]
arr2 = [4,5,6]
a = Addtion(arr1,arr2)
a.display()