import re

text = input("Enter text: ")

result = re.findall(r'\bhitee\b',text)

print(result)

