import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ace's high", 4.12)

    def test_song_has_name(self):
        self.assertEqual("Ace's high", self.song.title)

    def test_song_has_duration(self):
        self.assertEqual(4.12, self.song.duration)