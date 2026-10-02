filename = input("Enter filename: ")
word = input("Enter word: ")

file = open(filename,'r')
content = file.read()

words = content.split()

if word in words:
    print("word found")
else:
    print("not")

file.close()



