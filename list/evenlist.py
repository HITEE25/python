#created a list from 1 to 20 number
list = list(range(1,21))
print(list)
#create a even list
#storing x in list from list where even number
even = [x for x in list if x % 2 == 0]
print(even)