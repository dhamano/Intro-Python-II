from room import Room
from player import Player
from item import Item
from cmd import Cmd

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("apple", "Apples are overrated."), Item("note", "A simple missive to nothing.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("old note", "Nothing, nothing, nothing!")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("bucket of gold", "a useless bucket of gold.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
player = {}

def get_name():
    username = input("What's your name? ")
    return username

def setup():
    name = get_name()
    if not name or len(name.strip()) == 0:
        get_name()
    else:
        global player
        player = Player(name, room['outside'])

setup()

def get_directions(the_rm):
    dir = []
    if the_rm.n_to != None:
        dir.append('n')
    if the_rm.w_to != None:
        dir.append('w')
    if the_rm.e_to != None:
        dir.append('e')
    if the_rm.s_to != None:
        dir.append('s')
    d = ", ".join(dir)
    dir = f"You can go: {d}"
    return dir
 
def get_output(dir):
    if dir != None:
        player.set_current_room(dir)
        the_rm = player.current_room
        print(f"\n\n\n{the_rm.desc}\n")
        directions = get_directions(the_rm)
        print(f"{directions}")
    else:
        print("\n\n\nYou can't go that way")

def add_item(verb, q):
    the_rm = player.current_room
    the_items = the_rm.items
    item_to_add = False
    for item in the_items:
        # print(f"ITEM FOR LOOP {item.name} | {q}")
        if item.name == q:
            player.add_item(item)
            the_rm.rem_item(item)
            item_to_add = True
    if not item_to_add:
        print(f"\n\n\nThere is no item called {q}\n\n")
    else:
        print(f"\n\n\nYou {verb} the {q}\n\n")
        # print(f"items: {the_items}")

def get_inventory():
    the_items = player.items
    if len(the_items) < 1:
        print("\n\n\nYou are carrying nothing\n")
    else:
        print("\n\n\nInventory:")
        for i, item in enumerate(the_items, start=1):
            print(f"\t{i}. {item.name}")
        print("\n\n")

class AppCmd(Cmd):
    global player
    the_rm = player.current_room
    prompt = "What do you want to do? "
    dir = get_directions(the_rm)
    intro = f"\n\n\n{the_rm.desc}\n\n{dir}"

    def do_n(self, q):
        the_rm = player.current_room
        dir = the_rm.n_to
        get_output(dir)
    
    def do_s(self, q):
        the_rm = player.current_room
        dir = the_rm.s_to
        get_output(dir)
    
    def do_e(self, q):
        the_rm = player.current_room
        dir = the_rm.e_to
        get_output(dir)
    
    def do_w(self, q):
        the_rm = player.current_room
        dir = the_rm.w_to
        get_output(dir)
    
    def do_get(self, q):
        add_item("get", q)
    
    def do_take(self, q):
        add_item("take", q)
    
    def do_drop(self, q):
        the_rm = player.current_room
        the_items = player.items
        item_to_remove = False
        for item in the_items:
            if item.name == q:
                player.rem_item(item)
                the_rm.add_item(item)
                item_to_remove = True
        if not item_to_remove:
            print(f"\n\n\nThere is no item called {q}\n\n")
        else:
            print(f'\n\n\nYou drop item {q}\n\n')
    
    def do_inventory(self, q):
        get_inventory()
    
    def do_inv(self, q):
        get_inventory()
    
    def do_exit(self, q):
        dir = get_directions(player.current_room)
        print(f"\n\n\n{dir}\n\n")
    
    def do_look(self, q):
        the_rm = player.current_room
        dir = get_directions(the_rm)
        print(f"\n\n\n{the_rm.desc}\n{dir}\n")
        the_items = player.current_room.items
        if len(the_items) < 1:
            print("There is nothing")
        else:
            print(f'')
            print("You also see:")
            for i, item in enumerate(the_items, start=1):
                print(f"\t{i}. {item.name}")
            print("\n")
    
    def do_quit(self, q):
        return True


if __name__ == '__main__':
    AppCmd().cmdloop()