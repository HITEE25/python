file = open("book.txt","w")
file.write("abc,12,xyz,500\n")
file.write("book,34,athour,300\n")
file.write("life amazing secret,34,gaur gopal das swami,600\n")

books = []
file.close()

file = open("book.txt","r")

for lines in file:
    book,id,author,price = lines.strip().split(",")
    books.append((book,id,author,int(price)))

file.close()

expensive = list(filter(lambda b:b[3] > 500,books))

for i in expensive:
    print(i)