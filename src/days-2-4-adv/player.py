# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, currentRoom, items = []):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items
        self.treasures = []
        self.pTreasures = []#add to both check if its already here to add value or not.
        self.points = 0 
        self.toCollect = 3#if a player gets all 3 treasures they win the game. 

    def __str__(self):
        return f"{self.name} \n\ncurrently in room {self.currentRoom}\n"
    
    def room_change(self, direction):
        newRoom = self.currentRoom.change_room(direction)
        print(f"newRoom === {newRoom}") #sole purpose of this line is for debugging
        if newRoom is not None:
            self.currentRoom = newRoom
            return f"Changing rooms..."
        else:
            return "You cannot go into that direction!"
    #
    def grabItem(self, item):
        if item.name == 'coins':
            successful = self.currentRoom.removeItem(item)
            if successful is not None:
                self.points += 25
                return f"You collected coins and added 25 points to your score. Your current score is {self.points}"
            else:
                return f"You have collected all of the coins this room has to offer."
        else: 
            successful = self.currentRoom.removeItem(item)
            if successful is not None:
                self.items.append(item)
                return f"You collected the {item.name}\n"
            else:
                return f"That item is not available in this room."
    def dropItem(self, item):
        if item.name == 'coins':
            return f"Coins cannot be dropped"
        elif self.items.count(item) > 0:
            if self.items.count(item) > 0:
                self.currentRoom.addItem(item)
                self.items.remove(item)
                return f"You have dropped the {item.name} in the {self.currentRoom}"
            else:
                return (f"You do not have that item in your inventory\n  use option i to view your inventory")
    def showInventory(self):
        items = []
        for item in self.items:
            items.append((item.name, item.description)) 
        return items
    #
    def currentScore(self):
        return f"Your current score is {self.points}"
    #
    def lookAround(self):
        able_to_see = self.currentRoom.is_light
        if able_to_see:
            return self.currentRoom.revealItems()
        else:
            # if the player has a light source self.currentRoom.revealItems()
            has_light = False 
            for item in self.items:
                if(isinstance(item, LightSource)):
                    has_light = True
            if has_light:
                return self.currentRoom.revealItems()
            else:
                return f"This room requires a lightsource to see items within."
                    
                
    #
    #
    #

        
