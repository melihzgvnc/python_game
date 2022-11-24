"""
    Create a room described "description". Initially, it has
    no exits and is not locked.
"""

class Room:

    def __init__(self, description, unlocked=True):
        """
            Constructor method.
        :param description: Text description for this room
        :param unlocked: True by default, False if room is needed to be locked
        :return: None
        """
        self.description = description
        self.exits = {}  # Dictionary (direction: room)
        self.unlocked = unlocked
        self.items = [] #item instances
        self.item_names = [] #names of the item instances
        self.notice = None

    def set_notice(self, hint):
        """
            Sets up a notice.

        :param hint: a clue the notice contains
        :return: None
        """
        self.notice = hint

    def get_notice(self):
        """
            Gets a notice if exists.
        :return: Notice, a message if not exists
        """
        if self.notice == None:
            return "Nothing to read here!"
        else:
            return self.notice

    def set_item(self, item):
        """
            Put a given item into a room
        :param item: an item instance of Item class
        :return: None
        """
        self.items.append(item)
        self.item_names.append(item.name)

    def get_item(self, second_word):
        """
            Fetch an item.
        :param second_word: the name of an item
        :return: Item if exists, otherwise None
        """
        for item in self.items:
            if second_word == item.name:
                return item


    def remove_item(self, item):
        """
            Delete an item.
        :param item: an item instance of Item class
        :return: None
        """
        for item in self.items:
            self.items.remove(item)
            self.item_names.remove(item.name)

    def check_item(self, name):
        """
            Check the existence of an item by its name given.
        :param name: the name of an item
        :return: True if item exists, False otherwise
        """
        if name in self.item_names:
            return True
        else:
            return False

    def print_items(self):
        """
            Print item(s) in a room.
        :return: Text of items if exists, or a text telling no item in the room
        """
        if len(self.items) == 1:
            return f'There is an item here: {self.item_names[0]}'
        elif len(self.items) > 1:
            return f'There are some items here: {self.item_names}'
        else:
            return 'This room seems to be all empty'

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None
