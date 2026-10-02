file = open("name.txt","r")

content = file.read()

words = content.split()
no_words = len(words)

no_state = 0
for word in content:
    if word in "?.!":
        no_state += 1

print(no_words)
print(no_state)