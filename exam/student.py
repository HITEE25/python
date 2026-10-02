class Student:
    def read(self):
        self.name = input("Enter name: ")
        self.roll = input("Enter roll: ")
        self.age = int(input("Enter age: "))
        self.marks = int(input("Enter marks: "))

    def print(self):
        print(self.name)
        print(self.roll)
        print(self.age)
        print(self.marks)

s = Student()
s.read()
s.print()