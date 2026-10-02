data1 = input("Enter file1 data:")
data2 = input("Enter file2 data:")

file1 = open("file1.txt","w")
file1.write(data1)
file1.close()
file2 = open("file2.txt","w")
file2.write(data2)
file2.close()

file1 = open("file1.txt","r")
read1 = file1.read()

file2 = open("file2.txt","r")
read2 = file2.read()

file3 = open("file3.txt","w")
file3.write(read1 + read2)
file3.close()


sum = 0
for i in read1 + read2:
    if i.isdigit():
        sum += int(i)

print(sum)



