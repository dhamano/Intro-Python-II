from room import Room
from player import Player
from item import Item
from cmd import Cmd

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
        print('getting item')
    
    def do_take(self, q):
        print('taking item')
    
    def do_exit(self, q):
        return True
    
    def do_quit(self, q):
        return True


if __name__ == '__main__':
    AppCmd().cmdloop()