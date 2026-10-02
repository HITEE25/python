class Restarurant:
    def __init__(self):
        self.menu  = {
            "Pizza":456,
            "Pasta":120,
            "Burger":123,
            "Sandwich":100
        }
    def display(self):
        for item,price in self.menu.items():
            print(f"{item} X {price}")

class Bill(Restarurant):
    def __init__(self):
        super().__init__()
        self.order = []

    def take_order(self):
        while True:
            item = input("Enter item: ")

            if item.lower() == "done":
                break

            if item in self.menu:
                self.order.append(item)
            else:
                print("Not available")
        
    def bill(self):
        total = 0
        for item in self.order:
            print(f"Order:  {item} ${self.menu[item]}")
            total += self.menu[item]

        print("Total", total)

obj = Bill()
obj.take_order()
obj.bill()