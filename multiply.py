class number1:
    def __init__(self):
        n1 = int(input("Enter number1: "))
        return n1

class number2:
    def __init__(self):
        n2 = int(input("Enter number2: "))
        return n2

class Mutilpy(number1,number2):
    def __init__(self):
        num1 = number1.__init__(self)
        num2 = number2.__init__(self)
        if  num1 < 0 and  num2 < 0:
            print("Number must be positive")
        else:
            mul = num1 * num2
            print("Multiplication: ",mul)


mul = Mutilpy()

