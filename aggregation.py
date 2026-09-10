class Game:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def describe(self):
        print(f"{self.name} - {self.genre}")


class Game_Library:
    # Aggregation:
    # Aggregation is a HAS-A relationship where one class
    # contains/uses objects of another class, but the contained
    # objects can exist independently of the container.
    #
    # Game_Library HAS-A collection of Game objects.

    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def show_games(self):
        for game in self.games:
            game.describe()


# Game objects are created independently of Game_Library.
game1 = Game("GTA VC", "Crime")
game2 = Game("RDR2", "Action")


# Now the Game objects are added to the library.
library = Game_Library()

library.add_game(game1)
library.add_game(game2)

library.show_games()
