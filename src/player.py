# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []


    def move(self, direction):
        if getattr(self.currentRoom, f"{direction}_to") is not None:
            self.currentRoom = getattr(self.currentRoom, f"{direction}_to")
            print(self.currentRoom)
        else:
            print("Sorry the next room is locked")