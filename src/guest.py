class Guest:

    def __init__(self, name, age, cash, favourite_song):
        self.name = name
        self.age = age
        self.cash = cash
        self.favourite_song = favourite_song

    def pay_for_karaoke(self, amount):
        self.cash -= amount