class Number1:
    def get_n1(self):
        self.n1 = int(input("Enter number 1: "))

class Number2:
    def get_n2(self):
        self.n2 = int(input("Enter number 2: "))

class Multiplication(Number1,Number2):
    def mul(self):
        if self.n1 < 0 or self.n2 < 0:
            print("take Postive number")
            #self.get_n1()
        else:
            print("mul: ", self.n1 * self.n2)

obj = Multiplication()
obj.get_n1()
obj.get_n2()
obj.mul()
