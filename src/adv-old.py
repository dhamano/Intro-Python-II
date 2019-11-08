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

def get_input(the_rm):
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
    print(f"You can go: {d}")
    cmd_in = input("action: ")
    return cmd_in

def get_dir(the_input, the_rm):
    if the_input == 'n':
        dir = the_rm.n_to
        if dir != None:
            player.set_current_room(dir)
            cmd_center()
        else:
            print("\n\n\n\nYou can't go that way")
            cmd_center()
    elif the_input == 's':
        dir = the_rm.s_to
        if dir != None:
            player.set_current_room(dir)
            cmd_center()
        else:
            print("\n\n\n\nYou can't go that way")
            cmd_center()
    elif the_input == 'e':
        dir = the_rm.e_to
        if dir != None:
            player.set_current_room(dir)
            cmd_center()
        else:
            print("\n\n\n\nYou can't go that way")
            cmd_center()
    elif the_input == 'w':
        dir = the_rm.w_to
        if dir != None:
            player.set_current_room(dir)
            cmd_center()
        else:
            print("\n\n\n\nYou can't go that way")
            cmd_center()
    else:
        print("\n\n\n\nYou can't go that way")
        cmd_center()

def eval_input(the_input, the_rm):
    global player
    if len(the_input.strip()) == 1:
        get_dir(the_input, the_rm)
    elif len(the_input.strip()) > 1:
        input_arr = the_input.split(" ")
        if len(input_arr) < 2:
            # print("array is one")
            if input_arr[0] == "exit":
                quit()
        else:
            # print("array larger than 2")
            if input_arr[0] == "take" or input_arr[0] == "get":
                print(f"input_arr[1]: {input_arr[1]}")
                cmd_center()
            else:
                print("un-oh! I don\'t know")
                cmd_center()

def setup():
    name = get_name()
    if not name or len(name.strip()) == 0:
        get_name()
    else:
        global player
        player = Player(name, room['outside'])
    cmd_center()

def cmd_center():
    the_rm = player.current_room
    desc = the_rm.desc
    print(f"\n\n\n{desc}")
    the_input = get_input(the_rm)
    if not the_input or len(the_input.strip()) == 0:
        cmd_center()
    else:
        eval_input(the_input, the_rm)

setup()



    # def do_n(self, q):
    #     the_rm = player.current_room
    #     dir = the_rm.n_to
    #     if dir != None:
    #         player.set_current_room(dir)
    #         cmd_center()
    #     else:
    #         print("\n\n\n\nYou can't go that way")
    #         cmd_center()
    
    # def do_s(self, q):
    #     dir = the_rm.s_to
    #     if dir != None:
    #         player.set_current_room(dir)
    #         cmd_center()
    #     else:
    #         print("\n\n\n\nYou can't go that way")
    #         cmd_center()
    
    # def do_e(self, q):
    #     dir = the_rm.e_to
    #     if dir != None:
    #         player.set_current_room(dir)
    #         cmd_center()
    #     else:
    #         print("\n\n\n\nYou can't go that way")
    #         cmd_center()
    
    # def do_w(self, q):
    #     dir = the_rm.w_to
    #     if dir != None:
    #         player.set_current_room(dir)
    #         cmd_center()
    #     else:
    #         print("\n\n\n\nYou can't go that way")
    #         cmd_center()
    
    # def do_exit(self, q):
    #     quit()
    
    # def do_quit(self, q):
    #     quit()