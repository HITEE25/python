file = open("name.txt","r")
lines = file.read()

words = lines.strip().split()

result = []

for word in words:
    if word[0].lower() == 'a' and word[-1].lower() == 'e':
        result.append(word)

if words:
    if words[0].lower() == "student":
        result.append(words[0])
    if words[-1].lower() == "student":
        result.append(words[-1])

file.close()

file = open("namewrite.txt","w")

for name in result:
    file.write(name + "\n")

file.close()
