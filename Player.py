class Player:

    def __init__(self, name):
        self.name = name
        self.backpack = {"Items": [], "Weight": 0}
        self.inventory = []

    def get_inventory(self):
        return self.backpack

    def get_item(self, second_word):
        for item in self.inventory:
            if second_word == item.name:
                return item

    def remove_item(self, item):
        self.backpack['Items'].remove(item.name)
        self.backpack['Weight'] -= item.weight
        self.inventory.remove(item)