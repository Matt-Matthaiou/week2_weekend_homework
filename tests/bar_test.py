import unittest
from src.bar import Bar
from src.guest import Guest
from src.song import Song

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar({"beer": 3, "wine": 3, "soft_drinks": 2, "spirits": 4}, {"burger": 5, "hot dog": 3, "dirty fries": 4})
        self.guest = Guest("Matt", 35, 50, Song("whatever", 3.14), True)

    def test_bar_has_drink(self):
        self.assertEqual(4, len(self.bar.drinks))

    def test_bar_has_food(self):
        self.assertEqual(3, len(self.bar.food))
    
    
    
    # test passed to see if the initial function worked to charge the guest for the drink.
    # def test_sell_drink(self):
    #     self.bar.sell_drink(self.guest, "beer")
    #     self.assertEqual(47, self.guest.cash)


    

    