class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def calculate(self):
        pf = self.salary * 0.10
        tds = self.salary * 0.12
        deduct =self.salary * 0.05

        net_salary = self.salary - (pf + tds + deduct)

        print(self.name)
        print(self.salary)
        print(net_salary)


name = input("Enter name: ")
salary = int(input("Enter salary: "))
emp = Employee(name,salary)
emp.calculate()

