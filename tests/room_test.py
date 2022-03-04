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
        self.guest = Guest("Matt", 35, 50, Song("Ace's high", 4.12))


    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def  test_room_has_songs(self):
        self.assertEqual(self.song1, self.room.song_list[0])
        self.assertEqual(self.song2, self.room.song_list[1])
        self.assertEqual(self.song3, self.room.song_list[2])
    
    def test_check_guest_in_room(self):
        self.room.check_guest_in_room(self.guest)
        self.assertEqual(self.guest, self.room.current_guests[0])
