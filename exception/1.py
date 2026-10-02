try:
    n1 = int(input("Enter number1: "))
    n2 = int(input("Enter number2: "))
    ans = n1/n2
    print("Div: ",ans)
    
except ZeroDivisionError:
    print("Error: cant divide deno is zero")

except ValueError:
    print("Error: enter valid intger number")

finally:
    print("No error")