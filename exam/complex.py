class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self,other):
        real_p = self.real + other.real
        img_p = self.img + other.img
        return Complex(real_p,img_p)

    def display(self):
        print(f"{self.real} + {self.img}i")

r1 = int(input("Enter r1: "))
i1 = int(input("Enter i1: "))
c1 = Complex(r1,i1)
r2 = int(input("Enter r2: "))
i2 = int(input("Enter i2: "))
c2 = Complex(r2,i2)

c3 = c1 + c2

c3.display()