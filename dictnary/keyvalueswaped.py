'''Create a dictionary with the first 5 positive integers as keys 
and their squares as values. Create a new dictionary with keys and 
values swapped. Print the new dictionary.'''

#key as first 5 positive intger
#values as square of keys
my_dist = {i : i**2 for i in range(1,6)}
#dictionary with keys and values swapped
new_dist = {value:key for key,value in my_dist.items()}
print(new_dist)
