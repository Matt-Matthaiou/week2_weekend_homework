class Room:

    def __init__(self, capacity, song_list, till, bar):
        self.capacity = capacity
        self.song_list = song_list
        self.till = till
        self.bar = bar
        self.current_guests = []
        self.guest_tab = {}

    def check_guest_in_room(self, guest):
        if len(self.current_guests) < self.capacity: #checks that there is space in the room
            self.current_guests.append(guest)
            self.guest_tab[guest] = 10 #adds entry fee to the guest's tab
            
            if guest.favourite_song in self.song_list: 
                return "Whooooo!!"  #the guest is happy at check in if his/her favourite song in list
        else:
            return "Sorry we are full"

    def checkout_guest(self, guest):
        total_amount = self.guest_tab[guest]
        if self.does_guest_have_club_membership(guest): #checks if customer has club membership
            discount = self.guest_tab[guest] * 10 / 100#applies discount 10%
            total_amount -= discount                   #
        self.current_guests.remove(guest)
        guest.pay_for_karaoke(total_amount)
        self.till += total_amount
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

    #lets the owner know at the end of the nnight what VAT he/she needs to pay from the earnings
    def pay_VAT_for_the_day(self):
        vat = self.till * 20 / 100
        self.till = self.till - vat
        return f"the vat is: {vat} and the profit for the night is: {self.till}"

    def does_guest_have_club_membership(self, guest):
        return guest.club_membership

    

    

    

    
        

    
        