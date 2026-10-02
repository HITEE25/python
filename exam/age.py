name = input("Enter name: ")
age = int(input("Enter age: "))

if age < 0:
    print("invalid")
else:
    file = open("age.txt","w")
    file.write("Name: "+ name + "\n")
    file.write("Age: " + str(age) + "\n")

if age >= 18:
    print("elgiable")


print(len(name))