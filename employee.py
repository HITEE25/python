class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def cal_salary(self):
        pf = self.salary * 0.12
        tds = self.salary * 0.10
        reduce = self.salary * 0.05

        net_salary = self.salary - (pf + tds + reduce)

        print("Net_salary: ", net_salary)


name = input("Enter name of employee: ")
salary = int(input("Enter the salary: "))
emp = Employee(name,salary)
emp.cal_salary()