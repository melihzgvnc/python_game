class Player:

    def __init__(self, name="noname"):
        self.name = name
        self.money = 5

    def get_money(self):
        return str(self.money)+"£"
