import datetime
from roomsgit import rooms
from player import *
from gameparser import *


rap = current_room["rap"] # finds the relative rap from the room that you're in
n = current_room["n"] # this is the time limit you get for rapping in the current
global a
a = 1.0

def screen_menu():
	print("\n" + "\n" + "RAPPING GAME (title in progress)" + "\n" + "\n" + "\n" + "Your goal is to become the best rapper, surpassing even that of Eminem." + "\n")
	print("The more items you pick up, the lower your overall score will be - the lower the score the better!" + "\n")
	print("Also, the less rappers you have to destroy, the better your overall score will be." + "\n" + "\n")
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
    #reputation = 0 #resets reputation of the player
    reputation = 0
    for item in inventory:  #iterates through every item in the players inventory (see player.py)
        reputation = reputation + item["reputation"] #Reputation is added to by each item
    return reputation #The total rep is returned to the function that called it (probs the battle one.)

def battle(n, room):
	global a
	print("")
	print("You're in the heat of the battle! You have " + str(int(current_room["n"]) * a + int(calculate_reputation(inventory)))+ " seconds to show your talent and rap " + "'" + current_room["rap"] + "'")
	print("You must type word for word, letter for letter." + "\n")
	yes_or_no = input("Ready? y / n: ")
	if yes_or_no == "y":
		z = datetime.datetime.now() # gets the exact time that the user begins inputting the rap
		rap_input = normalise_input(input(""), True)
		if rap_input == normalise_input(current_room["rap"], True): # if the user input is exactly what the room's rap is
			b = datetime.datetime.now() # record the time that the user entered their input
			c = b - z # work out how long it took the user to input by subtracting the start time from the end time
			divmod(c.days * 86400 + c.seconds, 60) # this formats the time into something that can be used in an if statement
			d = current_room["n"] * a
			total_time = d + int(calculate_reputation(inventory))
			if c.seconds > total_time: # if the user time is larger than what the room's allocated time is
				print("You didn't rap fast enough!")
				print("That took you " + str(c.seconds) + " seconds, which is " + str(c.seconds - total_time) + " seconds more than it should have." + "\n" + "Maybe you should try some other rappers first to build up your reputation?")
			else:
				print("You showed your rapping skills and won the rap battle!" + "\n")
				current_room["rapperbeat"] = True
				print("That took you " + str(c.seconds) + " seconds." + "\n")
				inventory.append(current_room["award"])
				print("Winning the rap battle got you a " + current_room["award"]["name"] + "." + "\n")
				print("This " + current_room["award"]["id"] + " gives you an extra " + str(current_room["award"]["reputation"])+ " reputation.")
				print("This now makes your total reputation " + str(calculate_reputation(inventory)) + ".")
		else:
			print("You're not rapping the right words")
	else:
		print("You pussied out of the fight and got thrown out of the club")

def print_inventory_items(players_items):
    if len(players_items) ==0:
        print("You currently have no items")
    else:
        print("You have "+list_of_items(players_items)+".")

def list_of_items(items):
    full_list= ""
    i=0
    for item in items:
        if i ==0:
            full_list= full_list+ item["name"]
            i=+1
        else:
            full_list = full_list +", " +item["name"]
    return full_list





def print_room(current_room):
	print("")
	print(current_room["name"].upper())
	print("")
	print(current_room["description"])
	print("")


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]



def print_exit(direction, leads):
	print("GO " + direction.upper() + " to " + leads + ".")


def print_menu(exits):
	print_inventory_items(inventory)
	for direction in exits:
		print_exit(direction, exit_leads_to(exits, direction))
	if current_room["rapperbeat"] == False:
		if len(current_room["rapper"]) != 0:
			print("Battle " + current_room["rapper"])
	else:
		print("")
		print("")


def execute_command(command):

    #if 0 == len(command):
     #   return

    #if command[0] == "b":
    #	print("hello world")

    if command.split(' ', 1)[0] == "battle":
    	if current_room["rapperbeat"] == False:
    		if len(current_room["rapper"]) != 0:
    			battle(n, current_room)
    elif command.split(' ', 1)[0] == "go":
    	execute_go(command.split(' ',1)[1])
    else:
    	print("I don't understand that command")

def execute_go(direction):

	global current_room
	if direction in current_room["exits"]:
		a = (current_room["exits"])

		b = a[direction]

		current_room = rooms[b]


	else:
		print("You need to pick a valid direction")



def menu(exits):
	print_menu(current_room["exits"])
	user_input = input("> ")
	if user_input == "q":
		raise SystemExit()
	else:
		return user_input


def main():
	while True:

		print_room(current_room)
		command = menu(current_room["exits"])
		#print_menu(current_room["exits"])
		execute_command(command)
		#battle(n, current_room)
		calculate_reputation(inventory)






screen_menu()
main()
