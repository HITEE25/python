class Library:
    def __init__(self,library_name):
        self.library_name = library_name

    def display_library(self):
        print(self.library_name)

class Member(Library):
    def __init__(self,library_name,member,duebook,late):
        super().__init__(library_name)
        self.member = member
        self.duebook = duebook
        self.late = late
        self.fineper = 5

    def fine(self):
        total_fine = self.duebook * self.late * self.fineper
        return total_fine
    
    def display(self):
        print("Name: ", self.member," Overdue Book: ", self.duebook," Delay: ", self.late," fine", self.fine())

obj = Member("bvm","hitee",2,3)
obj.display_library()
obj.fine()
obj.display()