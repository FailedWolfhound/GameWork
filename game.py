#!/usr/bin/python3

from map import rooms
import string


def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    pass # The pass statement does nothing. Replace it with the body of your function.
    
    
def remove_spaces(text):
    """This function is used to remove leading and trailing spaces from a string.
    It takes a string and returns a new string with does not have leading and
    trailing spaces. For example:

    >>> remove_spaces("  Hello!  ")
    'Hello!'
    >>> remove_spaces("  Python  is  easy!   ")
    'Python  is  easy!'
    >>> remove_spaces("Python is easy!")
    'Python is easy!'
    >>> remove_spaces("")
    ''
    >>> remove_spaces("   ")
    ''
    """
    pass


def normalise_input(user_input):
    """This function removes all punctuation, leading and trailing
    spaces from a string, and converts the string to lower case.
    For example:

    >>> normalise_input("  Go south! ")
    'go south'
    >>> normalise_input("!!! tAkE,. LAmp!?! ")
    'take lamp'
    >>> normalise_input("HELP!!!!!!!")
    'help'
    """
    pass

    
def display_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. For example:

    >>> display_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # pass # The pass statement does nothing. Replace it with the body of your function.
    
    





    
def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    pass
    

def print_menu_line(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    Go <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_menu_line("east", "you personal tutor's office")
    Go EAST to you personal tutor's office.
    >>> print_menu_line("south", "Robs' room")
    Go SOUTH to Robs' room.
    """
    pass


def print_menu(exits):
    """This function displays the menu of available exits to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    menu should, for each exit, call the function print_menu_line() to print
    the information about each exit in the appropriate format. The room into
    which an exit leads is obtained using the function exit_leads_to().

    For example, the menu of exits from Reception may look like this:

    You can:
    Go EAST to your personal tutor's office.
    Go WEST to the parking lot.
    Go SOUTH to Robs' room.
    Where do you want to go?
    """
    print("You can:")
    
    # COMPLETE THIS PART:
    # Iterate over available exits:
    #     and for each exit print the appropriate menu line

    print("Where do you want to go?")


def is_valid_exit(exits, user_input):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "user_input" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    pass


def menu(exits):
    """This function, given a dictionary of possible exits from a room, prints the
    menu of exits using print_menu() function. It then prompts the player to type
    a name of an exit where she wants to go. The players's input is normalised
    using the normalise_input() function before further checks are done.  The
    function then checks whether this exit is a valid one, using the function
    is_valid_exit(). If the exit is valid then the function returns the name
    of the chosen exit. Otherwise the menu is displayed again and the player
    prompted, repeatedly, until a correct choice is entered."""

    # Repeat until the player enter a valid choice
    while True:
        pass
        # COMPLETE THIS PART:
        
        # Display menu

        # Read player's input

        # Normalise the input

        # Check if the input makes sense (is valid exit)
            # If so, return the player's choice




def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Robs"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """
    pass


# This is the entry point of our program
def main():
    # Start game at the reception
    current_room = rooms["Reception"]

    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)

        # What are the possible exits from the current room?
        exits = current_room["exits"]

        # Show the menu with exits and ask the player
        direction = menu(exits)

        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
