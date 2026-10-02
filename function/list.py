def sum_of_squares(list):
    total = 0
    for i in list:
        #sum of sqares of list numbers
        total = total + (i*i)
    return total

nums=[1,2,3,4]
print("Sum of sqaures of numbers:",sum_of_squares(nums))