class Game:
    #Constructor
    def __init__(self,name,genre,rating):
        self.name=name
        self.genre=genre
        self.rating=rating
    #function
    def describe(self):
        print(f"Name: {self.name} || Genre: {self.genre} || Rating: {self.rating}")
    
games=[Game("Katana Zero","Indie",5),Game("GTA VC","Shooter/Crime",4.8),Game("Chess","Casual/Logic",4.5)]
for Game_name in games:
    Game_name.describe()

# Name: Katana Zero || Genre: Indie || Rating: 5
# Name: GTA VC || Genre: Shooter/Crime || Rating: 4.8
# Name: Chess || Genre: Casual/Logic || Rating: 4.5


# ** Process exited - Return Code: 0 **
