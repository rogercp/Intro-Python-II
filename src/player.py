# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name, current_room, inventory=[]):
        self.current_room = current_room
        self.name = name
        self.inventory = inventory

    def print_inventory(self):
        if len(self.inventory) < 1:
            return f'----- inventory:[empty]'
        else:
            return ', '.join(str(i) for i in self.inventory)

    def move(self, direction):
        if getattr(self.current_room, f"{direction}") is not None:
            self.current_room = getattr(self.current_room, f"{direction}")
        else:
            print("------- sorry next room is locked")

    def pick_up_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)





