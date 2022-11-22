from TextUI import TextUI

"""
    Create a player with a name given.
    If a name is not provided, names it 'noname' by default.
"""
class Player:

    def __init__(self, name="noname"):
        """
            Inıtialise a player.
        :param name: name of the player, if not given noname
        """
        self.name = name
        self.money = 5
        self.textUI = TextUI()

    def get_money(self):
        """
            Fetch the money of the player.
        :return: None
        """
        self.textUI.print_to_textUI(f"Your money: {str(self.money)}£")

