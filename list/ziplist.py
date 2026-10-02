#combine the list into the tuples
list1 = [1,2,3,4,5,6]
list2 = ['q','a','b','c']
#to combine to list using zip
list = list(zip(list1,list2))
#[(1, 'q'), (2, 'a'), (3, 'b'), (4, 'c')]
print(list)
