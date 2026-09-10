class Game:
    total_games = 0

    def __init__(self, name):
        self.name = name
        Game.total_games += 1

    @classmethod
    def show_total(cls):
        # Class method works with the CLASS itself.
        # cls refers to the class, just like self refers to an object.
        print(f"Total games: {cls.total_games}")


g1 = Game("GTA VC")
g2 = Game("RDR2")

Game.show_total()

# Total games: 2


# ** Process exited - Return Code: 0 **
