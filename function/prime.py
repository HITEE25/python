'''def check_prime(num):
    if num <= 1:
        print("Not prime")
        return
    
    flag = False
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break

    if(flag):
        print("Not Prime")
    else:
        print("Prime")

num=int(input("Enter number:"))
check_prime(num)'''

def check_prime(num):
    if num <= 1:
        #print("Not prime")
        return "Not prime"
    
    for i in range(2,num):
        if num % i == 0:
            return "Prime"

    return "Not prime"

num=int(input("Enter number:"))
print(check_prime(num))
