import re

employee = [
    "abc 4000 Daman Pin:388120",
    "aihu 5000 Diu Pin:380021",
    "mihu 6000 Daman Pin:388120",
]

file = open("employee.txt","w")

for emp in employee:
    if re.search(r"\b388120\b",emp):
        matched = re.findall(r"(\w+)\s+(\d+)",emp)
        file.write(f"{matched[0][0]} {matched[0][1]}\n")

file.close()

file = open("employee.txt","r")
content = file.read()

updated_data = re.sub(r"\b388120\b","388325",content)

file.close()

file = open("employee.txt","w")
file.write(updated_data)

file.close()