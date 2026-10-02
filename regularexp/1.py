import re
employee = [
    "Hitee,4500,daman,388120",
    "Prachi,3500,daman,388120",
    "Pratha,5500,daman,388150"
]

file = open("emp.txt",'w')
file.write("Employee details\n")

for emp in employee:
    if re.search(r'388120',emp):
        #remove space create list separted by ,
        parts = emp.strip().split(',')
        name = parts[0]
        salary = parts[1]
        #store name and salary
        file.write(f"{name} , {salary}\n")

file.close()

updated_data = []
#update data in emp.txt
file1 = open("emp.txt",'r')
data = file1.readlines()

for line in data:
    update = re.sub(r'388120','388325',line)
    updated_data.append(update)

file1.close()

file2 = open("emp.txt",'w')
file2.writelines(updated_data)
file2.close()


