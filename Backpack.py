from TextUI import TextUI
"""
    Create a backpack for the player. 
    The backpack has a capacity of 10kg by default.
"""
class Backpack:

    def __init__(self, capacity=10):
        """
            Construct a backpack.
        :param capacity: the weight limit the backpack can carry, 10 by default
        """
        self.capacity = capacity
        self.backpack = {"Items": [], "Weight": 0}
        self.inventory = []
        self.textUI = TextUI()

    def get_inventory(self):
        """
            Fetch all items in the backpack.
        :return: a dictionary containing items and the total weight they make up.
        """
        return self.backpack

    def get_item(self, second_word):
        """
            Fetch an item according to its name given as a parameter.
        :param second_word: a string of the name of an item
        :return: Item if exists, otherwise None
        """
        for item in self.inventory:
            if second_word == item.name:
                return item

    def add_item(self, item, room):
        """
            Add an item to the backpack.
        :param item: an instance of Item class
        :param room: an instance of Room class
        :return: None
        """
        if self.backpack["Weight"] + item.weight < self.capacity:
            #Add the item into the inventory if it does not outweigh the capacity
            self.inventory.append(item)
            self.backpack['Items'].append({"Name": item.name, "Price": item.price})
            self.backpack['Weight'] += item.weight
            self.textUI.print_to_textUI(f"An item added to your inventory: {self.get_inventory()}")
            room.remove_item(item)
        else:
            #If the capacity is exceeded, the item will not be added
            self.textUI.print_to_textUI(f"The backpack can only carry up to {self.capacity}kg!")
            self.textUI.print_to_textUI("Your backpack is full! You cannot add another item.")

    def buy_item(self, item, player, store):
        """
            Add an item bought from the store to the backpack.
        :param item: an instance of Item class
        :param player: an instance of Player class
        :param store: an instance of Store class
        :return:
        """
        if self.backpack["Weight"] + item.weight < self.capacity:
            if player.money >= item.price:
                #But the item if the player has enough capacity and money
                store.sell_item(item)
                self.inventory.append(item)
                self.backpack['Items'].append({"Name": item.name, "Price": item.price})
                self.backpack['Weight'] += item.weight
                player.money -= item.price
                self.textUI.print_to_textUI(f"An item added to your inventory: {self.get_inventory()}")
            else:
                #Do not buy, if the money is not enough
                self.textUI.print_to_textUI("You do not have enough money to buy this item!")
        else:
            #Do not buy, if the current capacity is not enough
            self.textUI.print_to_textUI(f"The backpack can only carry up to {self.capacity}kg!")
            self.textUI.print_to_textUI("Your backpack is full! You cannot add another item.")

    def remove_item(self, item):
        """
            Remove a given item from the backpack.
        :param item: an instance of Item class
        :return: None
        """
        self.backpack['Items'].remove({"Name": item.name, "Price": item.price})
        self.backpack['Weight'] -= item.weight
        self.inventory.remove(item)
