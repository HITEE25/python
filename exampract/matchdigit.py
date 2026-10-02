import re
msg = input("Enter msg: ")

result = re.findall(r'\d+',msg)
print(result)