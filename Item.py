"""
    Sets up an item which has the attributes, name, weight and price.
    Price is 0.1£ by default if it is not specified.
"""
class Item:

    def __init__(self, name, weight, price=0.1):
        """
            Initialise an item.
        :param name: name of the item
        :param weight: weight of the item in kg
        :param price: price of the item in pounds
        """
        self.name = name
        self.weight = weight
        self.price = price

    def get_description(self):
        """
            Get the description of an item
        :return: a dictionary consisting of the name as key and the weight as value
        """
        return {self.name: self.weight}