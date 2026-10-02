f = open("ab.txt" , "w")
name = "haraprasad\n"
roll = "24IT420"
f.write(name)
f.write(roll)
f.close()

f = open("ab.txt" , "r")
content = f.read()
print(content)
f.close()