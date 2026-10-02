import re
file = open("email.txt","r")
content = file.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+"

gmails = re.findall(pattern,content)

for mail in gmails:
    print(mail)