import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest
from src.bar import Bar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.bar = Bar({"beer": 3, "wine": 3, "soft_drinks": 2, "spirits": 4}, {"burger": 5, "hot dog": 3, "dirty fries": 4})
        self.song1 = Song("Ace's high", 4.12)
        self.song2 = Song("Master of puppets", 5.23)
        self.song3 = Song("Azrael", 6.10)
        self.song4 = Song("Rock n roll", 2.57)
        self.room = Room(2, [self.song1, self.song2, self.song3], 10, self.bar)
        self.guest1 = Guest("Matt", 35, 50, self.song1)
        self.guest2 = Guest("Lemmy", 60, 100, self.song4)
        self.guest3 = Guest("Argiris", 58, 10, "Children of the sun")
        


    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def  test_room_has_songs(self):
        self.assertEqual(self.song1, self.room.song_list[0])
        self.assertEqual(self.song2, self.room.song_list[1])
        self.assertEqual(self.song3, self.room.song_list[2])
    
    def test_check_guest_in_room(self):
        guest_shout = self.room.check_guest_in_room(self.guest1)
        self.assertEqual(self.guest1, self.room.current_guests[0])
        self.assertEqual("Whooooo!!", guest_shout)

    def test_checkout_guest_from_room(self):
        self.room.check_guest_in_room(self.guest1)
        self.room.check_guest_in_room(self.guest2)
        self.room.checkout_guest(self.guest1)
        self.assertEqual(self.guest2, self.room.current_guests[0])

    def test_add_song_to_room(self):
        self.room.add_song(self.song4)
        self.assertEqual(self.song4, self.room.song_list[3])

    def test_capacity_limit(self):
        self.room.check_guest_in_room(self.guest1)
        self.room.check_guest_in_room(self.guest2)
        self.at_capacity = self.room.check_guest_in_room(self.guest3)
        self.assertEqual("Sorry we are full", self.at_capacity)

    def test_guest_charge(self):
        self.room.check_guest_in_room(self.guest1)
        self.room.check_guest_in_room(self.guest2)
        self.assertEqual(10, self.room.guest_tab[self.guest1])
        self.assertEqual(10, self.room.guest_tab[self.guest2])

    def test_sell_drink_to_customer(self):
        self.room.check_guest_in_room(self.guest1)
        self.room.sell_drink_to_guest(self.guest1, "beer")
        self.room.checkout_guest(self.guest1)
        self.assertEqual(37, self.guest1.cash)
        self.assertEqual(23, self.room.till)

    def test_sell_food_to_customer(self):
        self.room.check_guest_in_room(self.guest1)
        self.room.sell_food_to_guest(self.guest1, "dirty fries")
        self.room.checkout_guest(self.guest1)
        self.assertEqual(36, self.guest1.cash)
        self.assertEqual(24, self.room.till)
    

