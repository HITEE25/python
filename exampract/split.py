import re

text = input("Enter text: ")

result = re.split(r'\s',text)
print(result)
