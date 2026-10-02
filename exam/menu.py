menu = {
    "Paneer": 456,
    "momos": 345,
    "sushi": 1000
}

found = False
dish = input("Enter dish: ")

print("matched: ")

for search in menu:
    if dish.lower() in search.lower():
        print(search, "-" , menu[search])
        found = True

if not found:
    print("no matched")