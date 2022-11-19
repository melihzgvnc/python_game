from TextUI import TextUI

class Backpack:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.backpack = {"Items": [], "Weight": 0}
        self.inventory = []
        self.textUI = TextUI()

    def get_inventory(self):
        return self.backpack

    def remove_item(self, item):
        self.backpack['Items'].remove(item.name)
        self.backpack['Weight'] -= item.weight
        self.inventory.remove(item)

    def get_item(self, second_word):
        for item in self.inventory:
            if second_word == item.name:
                return item

    def add_item(self, item, room):
        if self.backpack["Weight"] + item.weight < self.capacity:
            self.inventory.append(item)
            self.backpack['Items'].append(item.name)
            self.backpack['Weight'] += item.weight
            self.textUI.print_to_textUI(f"An item added to your inventory: {self.get_inventory()}")
            room.remove_item(item)
        else:
            self.textUI.print_to_textUI(f"The backpack can only carry up to {self.capacity}kg!")
            self.textUI.print_to_textUI("Your backpack is full! You cannot add another item.")

    def buy_item(self, item, player, store):
        if self.backpack["Weight"] + item.weight < self.capacity:
            if player.money >= item.price:
                store.sell_item(item)
                self.inventory.append(item)
                self.backpack['Items'].append(item.name)
                self.backpack['Weight'] += item.weight
                player.money -= item.price
                self.textUI.print_to_textUI(f"An item added to your inventory: {self.get_inventory()}")
            else:
                self.textUI.print_to_textUI("You do not have enough money to buy this item!")
        else:
            self.textUI.print_to_textUI(f"The backpack can only carry up to {self.capacity}kg!")
            self.textUI.print_to_textUI("Your backpack is full! You cannot add another item.")
