'''Create a dictionary with the first 5 positive integers as keys 
and their squares as values. Convert the dictionary to a list of 
tuples and print it.'''

#first 5 positive intger as key
#and values as a sqaure of key
my_dist = {i : i**2 for i in range(1,6)}
#covert into list of tuple
list_of_tuple = list(my_dist.items())
#my_dist is a dictionary
#.items() returns all key–value pairs from the dictionary
#Each key–value pair is returned as a tuple
#list() converts those tuples into a list
print(list_of_tuple)