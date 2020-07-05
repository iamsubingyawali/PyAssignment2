class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.lives = 0
        self.dress_color = 'blue'

    def change_dress_color(self, color):
        self.dress_color = color

    def decrease_life(self):
        self.lives = self.lives - 1

    def increase_life(self):
        self.lives = self.lives + 1

    def add_coins(self, coins):
        self.coins = self.coins + coins

    def change_player_name(self, name):
        self.name = name


new_player = Player('Mario Player')
new_player.increase_life()
new_player.add_coins(1000)
print(new_player.name, new_player.coins, new_player.lives)
