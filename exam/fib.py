def fibo(n):
    a = 0
    b = 1
    fib = []
    
    for i in range(n):
        fib.append(a)
        a,b=b,a+b
    return fib

n = int(input("Enter number: "))
result = fibo(n)
print(result)