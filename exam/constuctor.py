class Employee:
    def __init__(self,name=None,salary=None):
        if name is None and salary is None:
            print("no para")
            self.name = "unknow"
            self.salary = 0
        elif salary is None:
            print("one para")
            self.name = name
            self.salary = 0
        else:
            self.name = name
            self.salary = salary

    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)

E = Employee("hitee")
E.display()
