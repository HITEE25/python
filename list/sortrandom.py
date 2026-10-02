'''Create a list of random numbers and sort it in ascending and descending 
order.Remove the duplicates from the list and print the modified list.'''
import random
#create a list of random number
#it would genrate random number (intger) between 1 to 20
# _ this says i dont care about loop variable , it would run loop 15 times
#so size of loop would be 15
num = list(random.randint(1,20) for _ in range(15))
print(num)
#ascending order
sorted_num = sorted(num)
print(sorted_num)
#decending order
sorted_dec = sorted(num, reverse={True}) 
print(sorted_dec)
#set store unique element it can store unique element
#creating list of unique element
unique = list(set(num))
print(unique)