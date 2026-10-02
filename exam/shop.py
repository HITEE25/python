class item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def purchase(self,no_items):
        if no_items < 0 or no_items > self.quantity:
            print("Invalid")
        elif no_items == 0:
            print("no item purchased")
        else:
            print("number of item purchased", no_items)
            self.quantity -= no_items

    def increase_stock(self,no_stock):
        if no_stock < 0:
            print("Invalid")
        elif no_stock == 0:
            print("no stock came")
        else:
            print("number of arrive in stock", no_stock)
            self.quantity += no_stock

    def display(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

i = item("kinderjoy",50,45)
i.purchase(100)
i.increase_stock(100)
i.display()
