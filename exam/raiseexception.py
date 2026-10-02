class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message

user = "hitee"
password = 12345
pin = int(input("Enter pin: "))

try:
    if password != pin:
        raise MyCustomException("wrong passsword")
    else:
        print("succesfully login")

except MyCustomException as e:
    print("Error: ", e.message)

