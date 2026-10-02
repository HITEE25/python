data = input("Enter data: ")

file = open("text.txt","a")
file.write(data + "\n")
file.close()

file = open("text.txt","r")
content = file.read()

print(content)