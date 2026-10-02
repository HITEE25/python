class Bank_Account:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        if amount < 0:
            print("invalid")
        else:
            self.__balance += amount

    def withdraw(self,amount):
        if amount < 0:
            print("inavlid")
        elif amount > self.__balance:
            print("insuffcient")
        else:
            self.__balance -= amount

    def display(self):
        print("name : ", self.name)
        print("balance: ", self.__balance)

b = Bank_Account("hitee",8000)
b.deposit(500)
b.withdraw(50)
b.display()

    