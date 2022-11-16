class Item:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    def get_description(self):

        return {self.name: self.weight}