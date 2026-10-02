#rotate the list by two position
def rotate(org_list,n):
    rotate = org_list[n:] + org_list[:n]
    return rotate

org_list = [2,4,1,6,3]#orginal list
rotated_list = rotate(org_list,2)#roated list
print(org_list)
print(rotated_list)
#moving three position left
print(org_list[-2:]+org_list[:-2])