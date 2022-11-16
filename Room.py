"""
    Create a room described "description". Initially, it has
    no exits. The 'description' is something like 'kitchen' or
    'an open court yard'.
"""

class Room:

    def __init__(self, description, unlocked=True):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
        self.exits = {}  # Dictionary

        self.unlocked = unlocked
        self.items = [] #item instances
        self.item_names = [] #names of the item instances

    def set_item(self, item):
        self.items.append(item)
        self.item_names.append(item.name)
    def get_item(self, second_word):
        for item in self.items:
            if second_word == item.name:
                return item

    def del_item(self, item):
        self.items.remove(item)
        self.item_names.remove(item.name)

    def remove_item(self, item):
        for item in self.items:
            self.items.remove(item)
            self.item_names.remove(item.name)

    def check_item(self, name):
        names = []
        for item in self.items:
            names.append(item.name)
        if name in names:
            return True
        else:
            return False
    def print_items(self):

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
