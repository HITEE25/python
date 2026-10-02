temp = float(input("Enter temp: "))
humdity = float(input("Enter humdity:"))

if temp > 30 and humdity < 20:
    print("Hot and Dry")
elif temp >= 20 and temp <= 30 and humdity >= 20 and humdity <= 40:
    print("Good weather condition")
elif temp >= 20 and temp <= 30 and humdity >= 80:
    print("Moisture present")
else:
    print("no matched")