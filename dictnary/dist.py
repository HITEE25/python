'''Create a dictionary with the first 10 positive integers as keys 
and their squares as values. Print the dictionary.'''

#i storing value from 1 to 10 and i**2 calculating sqare of i 
my_dist = {i : i**2 for i in range(1,11)}
print(my_dist)

#Print the value of the key 5 and the keys of the dictionary 
print(my_dist[5])
print(my_dist.keys())
#inserting element
my_dist[11] = 121
print(my_dist)
#deleting element based n index
my_dist.pop(1)
print(my_dist)

#Iterate over the dictionary and print each key-value pair.
for key,value in my_dist.items():
    print(f"keys : {key} values: {value}")
