'''Create a list of the first 10 positive integers. Remove the elements 
at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.'''

list = list(range(1,11))
del list[2]
del list[4]
del list[6]
list.insert(5,99)
print(list)