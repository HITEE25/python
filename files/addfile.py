filename1 = input("Enter filename1")
file1 = open(filename1,'r')
data1 = file1.read()
file1.close()

filename2 = input("Enter filename2")
file2 = open(filename2,'r')
data2 = file2.read()
file2.close()

filename3 = input("Enter filename3")
data = data1 + data2
file3 = open(filename3,'w')
file3.write(data)
file3.close()

read_file = open(filename3,'r')
data = read_file.read()

sum = 0
for ch in data:
    if ch.isdigit():
        sum += int(ch)

print(sum)
read_file.close()


