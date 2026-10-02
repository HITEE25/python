try:
    filename = input("Enter file name ")
    file = open(filename,"r")

    num = int(input("Enter number: "))
    sum = num + "10"

    print("Sum: ",sum)
except FileNotFoundError:
    print("File not found error ")
except PermissionError:
    print("Didn't get Permission ")
except TypeError:
    print("Type are not same ")
except ValueError:
    print("invalid type Value ")