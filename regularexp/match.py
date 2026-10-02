import re

names = ["hitee","mishu","mihu","vency","RaJ","suresH","RamesH"]

pattern = r'^[RSrs].*[HJhj]$'

for name in names:
    if re.match(pattern,name):
        print(name)
