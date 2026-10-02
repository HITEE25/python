class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message

name = "Hitee"
password = 12345
pin = int(input("Enter pin: "))

try:
    if password != pin:
        raise MyCustomException("Incorrect Password ")
    else:
        print("Login succesfully")
except MyCustomException as e:
    print("Error: ", e.message)
