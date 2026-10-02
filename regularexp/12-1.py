#import regular expression re
import re

with open("employee.txt","r") as file:
    data = file.readlines()

selected = []

for line in data:
    if re.search(r'388120',line):
        parts = line.strip().split(',')
        name = parts[0]
        age = parts[1]
        selected.append(f"{name},{age}\n")


print("selected store")
with open("selected.txt","w") as file:
    file.writelines(selected)

print("update pin code")

updated_data = []

for line in data:
    new_line = re.sub(r'388120','388325',line)
    updated_data.append(new_line)

print(updated_data)

with open("employee.txt","w") as file:
    file.writelines(updated_data)
