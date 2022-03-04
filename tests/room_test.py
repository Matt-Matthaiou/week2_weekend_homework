import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Ace's high", 4.12)
        self.song2 = Song("Master of puppets", 5.23)
        self.song3 = Song("Azrael", 6.10)
        self.room = Room(5, [self.song1, self.song2, self.song3])
        self.guest1 = Guest("Matt", 35, 50, Song("Ace's high", 4.12))
        self.guest2 = Guest("Lemmy", 60, 100, Song("Rock n roll", 2.57))


    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def  test_room_has_songs(self):
        self.assertEqual(self.song1, self.room.song_list[0])
        self.assertEqual(self.song2, self.room.song_list[1])
        self.assertEqual(self.song3, self.room.song_list[2])
    
    def test_check_guest_in_room(self):
        self.room.check_guest_in_room(self.guest1)
        self.assertEqual(self.guest1, self.room.current_guests[0])

    def test_checkout_guest_from_room(self):
        self.room.check_guest_in_room(self.guest1)
        self.room.check_guest_in_room(self.guest2)
        self.room.checkout_guest(self.guest1)
        self.assertEqual(self.guest2, self.room.current_guests[0])
