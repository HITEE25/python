'''Create a tuple with the characters of a string. Join the tuple 
elements into a single string. Print the string.'''

#string => tuple of char
str = "Hello"
my_tuple = tuple(str)#it would create tuple with char
print(my_tuple)
#join tuple into single string
s = ''.join(my_tuple)
#'' → empty string (separator)
#.join(...) → joins items together
#my_tuple → tuple whose elements will be joined
print(s)