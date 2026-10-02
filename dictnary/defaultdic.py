'''Create a default dictionary where each key has a default value 
of an empty list. Add some elements to the lists and print the 
dictionary.'''

#defaultdict(list)→ Creates a dictionary where missing keys automatically get an empty list.
#default_dis['a'].append(1)→ Since 'a' doesn’t exist, Python creates it as [] and then appends 1

from collections import defaultdict

default_dict = defaultdict(list)
default_dict['a'].append(1)
default_dict['b'].append(2)
default_dict['c'].append(3)
print(default_dict)