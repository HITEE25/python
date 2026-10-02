class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        if amount >= 0:
            self.__balance += amount
            print(f"{amount} deposited")
        else:
            print("invalid amount")

    def withdraw(self,amount):
        if amount < 0:
            print("Invalid")
        elif amount > self.__balance:
            print("insufficent")
        else:
            self.__balance -= amount
            print(f"{amount} withdraw")

    def display(self):
        print(f"{self.name} {self.__balance}")

acc = BankAccount("Hitee",5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.display()