from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


item = {
    'stick': Item("stick",
                    """with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsu""" ),

    'book': Item("book", """with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsu"""),

    'sword': Item("sword", """with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsu"""),

    'compass':  Item("compass", """with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsu"""),

    'bow': Item("bow", """with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsu"""),
}
# for key,value in room.items():
#     print(f"{key} :{value}")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room["outside"].items = [item["stick"], item["bow"], item["compass"]]
room["foyer"].items = [item["book"], item["sword"]]
room["overlook"].items = [item["sword"], item["compass"], item["bow"]]
room["narrow"].items = [item["bow"]]
room["treasure"].items = [item["compass"]]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Kevin Van Nord", room["outside"],[item["book"],item["sword"]])
directions = ["n", "w", "s", "e"]

current_room = player1.currentRoom
current_inventory = player1.inventory
print(current_room)
print(current_inventory)



while True:
    command = input("where to go?---->")
    if command in directions:
        player1.move(command)
    elif command == "q":
        exit()
    else:
        print("command not recognized")





# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


