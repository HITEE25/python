class Palindrome:
    def __init__(self,st):
        self.st = st

    def check_palindrome(self):
        orginal = self.st
        rev = ""

        for i in range(len(self.st) - 1,-1,-1):
            rev += self.st[i]

        if rev == orginal:
            print("Palidrome")
        else:
            print("Not palidrome")


st = input("Enter string: ")
p = Palindrome(st)
p.check_palindrome()