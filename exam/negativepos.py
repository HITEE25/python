file = open("world.txt","r")
neg_file = open("abc.txt","w")
pos_file = open("positive_no.txt","w")

for line in file:
    num = int(line)

    if num < 0:
        neg_file.write(str(num) + "\n")
    else:
        pos_file.write(str(num) + "\n")

file.close()
neg_file.close()
pos_file.close()

file = open("world.txt","r")
print(file.read())
file.close()

neg_file = open("abc.txt","r")
print(neg_file.read())
neg_file.close()

pos_file = open("positive_no.txt","r")
print(pos_file.read())
pos_file.close()