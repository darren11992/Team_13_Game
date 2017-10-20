from items import *
from roomsgit import rooms
#from rooms import rooms

inventory = [item_necklace]

# Start game at the reception
global current_room
score = 0
current_room = rooms["Jail Entrance"]