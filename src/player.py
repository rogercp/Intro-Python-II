# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def __str__(self):
        return (f"{self.name} is currently in room{self.currentRoom}")

    def __repr__(self):
        return (f"{self.name}:{self.currentRoom}")

