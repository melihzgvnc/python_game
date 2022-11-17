class Item:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


    def get_description(self):
        return {self.name: self.weight}