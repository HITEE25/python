'''Create a dictionary with the first 10 positive integers as keys 
and their squares as values. Create a new dictionary containing only 
the key-value pairs where the key is even. Print the new dictionary.'''

#key value as first 10 positive intger
#values as square of key
my_dist = {i : i**2 for i in range(1,11)}
#stores key value pair my_dist.items()
#for key,value in my_dist.items() take key and value from my_dist
#take a key if the key is even if key % 2 == 0
new_d = {key:value for key,value in my_dist.items() if key % 2 == 0}
print(new_d)