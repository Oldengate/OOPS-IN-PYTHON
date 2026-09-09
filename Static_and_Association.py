class Game:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def describe(self):
        print(f"Name: {self.name} || Genre: {self.genre} || Rating: {self.rating}")
class Game_Library:
    collection = 0

    def __init__(self):
        self.game_list = []

    def add_game(self, game):
        self.game_list.append(game)
        Game_Library.collection += 1

    def show_games(self):
        if len(self.game_list) == 0:
            print("Library is empty.")
        else:
            for game in self.game_list:
                game.describe()

    def show_count(self):
        print(f"Total games: {Game_Library.collection}")


library = Game_Library()

while True:
    print("\n--- GAME LIBRARY ---")
    print("1. Add game")
    print("2. Show games")
    print("3. Show count")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Game name: ")
        genre = input("Genre: ")
        rating = float(input("Rating: "))

        game = Game(name, genre, rating)
        library.add_game(game)

    elif choice == "2":
        library.show_games()

    elif choice == "3":
        library.show_count()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
