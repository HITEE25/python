phonebook = {
    "hitee" : "9734523456",
    "mihu" : "8678353535",
    "vency" : "9456323467"
}

def findname(name):
    if name in phonebook:
        del phonebook[name]
        print("deleted")
    else:
        print("name not found")

findname("hitee")
print(phonebook)