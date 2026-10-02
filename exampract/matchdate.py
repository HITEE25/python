import re

date = input("Enter date: ")

if re.match(r'\d{2}-\d{2}-\d{4}',date):
    print("valid")
else:
    print("invalid")
