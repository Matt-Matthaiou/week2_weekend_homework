from src.guest import Guest

class Bar:

    def __init__(self, drinks, food):
        self.drinks = drinks
        self.food = food
    
    def sell_drink(self, drink):
        if drink in self.drinks.keys():
            return self.drinks[drink]
        
    def sell_food(self, food):
        if food in self.food.keys():
            return self.food[food]


