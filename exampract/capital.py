import re

msg = input("Enter message: ")
result = re.findall(r'\b[A-Z]\w*',msg)
print(result)

alpha = re.findall(r'[A-Za-z]+',msg)
print(alpha)

