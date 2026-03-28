class Drink:
    def __init__(self, name, sugar="正常甜", ice="正常冰"):
        self.name = name
        self.sugar = sugar
        self.ice = ice

    def show_label(self):
        print(f"{self.name} ({self.sugar}/{self.ice})")

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_label(self):
        print(f"{self.name} - ${self.price}")
