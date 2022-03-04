class Room:

    def __init__(self, capacity, song_list):
        self.capacity = capacity
        self.song_list = song_list
        self.current_guests = []

    def check_guest_in_room(self, guest):
        self.current_guests.append(guest)

    def checkout_guest(self, guest):
        self.current_guests.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)


        