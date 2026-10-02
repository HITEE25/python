#find intersection of two list
def intersection(list1,list2):
    #x is one element in list
    #list2 is entire list
    #3 == [2,4,5]
    #An integer can never be equal to a list, so condition is always False.
    #3 in [2,4,5] is a membership test so it would check if 3 is present in [2,4,5]
    return [x for x in list1 if x in list2]

def interact(list1,list2):
    list = []
    for x in list2:
        if x in list1:
            list.append(x)
    return list

list1 = [1,5,6,3,8]
list2 = [4,6,7,8,2]
print(list1)
print(list2)
#print intersection of two list
print(intersection(list1,list2))
print(interact(list1,list2))