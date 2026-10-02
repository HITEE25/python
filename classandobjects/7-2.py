class Palindrome:

    def __init__(self,num):
        self.num = num

    def check_palindrome(self):
        rev = ""

        for i in range(len(self.num) - 1, -1 , -1):
            rev += self.num[i]

        if rev == self.num:
            print("Palindrome")
        else:
            print("Not Palindrome")

str = input("Enter string: ")
s1 = Palindrome(str)
s1.check_palindrome()