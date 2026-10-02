def first_ends(str1,str2):
    l1 = len(str1)
    l2 = len(str2)

    if l2 > l1:
        print("string 1 dont ends with string 2")

    #use partition to take end string
    if str1[l1 - l2:] == str2:
        print("string 1 ends with string 2")
    else:
        print("string 1 dont ends with string 2")

str1 = input("Enter string 1")
str2 = input("Enter string 2")
first_ends(str1,str2)