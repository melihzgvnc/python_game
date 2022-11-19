class Store:

    def __init__(self):
        self.on_sale = {}
        self.all_items = []

    def add_item(self, item):
        self.on_sale[item.name] = {"Price": str(item.price)+"£", "Weight": item.weight}
        self.all_items.append(item)

    def sell_item(self, item):
        self.on_sale.pop(item.name)
        self.all_items.remove(item)

    def get_item(self, second_word):
        temp = None
        for item in self.all_items:
            if item.name == second_word:
                temp = item
        if temp == None:
            return None
        else:
            return temp

    def get_items(self):
        return self.on_sale