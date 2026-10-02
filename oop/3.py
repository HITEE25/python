class Number1:
    def __init__(self):
        n1 = int(input("Enter number1: "))
        self.n1 = n1

class Number2:
    def __init__(self):
        n2 = int(input("Enter number2: "))
        self.n2 = n2

class Mul(Number1,Number2):
    def __init__(self):
        Number1.__init__(self)
        Number2.__init__(self)

    def mul(self):
        ans = self.n1 * self.n2
        return ans
    
obj = Mul()
ans = obj.mul()
print("Mul: ",ans)
