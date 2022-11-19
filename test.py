import unittest
from Player import Player
from Item import Item
from TextUI import TextUI
from Store import Store
from Room import Room
from Backpack import Backpack


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_player(self):
        self.assertEqual(self.player.get_money(), str(self.player.money)+"£")


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item("apple", 5, 5)

    def test_item(self):
        test_var = {self.item.name: self.item.weight}
        self.assertEqual(self.item.get_description(), test_var)


class TestTextUI(unittest.TestCase):

    def setUp(self):
        self.textUI = TextUI()

    def test_textUI(self):
        self.assertIsNone(self.textUI.print_to_textUI("trial"))
        #self.assertIsNotNone(self.textUI.get_command())


class TestStore(unittest.TestCase):

    def setUp(self):
        self.store = Store()
        self.item = Item("apple", 5, 5)

    def test_store(self):
        self.store.add_item(self.item)
        self.assertIn(self.item, self.store.all_items)
        self.assertIn(self.item.name, self.store.on_sale.keys())

        test_var = self.store.get_item("apple")
        self.assertEqual(self.store.get_item("apple"), test_var)

        self.store.sell_item(self.item)
        self.assertNotIn(self.item.name, self.store.on_sale.keys())

        self.assertIsNone(self.store.get_item("apple"))

        self.assertIsNotNone(self.store.get_items())


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("test_room")
        self.room2 = Room("test_room2")
        self.item = Item("apple", 5, 5)

    def test_room(self):
        self.room.set_item(self.item)
        self.assertIn(self.item, self.room.items)
        self.assertIn(self.item.name, self.room.item_names)

        self.assertEqual(self.room.get_item("apple"), self.item)

        self.room.del_item(self.item)
        self.assertNotIn(self.item, self.room.items)
        self.assertNotIn(self.item.name, self.room.item_names)

        self.assertFalse(self.room.check_item(self.item.name))

        self.assertIsNotNone(self.room.print_items())

        self.room.set_exit("north", self.room2)
        self.assertEqual(self.room.exits["north"], self.room2)

        self.assertIsNotNone(self.room.get_long_description())
        self.assertIsNotNone(self.room.get_short_description())

        self.assertIsNotNone(self.room.get_exits())

        self.assertIsNotNone(self.room.get_exit("north"))
        self.assertIsNone(self.room2.get_exit("north"))


class TestBackpack(unittest.TestCase):

    def setUp(self):
        self.backpack = Backpack()
        self.room = Room("test_room")
        self.item = Item("apple", 1, 1)
        self.item_bought = Item("banana", 1, 1)
        self.room.set_item(self.item)
        self.player = Player()
        self.store = Store()
        self.store.add_item(self.item_bought)

    def test_backpack(self):
        self.assertIsNotNone(self.backpack.get_inventory())

        self.backpack.add_item(self.item, self.room)
        self.assertIn(self.item, self.backpack.inventory)
        self.assertIn(self.item.name, self.backpack.backpack["Items"])

        self.backpack.buy_item(self.item_bought, self.player, self.store)
        self.assertIn(self.item_bought, self.backpack.inventory)
        self.assertIn(self.item_bought.name, self.backpack.backpack["Items"])

        self.backpack.remove_item(self.item)
        self.assertNotIn(self.item, self.backpack.inventory)
        self.assertNotIn(self.item.name, self.backpack.backpack["Items"])


if __name__ == '__main__':
    unittest.main()
