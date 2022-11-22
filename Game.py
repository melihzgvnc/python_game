from Room import Room
from TextUI import TextUI
from Item import Item
from Player import Player
from Store import Store
from Backpack import Backpack

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game. Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.
    
    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game. It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage.
"""

class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.textUI = TextUI()
        self.create_rooms()
        self.create_items()
        self.create_notices()
        self.store = Store()
        self.create_items_on_sale()
        self.current_room = self.entrance
        self.backpack = Backpack()

    def create_items_on_sale(self):
        """
            Sets up the items on sale.
        :return: None
        """
        self.key = Item("key", 0.2, 8)
        self.store.add_item(self.key)

    def create_player(self):
        """
            Create the player instance.
        :return: None
        """
        try:
            #self.player = Player(input("Name your character: "))
            name = input("Name your character: ")
            if name.isidentifier() == False:
                raise Exception()
            else:
                self.player = Player(name)
        except:
            self.textUI.print_to_textUI("Name cannot contain space or start with a number!")
            return False
    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """

        self.entrance = Room("in the Entrance")
        self.subterr_chamber = Room("in the Subterranean Chamber")
        self.kings_chamber = Room("in the King's Chamber")
        self.grand_gallery = Room("in the Grand Gallery")
        self.cavity = Room("in the Cavity")
        self.queens_chamber = Room("in the Queen's Chamber")
        self.desc_passage = Room("in the Descending Passage")
        self.hall = Room("in the Hall")
        self.pit = Room("in the Pit")
        self.robbers_corr = Room("in the Robbers' Corridor")
        self.sarcophagus = Room("in the Sarcophagus")
        self.exit = Room("in the Exit", unlocked=False)

        self.entrance.set_exit("north", self.subterr_chamber)
        self.entrance.set_exit("west", self.kings_chamber)
        self.entrance.set_exit("south", self.grand_gallery)
        self.subterr_chamber.set_exit("west", self.cavity)
        self.subterr_chamber.set_exit("south", self.entrance)
        self.kings_chamber.set_exit("west", self.sarcophagus)
        self.sarcophagus.set_exit("east", self.kings_chamber)
        self.kings_chamber.set_exit("south", self.desc_passage)
        self.kings_chamber.set_exit("east", self.entrance)
        self.grand_gallery.set_exit("upstairs", self.hall)
        self.grand_gallery.set_exit("north", self.entrance)
        self.hall.set_exit("north", self.robbers_corr)
        self.hall.set_exit("south", self.pit)
        self.hall.set_exit("downstairs", self.grand_gallery)
        self.robbers_corr.set_exit("north", self.queens_chamber)
        self.robbers_corr.set_exit("south", self.hall)
        self.cavity.set_exit("east", self.subterr_chamber)
        self.queens_chamber.set_exit("south", self.robbers_corr)
        self.pit.set_exit("north", self.hall)
        self.desc_passage.set_exit("north", self.kings_chamber)
        self.desc_passage.set_exit("south", self.exit)
        self.exit.set_exit("north", self.desc_passage)

    def create_items(self):
        """
            Create all item instances and put them into rooms.
        :return: None
        """

        self.bracelet = Item('bracelet', 0.5, 5)
        self.queens_chamber.set_item(self.bracelet)

    def create_notices(self):
        """
            Set up notices and place them into rooms
        :return: None
        """
        self.subterr_chamber.set_notice("I saw something shining upstairs. It seemed valuable!")

    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        self.textUI.print_to_textUI(self.current_room.get_long_description())
        self.textUI.print_to_textUI(self.current_room.print_items())
        name = self.create_player()
        while name == False:
            name = self.create_player()
        finished = False
        while not finished:  # while (finished == False):
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
            if self.current_room == self.exit:
                self.print_congratulation()
                finished = True
        print("Thank you for playing!")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        self.textUI.print_to_textUI("You are lost. You are alone. You wander")
        self.textUI.print_to_textUI("around the deserted complex.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: A list of the available commands.
        """
        return ['help', 'go', 'collect', 'remove', 'show', 'unlock', 'read', 'quit']

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.do_go_command(second_word)
        elif command_word == "COLLECT":
            self.do_collect_command(second_word)
        elif command_word == "SHOW":
            self.do_show_command(second_word)
        elif command_word == "REMOVE":
            self.do_remove_command(second_word)
        elif command_word == "READ":
            self.do_read_command(self.current_room)
        elif command_word == "QUIT":
            want_to_quit = True
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Don't know what you mean.")

        return want_to_quit

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI(f"You are lost {self.player.name}. You are alone. You wander")
        self.textUI.print_to_textUI("around the deserted complex.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def print_congratulation(self):
        """
            Display a congratulation message for the player who have completed the game.
        :return: None
        """
        self.textUI.print_to_textUI("congratssss")

    def do_go_command(self, second_word):
        """
            Go towards desired direction.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Go where?")
            return

        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_to_textUI("There is no door!")
        else:
            if next_room.unlocked == True:
                self.current_room = next_room
                self.textUI.print_to_textUI(self.current_room.get_long_description())
                self.textUI.print_to_textUI(self.current_room.print_items())
                if self.current_room.notice != None:
                    self.textUI.print_to_textUI("A notice! It might be helpful if you read.")

            else:
                if self.key in self.backpack.inventory:
                    self.textUI.print_to_textUI("You have the key. Unlock it now!")
                    command, _ = self.textUI.get_command()
                    if command.upper() == "UNLOCK":
                        self.do_unlock_command(next_room, self.key)
                    else:
                        self.textUI.print_to_textUI("Don't know what you mean!")
                else:
                    self.textUI.print_to_textUI("It's locked. You must have the key!")

    def do_unlock_command(self, next_room, item):
        """
            Unlock the locked room.
        :param next_room: a room object the player will go into
        :param item: an instance of Item class which will be used to unlock the room
        :return: None
        """
        next_room.unlocked = True
        self.current_room = next_room
        self.backpack.remove_item(item)
        self.textUI.print_to_textUI("The door has been opened!")
        self.textUI.print_to_textUI(self.current_room.get_long_description())
        self.textUI.print_to_textUI(self.current_room.print_items())
        if self.current_room.notice != None:
            self.textUI.print_to_textUI("A notice! It might be helpful if you read.")

    def do_read_command(self, current_room):
        """
            Read the notice.
        :param current_room: the instance of Room class where the player is in
        :return: Nonw
        """
        self.textUI.print_to_textUI(current_room.get_notice())

    def do_collect_command(self, second_word):
        """
            Collect an item that exists in a room.
        :param second_word: the name of an item the player wishes to collect
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Collect what?")
            return

        if self.current_room.check_item(second_word):
            current_item = self.current_room.get_item(second_word)
            self.backpack.add_item(current_item, self.current_room)
        else:
            self.textUI.print_to_textUI("There is no such item here!")

    def do_show_command(self, second_word):
        """
            Show the inventory, money the player currently have or enter the store.
        :param second_word: the name of an instance the player want to display
        :return: None
        """
        if second_word.upper() == "INVENTORY":
            if len(self.backpack.inventory) >= 1:
                self.textUI.print_to_textUI(f"Your items: {self.backpack.get_inventory()}")
            else:
                self.textUI.print_to_textUI("Your backpack is empty!")

        elif second_word.upper() == 'MONEY':
            self.player.get_money()

        elif second_word.upper() == 'STORE':
            command_word = ""
            while command_word.upper() != "EXIT":
                self.textUI.print_to_textUI(f"Items on sale: {self.store.get_items()}")
                self.textUI.print_to_textUI(f"You have {self.player.get_money()}")
                self.textUI.print_to_textUI("Is there anything you want to buy or sell? If no, you can exit.")
                command_word, second_word = self.textUI.get_command()
                if command_word.upper() == "BUY":
                    self.do_buy_command(second_word)
                elif command_word.upper() == "EXIT":
                    self.textUI.print_to_textUI(self.current_room.get_long_description())
                    self.textUI.print_to_textUI(self.current_room.print_items())
                elif command_word.upper() == "SELL":
                    self.do_sell_item(second_word)
                else:
                    self.textUI.print_to_textUI("Don't know what you mean!")
                    self.textUI.print_to_textUI("You can buy or sell an item.")
        else:
            self.textUI.print_to_textUI("You can show the store, your money or your inventory!")

    def do_buy_command(self, second_word):
        """
            Buy a desired item from the store.
        :param second_word: the name of an item instance the player tries to buy
        :return: None
        """
        item_bought = self.store.get_item(second_word)
        if item_bought == None:
            self.textUI.print_to_textUI("Sorry, couldn't find what you want.")
        else:
            self.backpack.buy_item(item_bought, self.player, self.store)

    def do_remove_command(self, second_word):
        """
            Remove an item given from the player's backpack.
        :param second_word: the name of an item instance the player
        want to remove from its backpack
        :return: None
        """
        current_item = self.backpack.get_item(second_word)

        if current_item in self.backpack.inventory:
            self.backpack.remove_item(current_item)
            self.textUI.print_to_textUI(f"{current_item.name} is removed. Your backpack's current weight is {self.backpack.backpack['Weight']}kg.")
            self.current_room.set_item(current_item)
        else:
            self.textUI.print_to_textUI(f"There isn't any {second_word} in your inventory!")

    def do_sell_item(self, second_word):
        """
            Sell an item given.
        :param second_word: the name of item
        :return: None
        """
        item = self.backpack.get_item(second_word)
        if item != None:
            self.store.add_item(item)
            self.backpack.remove_item(item)
            self.player.money += item.price

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
