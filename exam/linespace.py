file = open("demo.txt","w")
data = input("Enter data of file: ")
file.write(data)

count_space = 0
count_line = 0

for i in data:
    if i == "\n":
        count_line += 1
    elif i == " ":
        count_space += 1

print(count_line)
print(count_space)