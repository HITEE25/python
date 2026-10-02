import re

msg = input("Enter msg : ")

if re.match(r'\S+',msg):
    print("valid")
else:
    print("in-valid")