# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,nameOfRoom ,description):
        self.nameOfRoom = nameOfRoom
        self.description = description

    def __str__(self):
        return (f"{self.nameOfRoom} : {self.description}")

    def __repr__(self):
        return (f"{self.nameOfRoom} : {self.description}")
