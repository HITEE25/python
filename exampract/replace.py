import re

text = input("Enter text: ")
result = re.sub(r'\d','x',text)

print(result)



