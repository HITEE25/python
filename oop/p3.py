class Number1:
    def get_n1(self):
        n1 = int(input("Enter number1: "))
        self.n1 = n1

class Number2:
    def get_n2(self):
        n2 = int(input("Enter number2: "))
        self.n2 = n2

class Mul(Number1,Number2):
    def mul(self):
        ans = self.n1 * self.n2
        return ans
    
obj = Mul()
obj.get_n1()
obj.get_n2()
ans = obj.mul()
print("Mul:",ans)
