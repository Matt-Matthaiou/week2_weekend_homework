import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(5, ["Ace's high", "Master of puppets", "Azrael"])

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def  test_room_has_songs(self):
        self.assertEqual("Ace's high", self.room.song_list[0])
        self.assertEqual("Master of puppets", self.room.song_list[1])
        self.assertEqual("Azrael", self.room.song_list[2])