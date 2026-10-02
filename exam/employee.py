file = open("input.txt","r")

Last_name = []

for line in file:
    words = line.strip().split()
    #appending last name
    Last_name.append(words[-1])

n = len(Last_name)

for i in range(n):
    for j in range(0,n-i,-1):
        if Last_name[j] > Last_name[j+1]:
            Last_name[j],Last_name[j+1] = Last_name[j+1],Last_name[j]

file.close()

file = open("output.txt","w")

for name in Last_name:
    file.write(name + "\n")

file.close()
