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
        self.create_player()
        self.create_rooms()
        self.create_items()
        self.store = Store()
        self.create_items_on_sale()
        self.current_room = self.lobby
        self.textUI = TextUI()
        self.backpack = Backpack()

    def create_items_on_sale(self):
        self.glass = Item("glass", 5, 0.5)
        self.store.add_item(self.glass)

    def create_player(self):
        self.player = Player(input("Name your character: "))

    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """

        self.lobby = Room("in the lobby")
        self.room1 = Room("in the room1")
        self.room2 = Room("in the room2")
        self.room3 = Room("in the room3")
        self.room1a = Room("in the room1a")
        self.room1b = Room("in the room1b")
        self.room2a = Room("in the room2a")
        self.room3a = Room("in the room3a")
        self.room3b = Room("in the room3b")
        self.room3c = Room("in the room3c")
        self.cafe = Room("in the cafe")
        self.thefinish = Room("in the finish", unlocked=False)

        self.lobby.set_exit("north", self.room1)
        self.lobby.set_exit("west", self.room2)
        self.lobby.set_exit("south", self.room3)
        self.room1.set_exit("west", self.room1a)
        self.room1.set_exit("east", self.room1b)
        self.room1.set_exit("south", self.lobby)
        self.room2.set_exit("west", self.cafe)
        self.cafe.set_exit("east", self.room2)
        self.room2.set_exit("south", self.room2a)
        self.room2.set_exit("east", self.lobby)
        self.room3.set_exit("east", self.room3a)
        self.room3.set_exit("north", self.lobby)
        self.room3a.set_exit("north", self.room3c)
        self.room3a.set_exit("south", self.room3b)
        self.room3a.set_exit("west", self.room3)
        self.room3c.set_exit("north", self.room1b)
        self.room3c.set_exit("south", self.room3a)
        self.room1a.set_exit("east", self.room1)
        self.room1b.set_exit("south", self.room3c)
        self.room1b.set_exit("west", self.room1)
        self.room3b.set_exit("north", self.room3a)
        self.room2a.set_exit("north", self.room2)
        self.room2a.set_exit("south", self.thefinish)
        self.thefinish.set_exit("north", self.room2a)

    def create_items(self):
        """
            Create all item instances
        :return:
        """
        self.note = Item('note', 0.5, 1)
        self.room1.set_item(self.note)
        self.key = Item('key', 0.5, 2)
        self.room3.set_item(self.key)

    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        finished = False
        while not finished:  # while (finished == False):
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("Thank you for playing!")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return:
        """
        self.textUI.print_to_textUI(f"You are lost {self.player.name}. You are alone. You wander")
        self.textUI.print_to_textUI("around the deserted complex.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'collect', 'remove', 'show', 'unlock', 'quit']

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

    def do_go_command(self, second_word):
        """
            Performs the GO command.
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
            else:
                if self.key in self.player.inventory:
                    self.textUI.print_to_textUI("You have the key. Unlock it now!")
                    command, _ = self.textUI.get_command()
                    if command.upper() == "UNLOCK":
                        self.do_unlock_command(next_room, self.key)
                    else:
                        self.textUI.print_to_textUI("Don't know what you mean!")
                else:
                    self.textUI.print_to_textUI("It's locked. You must have the key!")
    def do_unlock_command(self, next_room, item):
        next_room.unlocked = True
        self.current_room = next_room
        self.player.remove_item(item)
        self.textUI.print_to_textUI("The door has been opened!")
        self.textUI.print_to_textUI(self.current_room.get_long_description())
        self.textUI.print_to_textUI(self.current_room.print_items())

    def do_collect_command(self, second_word):
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
        if second_word.upper() == "INVENTORY":
            if len(self.backpack.inventory) >= 1:
                self.textUI.print_to_textUI(f"Your items: {self.backpack.get_inventory()}")
            else:
                self.textUI.print_to_textUI("Your backpack is empty!")

        elif second_word.upper() == 'STORE':
            command_word = ""
            while command_word.upper() != "EXIT":
                self.textUI.print_to_textUI(f"Items on sale: {self.store.get_items()}")
                self.textUI.print_to_textUI(f"You have {self.player.get_money()}")
                self.textUI.print_to_textUI("Is there anything you want to buy? If no, you can exit.")
                command_word, second_word = self.textUI.get_command()
                if command_word.upper() == "BUY":
                    item_bought = self.store.get_item(second_word)
                    if item_bought == None:
                        self.textUI.print_to_textUI("Sorry, couldn't find what you want.")
                    else:
                        self.backpack.buy_item(item_bought, self.player, self.store)
                elif command_word.upper() == "EXIT":
                    self.textUI.print_to_textUI(self.current_room.get_long_description())
                    self.textUI.print_to_textUI(self.current_room.print_items())
                    return
                else:
                    self.textUI.print_to_textUI("Don't know what you mean!")
        else:
            self.textUI.print_to_textUI("You can only show the store or your inventory!")

    def do_remove_command(self, second_word):
        current_item = self.backpack.get_item(second_word)

        if second_word in self.backpack.backpack['Items']:
            self.backpack.remove_item(current_item)
            self.textUI.print_to_textUI(f"{current_item.name} is removed. Your backpack's current weight is {self.backpack.backpack['Weight']}kg.")
            self.current_room.set_item(current_item)
        else:
            self.textUI.print_to_textUI(f"There isn't any {second_word} in your inventory!")
def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
