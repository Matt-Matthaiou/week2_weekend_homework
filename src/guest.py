class Guest:

    def __init__(self, name, age, cash, favourite_song, club_membership):
        self.name = name
        self.age = age
        self.cash = cash
        self.favourite_song = favourite_song
        self.club_membership = club_membership

    #pay the bill 
    def pay_for_karaoke(self, amount):
        self.cash -= amount