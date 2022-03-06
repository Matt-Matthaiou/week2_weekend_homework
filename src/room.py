class Room:

    def __init__(self, capacity, song_list, till, bar):
        self.capacity = capacity
        self.song_list = song_list
        self.till = till
        self.bar = bar
        self.current_guests = []
        self.guest_tab = {}

    def check_guest_in_room(self, guest):
        if len(self.current_guests) < self.capacity:
            self.current_guests.append(guest)
            self.guest_tab[guest] = 10
            
            if guest.favourite_song in self.song_list:
                return "Whooooo!!"
        else:
            return "Sorry we are full"

    def checkout_guest(self, guest):
        self.current_guests.remove(guest)
        guest.pay_for_karaoke(self.guest_tab[guest])
        self.till += self.guest_tab[guest]
        self.guest_tab.pop(guest)


    def add_song(self, song):
        self.song_list.append(song)

    def add_money_to_till(self, amount):
        self.till += amount

    def add_amount_to_guest_tab(self, guest, amount):
        self.guest_tab[guest] += amount
        
    def sell_drink_to_guest(self, guest, drink):
        price = self.bar.sell_drink(drink)
        self.add_amount_to_guest_tab(guest, price)

    def sell_food_to_guest(self, guest, food):
        price = self.bar.sell_food(food)
        self.add_amount_to_guest_tab(guest, price)

    
        