class Palindrome:
    def __init__(self,str):
        self.str = str
    
    def check(self):
        rev = ""
        n = len(self.str)
        for i in range(n-1,-1,-1):
            rev += self.str[i]

        #print(rev)
        if rev == self.str:
            print("Palindrome")
        else:
            print("Not palindrome")


str = input("Enter string: ")
s1 = Palindrome(str)
s1.check()

