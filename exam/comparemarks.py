class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __gt__(self,other):
        if self.marks > other.marks:
            return True
        else:
            return False
        
s1 = Student("hitee",23)
s2 = Student("mihu",30)

if s1 > s2:
    print(s1.name,s1.marks)
elif s2 > s1:
    print(s2.name,s2.marks)
else:
    print("equal")