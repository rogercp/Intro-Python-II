from player import Player
from room import Room
from item import Item
from dictionaries import *


player = Player("Kevin Van Nord",room["outside"],[item['axe'],item['helmet']])

directions = ["n", "w", "s", "e"]


while True:
    print("\n//////////////")
    print("You can: Enter in direction letter to move north(n), east(e), south(s), west(w)")
    print("Enter 'pickup' or 'drop' to select items,then type in the item name enter 'q' to quit game")
    print("//////////////\n")
    print(f"player ------ {player.name}")
    print(f"location {player.current_room}")
    print(f"room items -----", player.current_room.current_items())
    print("inventory -----", player.print_inventory())

    command = input("Pick an action:").lower().strip()

    if command == "q":
        quit()
    elif command in directions:
        player.move(f"{command}_to")

    elif command == "pickup":
        print(player.current_room.current_items())
        cmd = input("Pickup an item from room:").lower().strip()
        item_names = [item.name_of_item for item in player.current_room.items_stored]
        if cmd in item_names:
            player.pick_up_item(item[cmd])
            player.current_room.remove_item(item[cmd])
        else:
            print("\n>>>>>>that is not an item in this room")

    elif command == "drop":
        print(player.print_inventory())
        cmd = input("Drop item from your inventory:").lower().strip()
        item_names = [item.name_of_item for item in player.inventory]
        if cmd in item_names:
            player.drop_item(item[cmd])
            player.current_room.placed_item(item[cmd])
        else:
            print("\n>>>>>>that is not an item in your inventory")

    else:
        print("-----------command is not recognized-----------")






