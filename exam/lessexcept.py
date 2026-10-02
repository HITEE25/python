try:
    num = int(input("Enter + number: "))

    if num < 0:
        raise ValueError("Enter + num")
    
    print("you entered",num)

except ValueError as e:
    print("Error: ", e)
