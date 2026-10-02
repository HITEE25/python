import re

num = input("Enter mobile number: ")

#indian number starts with 6-9
#after that 9 digits
if re.match(r'[6-9][0-9]{9}',num):
    print("valid",num)
else:
    print("invalid")