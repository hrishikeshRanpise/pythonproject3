
class Laptop:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def getPrice(self):
        print(f"Price is {self.price}")

    def getQuant(self):
        print(f"Quantity is {self.quantity}")

    def getTotal(self):
        return self.quantity * self.price


lap1 = Laptop(1000, 4)

lap1.getPrice()
lap1.getQuant()
print(f"Total {lap1.getTotal()}")

lap2 = Laptop(500, 10)

lap2.getTotal()



