import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Matt", 35, 50, "Ace's high")
        
    def test_guest_has_a_name(self):
        self.assertEqual("Matt", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guest.age)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.guest.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Ace's high", self.guest.favourite_song)