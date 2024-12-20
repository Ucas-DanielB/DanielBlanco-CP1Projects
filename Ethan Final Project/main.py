import random

class AdventureGame:
    def __init__(self, player):
        self.player = player
        self.location = "PLAINS"
        self.inventory = []  # List to store special items
        self.game_running = True  # Loop control

def play(self):
    while self.game_running:  # The loop keeps the game running until the player decides to stop
        if self.location == "PLAINS":
            self.plains()
        elif self.location == "DESERT":
            self.desert()
        elif self.location == "DUNES":
            self.dunes()
        elif self.location == "CAVES":
            self.caves()
        elif self.location == "PORT":
            self.port()
        elif self.location == "WASTELANDS":
            self.wastelands()
        elif self.location == "HOTLANDS":
            self.hotlands()
        elif self.location == "ICECAPS":
            self.icecaps()
        elif self.location == "HIGHPLAINS":
            self.highplains()
        elif self.location == "BEACH":
            self.beach()
        elif self.location == "CYBER CITY":
            self.cyber_city()
        else:
            print("Unknown location.")
            self.game_running = False

def plains(self):
    print("You are in the Plains.")
    if self.player["weapon"] <= 0:
        print("You encountered an NPC and gained a weapon and armor!")
        self.player["weapon"] += 1
        self.player["armor"] += 1
    elif self.player["level"] <= 5:
        print("You encountered an enemy and need to fight!")
        self.fight()
    else:
        print("You encountered an NPC and progressed to the Desert.")
        self.location = "DESERT"

def desert(self):
    print("Do you want to go to the desert? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        self.location = "DESERT"
        print("You encountered a tough story NPC and a high-level enemy!")
        self.fight()
        if self.player["level"] >= 15:
            self.location = "DUNES"
            print("You progressed to the Dunes!")
            self.dunes()
    elif choice == "no":
        self.location = "CAVES"
        print("You encountered a low-level enemy!")
        self.fight()
        if self.player["level"] >= 7:
            print("You encountered a story NPC and another low-level enemy!")
            self.fight()

def dunes(self):
    print("You encountered a health item, high armor, high weapon, and a mini-boss!")
    self.player["weapon"] += 2
    self.player["armor"] += 2
    self.fight()
    print("You encountered a dune NPC and progressed to the Port.")
    self.location = "PORT"

def caves(self):
    print("You encountered a low-level enemy!")
    self.fight()
    if self.player["level"] >= 7:
        print("You encountered a story NPC and another low-level enemy!")
        self.fight()
    else:
        self.location = "MOUNTAINS"
        print("You are now in the Mountains.")
        if self.player["level"] >= 15:
            print("You encountered a health item, low armor, low weapon, and a low-level enemy!")
            self.fight()
        else:
            self.location = "DUNES"
            print("You encountered a health item, high armor, high weapon, and a mini-boss!")
            self.fight()
            if self.player["level"] >= 15:
                print("You defeated the mini-boss and progressed to the Port.")
                self.location = "PORT"

def port(self):
    print("Do you want to buy a boat? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        self.inventory.append("Boat")  # Adding the boat to the inventory
        print("You acquired a boat and progressed to the Wastelands.")
        self.location = "WASTELANDS"
    elif choice == "no":
        print("Backtracking to the Desert or Plains.")
        self.backtrack()

def backtrack(self):
    print("Do you want to go to the Desert? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        self.location = "DESERT"
    else:
        print("Do you want to go to the Plains? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            self.location = "PLAINS"
        else:
            self.location = "DESERT"

def wastelands(self):
    print("You encountered a story NPC.")
    if self.player["level"] <= 20:
        print("You gained a special weapon!")
        self.player["weapon"] += 1
        self.fight()
    if self.player["level"] >= 25:
        print("You encountered a wasteland boss!")
        self.fight()
        self.hotlands()

def hotlands(self):
    print("You gained special hotland armor!")
    self.player["armor"] += 2
    if self.player["level"] <= 30:
        print("You encountered a hotland enemy!")
        self.fight()
    else:
        print("You encountered a hotland NPC and gained a special weapon!")
        self.player["weapon"] += 2

def icecaps(self):
    print("You gained special icecap armor!")
    self.player["armor"] += 2
    if self.player["level"] <= 40:
        print("You encountered an icecap world event and phenomena!")
    else:
        print("You encountered an icecap boss!")
        self.fight()
        self.highplains()

def highplains(self):
    print("You encountered a new NPC with unique armors and new weapons!")
    if self.player["armor"] <= 5 and self.player["weapon"] <= 5:
        print("You progressed to the Beach!")
        self.beach()

def beach(self):
    if "Special Item" in self.inventory:  # Check for special item in inventory
        print("You opened the gate and progressed to Cyber City.")
        self.cyber_city()
    else:
        print("Backtracking to High Plains.")
        self.highplains()

def cyber_city(self):
    print("Are you ready for the final island? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        print("Progressing further to Cyber City.")
        self.fight()
        print("You encountered a cyber city NPC and cyber city boss!")
        self.fight()
        print("You won the game!")
        self.game_running = False  # Break out of the loop, ending the game
    elif choice == "no":
        print("Backtracking to previous locations.")
        self.backtrack()

def fight(self):
    print("Fighting!")
    dice_roll = random.randint(1, 12)
    base_damage = dice_roll + self.player["weapon"]
    print(f"You dealt {base_damage} damage!")

def combat_system(self):
    if self.player["level"] <= 10:
        print("You deal less damage.")
    else:
        print("You deal more damage.")
    if self.player["weapon"] >= 5 and self.player["armor"] >= 5:
        print("You deal less damage and take more damage.")
    else:
        print("You deal more damage and take less damage.")

# Example player setup
player = {
    "level": 5,
    "weapon": 0,
    "armor": 0,
}

game = AdventureGame(player)
game.play()
