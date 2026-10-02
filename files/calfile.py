filename = input("Enter filename: ")
file = open(filename,'w')
text = input("Enter text: ")
file.write(text)
file.close()

count_line = 0
count_space = 0

read_file = open(filename,'r')

data = read_file.read()

for ch in data:
    if ch == '\n':
        count_line+=1
    elif ch == ' ':
        count_space+=1

print(count_line)
print(count_space)

read_file.close()