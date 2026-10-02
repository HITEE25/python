import re

names = ["Amita", "Ravi", "Meena", "Sohan","meena"]

for name in names:
    if re.match(r'^[A-M].*[aeiouAEIOU]$',name):
        print(name)