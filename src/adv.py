from room import Room
from player import Player
from item import Item

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
    'potion': Item('potion', 'Recovers 25 HP'),

    'elixer': Item('elixer', 'Recovers 25 MP'),

    'shield': Item('shield', 'Legendary shield of Zeus'),

    'katana': Item('katana', 'A blade that can cut through anything'),

    'sword': Item('sword', 'Ancient sword from the East'),

    'spear': Item('spear', 'A cursed spear once wielded by ChuCulain'),

    'scroll': Item('scroll', 'A magic book that summons thunder against enemies')
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['treasure'].items_stored = [item['spear'], item['scroll']]
room['foyer'].items_stored = [item['elixer'], item['shield'],item['potion']]
room['narrow'].items_stored = [item['potion'], item['elixer']]
room['overlook'].items_stored = [item['sword'], item['katana']]


player = Player("Kevin Van Nord",room["outside"],[item['katana'],item['sword']])

directions = ["n", "w", "s", "e"]


while True:
    print(f"location {player.current_room}\n")
    print(f"room items:", player.current_room.current_items())
    print("inventory ===", player.print_inventory())
    print("//////////////You can: ")
    print("Enter in direction letter to move north(n), east(e), south(s), west(w)")
    print("Enter 'pickup' or 'drop' to select items")
    print("'q' to quit game//////////////")

    command = input("Pick an action:")

    if command == "q":
        quit()
    elif command in directions:
        player.move(f"{command}_to")
    elif command == "pickup":
        cmd = input("Pickup an item from room:")
        player.pick_up_item(cmd)
        player.current_room.remove_item(item[cmd])
    elif command == "drop":
        cmd = input("Drop item from your inventory:")
        player.drop_item(cmd)
    else:
        print("-------command is not recognized")






