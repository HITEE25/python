'''Create a dictionary where the keys are the first 5 positive 
integers and the values are lists containing the first 5 multiples 
of the key. Print the dictionary.'''

#key are value from 1 to 2
#value is a list containing first 5 multiples of key
d = {i : [i * j for j in range(1,6)] for i in range(1,6)}
print(d)
