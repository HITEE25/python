try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    c = a/b

    print("Division is: ",c)
except ZeroDivisionError:
    print("Error: Denometer should not be zero")
except ValueError:
    print("Error: value are different")