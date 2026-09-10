class Game:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Game: {self.name}"

    def __len__(self):
        return len(self.name)

    def __contains__(self, text):
        return text in self.name


game = Game("GTA VC")

print(game)             # __str__()
print(len(game))        # __len__()
print("GTA" in game)    # __contains__()
