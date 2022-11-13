class Player:

    def __init__(self, name):
        self.name = name
        self.backpack = []

    def get_inventory(self):
        return self.backpack