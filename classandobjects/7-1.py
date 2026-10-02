class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self,other):
        real_a = self.real + other.real
        img_a = self.img + other.img
        return Complex(real_a,img_a)
    
    def display(self):
        print("Adding two complex number: ", self.real , "+" , self.img ,"i")


r1 = int(input("Enter r1"))
i1 = int(input("Enter i1"))
c1 = Complex(r1,i1)
r2 = int(input("Enter r2"))
i2 = int(input("Enter i2"))
c2 = Complex(r2,i2)

#c1.display()
#c2.display()
c = c1 + c2
c.display()