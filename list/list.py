list = [10,20,45,60,70,90]
print(list[0])
list[0] = 30
print(list[0])
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
#5 is index
#30 value to be inserted
list.insert(5,30)
print(list)
#append
list.append(40)
print(list)
print(list[1:4])
#print in reverse order
print(list[::-1])
if 20 in list:
    print("present")
#change range of iteam value
list[1:3] = [56,78]
#it would append both value, if i gave two value and repalce number only one
list[1:2] = [90,100]
print(list)
#it would append one value, if i gave one value and repalce more then one number , then extra would be deleted
list[1:3] = [90]
print(list)
#extend is used to append one list to another
newlist = [45,23,56,78]
list.extend(newlist)
print(list)
#remove specific iteam
list.remove(23)
print(list)

#lst = list(range(1,21))
#print(lst)

