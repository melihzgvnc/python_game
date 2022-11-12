from Room import Room
from TextUI import TextUI

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
        self.create_rooms()
        self.current_room = self.lobby
        self.textUI = TextUI()

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
        self.thefinish = Room("in the finish")


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
        self.textUI.print_to_textUI("You are lost. You are alone. You wander")
        self.textUI.print_to_textUI("around the deserted complex.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit']

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
        self.textUI.print_to_textUI("You are lost. You are alone. You wander")
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
            self.current_room = next_room
            self.textUI.print_to_textUI(self.current_room.get_long_description())

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
