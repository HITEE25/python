import re

pwd = input("Enter Password: ")
# (?=.*[A-Z]) atlest one uppercase
# (?=.*[a-z]) atlest one lowercase
# ?= atlest one
# . any char
# * any number of char
if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$*!_%-?]).{8,}$',pwd):
    print("Password matched")
else:
    print("Password not matched")

