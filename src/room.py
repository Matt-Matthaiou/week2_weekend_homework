class Room:

    def __init__(self, capacity, song_list, till):
        self.capacity = capacity
        self.song_list = song_list
        self.till = till
        self.current_guests = []

    def check_guest_in_room(self, guest):
        if len(self.current_guests) < self.capacity:
            self.current_guests.append(guest)
            guest.pay_for_karaoke(10)
            self.add_money_to_till(10)
        else:
            return "Sorry we are full"

    def checkout_guest(self, guest):
        self.current_guests.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def add_money_to_till(self, amount):
        self.till += amount


        