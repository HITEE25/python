people = []

n = int(input("Enter number of people"))

for i in range(n):
    fname = input("Enter fname: ")
    lname = input("Enter lname: ")
    age = int(input("Enter age: "))
    gender = input("Enter M/F: ")

    people.append((age,fname,lname,gender))

people.sort()

print(people)