class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate(self):
        pf = self.salary*0.12
        tds = self.salary*0.10
        dec = self.salary*0.05

        net_salary = self.salary - (pf+tds+dec)

        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print("pf: ",pf)
        print("tds: ",tds)
        print("deduction: ",dec)
        print("net_salary: ",net_salary)

name = input("Enter name: ")
salary = float(input("Enter salary: "))
emp = Employee(name,salary)
emp.calculate()