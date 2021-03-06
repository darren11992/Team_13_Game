import datetime
import random
import time
import sys
from roomsgit import rooms
from player import *
from gameparser import *
from Bars import *


#rap = current_room["rap"]   # finds the relative rap from the room that you're in
#n = current_room["n"]   # this is the time limit you get for rapping in the current
global a
a = 0.75  # CHANGE THIS BACK

def slow_type(statement, typing_speed):
    for letter in statement:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    #print("")

def screen_menu():
    """First menu when the game is executed. Appears once."""
    slow_type("\n" + "\n" + "RAPPING GAME (title in progress)" + "\n" + "\n" + "\n" + "Your goal is to become the best rapper, surpassing even that of Eminem." + "\n", 200)
    slow_type("The more items you pick up, the lower your overall score will be - the lower the score the better!" + "\n", 200)
    slow_type("Also, the less rappers you have to destroy, the better your overall score will be." + "\n" + "\n", 200)
    difficulty = input("easy / medium / hard: ")
    global a
    if difficulty == "easy":
        a = 1.5
    elif difficulty == "medium":
        a = 1.0
    elif difficulty == "hard":
        a = 0.75
    else:
        print("That's not an option")
        difficulty = input("easy/medium/hard: ")


def calculate_reputation(inventory):
    """Calculate reputation and returns it via players inventory."""
    # reputation = 0 #resets reputation of the player
    reputation = 0
    for item in inventory:  # iterates through every item in the players inventory (see player.py)
        reputation = reputation + item["reputation"]  # Reputation is added to by each item
    return reputation  # The total rep is returned to the function that called it (probs the battle one.)


def produce_bar():
    """Return a random bar depending on the difficulty for the battle."""
    global a
    a = float(a)
    length = len(difficulty_dict[a])
    choice = random.randrange(0, length)
    return difficulty_dict[a][choice]


def battle():
    """Function that completes battle, takes a timed input, gives player item etc."""
    global a
    players_rap = produce_bar()
    print("")
    slow_type("You're in the heat of the battle! You have " + str(int(current_room["room_difficulty"]) * a + int(calculate_reputation(inventory))) + " seconds to show your talent and rap " + "'" + players_rap + "'" +"\n", 200)
    slow_type("You must type word for word, letter for letter." + "\n", 200)
    yes_or_no = input("Ready? y / n: ")
    if yes_or_no == "y":
        z = datetime.datetime.now()  # gets the exact time that the user begins inputting the rap
        rap_input = normalise_input(input(""), True)

        if rap_input == normalise_input(players_rap, True):  # if the user input is exactly what the room's rap is
            b = datetime.datetime.now()  # record the time that the user entered their input
            c = b - z  # work out how long it took the user to input by subtracting the start time from the end time
            divmod(c.days * 86400 + c.seconds, 60)  # this formats the time into something that can be used in an if statement
            d = current_room["room_difficulty"] * a
            total_time = d + int(calculate_reputation(inventory))
            if c.seconds > total_time:  # if the user time is larger than what the room's allocated time is
                slow_type("You didn't rap fast enough!", 50)
                slow_type("That took you " + str(c.seconds) + " seconds, which is " + str(c.seconds - total_time) + " seconds more than it should have." + "\n" + "Maybe you should try some other rappers first to build up your reputation?", 100)
            else:
                slow_type("You showed your rapping skills and won the rap battle!" + "\n", 200)
                current_room["rapperbeat"] = True
                slow_type("That took you " + str(c.seconds) + " seconds." + "\n", 200)
                inventory.append(current_room["award"])
                slow_type("Winning the rap battle got you a " + current_room["award"]["name"] + "." + "\n", 150)
                slow_type("This " + current_room["award"]["id"] + " gives you an extra " + str(current_room["award"]["reputation"]) + " reputation.", 150)
                slow_type("This now makes your total reputation " + str(calculate_reputation(inventory)) + ".", 150)
        else:
            slow_type("You didn't rap the right words, and flopped in the battle.", 150)
    else:
        slow_type("You pussied out of the fight and got thrown out of the club", 150)


def print_inventory_items(players_items):
    """Prints a list of inventory items."""
    if len(players_items) == 0:
        slow_type("You currently have no items", 200)
    else:
        slow_type("You have" + list_of_items(players_items) + ".", 200)


def list_of_items(items):
    """Returns a string with all the players items in a list."""
    full_list = ""
    i = 0
    for item in items:
        if i == 0:
            full_list = full_list + item["name"]
            i =+ 1
        else:
            full_list = full_list + ", " + item["name"]
    return full_list


def print_room(current_room):
    """Prints the description of the current room."""
    print("")
    slow_type(current_room["name"].upper(), 300)
    print("")
    slow_type(current_room["description"], 300)
    print("")


def exit_leads_to(exits, direction):
    """Returns exits of a room."""
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads):
    """Tells the user about an exit."""
    slow_type("\n""GO " + direction.upper() + " to " + leads + ".", 250)


def print_menu(exits):
    """Prints the list of options for the user to choose."""
    print_inventory_items(inventory)
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    if current_room["rapperbeat"] == False:
        if len(current_room["rapper"]) != 0:
            slow_type("\n"+"Battle " + current_room["rapper"], 250)
    else:
        print("")
        print("")


def execute_command(command):
    """Sends the program to the current execute function."""
    # if 0 == len(command):
    #   return

    # if command[0] == "b":
    # print("hello world")

    if command.split(' ', 1)[0] == "battle":
        if current_room["rapperbeat"] == False:
            if len(current_room["rapper"]) != 0:
                battle()
    elif command.split(' ', 1)[0] == "go":
        execute_go(command.split(' ', 1)[1])
    else:
        print("I don't understand that command")


def execute_go(direction):
    """Sends the user to a new room."""
    global current_room
    if direction in current_room["exits"]:
        a = (current_room["exits"])

        b = a[direction]

        current_room = rooms[b]

    else:
        print("You need to pick a valid direction")


def menu(exits):
    """Produces the menu via print_menu and takes the user's input."""
    print_menu(current_room["exits"])
    user_input = input("> ")
    if user_input == "q":
        raise SystemExit()
    else:
        return user_input


def main():
    """The main program that controls the flow of the program."""
    screen_menu()
    while True:

        print_room(current_room)
        command = menu(current_room["exits"])
        # print_menu(current_room["exits"])
        execute_command(command)
        # battle(n, current_room)
        calculate_reputation(inventory)
        if item_tattoo in inventory:
            slow_type("You have beaten one of the greatest rappers ever and performed for thousands," + "\n" + "You win.", 300)
            break

main()
