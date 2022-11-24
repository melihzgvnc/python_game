"""
    Sets up a store where a player can buy items.
"""
class Store:

    def __init__(self):
        """
            Constructor method.
        """
        self.on_sale = {}
        self.all_items = []

    def add_item(self, item):
        """
            Add an item to the store.
        :param item: an instance of Item class
        :return: None
        """
        self.on_sale[item.name] = {"Price": str(item.price)+"£", "Weight": item.weight}
        self.all_items.append(item)

    def sell_item(self, item):
        """
            Sell an item.
        :param item: an instance of Item class
        :return: None
        """
        self.on_sale.pop(item.name)
        self.all_items.remove(item)

    def get_item(self, second_word):
        """
            Fetch an item.
        :param second_word: the name of an item
        :return: None if item does not exist, item otherwise
        """
        temp = None
        for item in self.all_items:
            if item.name == second_word:
                temp = item
        if temp == None:
            return None
        else:
            return temp

    def get_items(self):
        """
            Get the items on sale.
        :return: a dictionary containing the names of the items as keys and
        the weight and price of them as values
        """
        return self.on_sale

