import random

# Player stats
player = {
    "health": 50,
    "max_health": 50,
    "damage": 15,
    "inventory": [],
    "equipped": {"weapon": None, "chest_armor": None, "boots": None},
    "defeated_monsters": [],
}

# Locations
locations = {
    "Center Plaza": {"description": "The starting point of your journey.", "unlocked": True, "item_obtained": True},
    "North House": {"description": "An easy monster to fight.", "monster": "A beast lies here, but he seems to be invisible!", "unlocked": True, "item_obtained": False},
    "East House": {"description": "An easy monster with a 10% chance to drop the Severed Hand.", "monster": "A monster with blades for hands!", "unlocked": True, "item_obtained": False},
    "West House": {"description": "An easy monster with a 10% chance to drop Rotten Teeth.", "monster": "The undead has come back! He seems to own the house and pay the mortage too!", "unlocked": True, "item_obtained": False},
    "Western School District": {"description": "Stronger monster that fights back.", "monster": "The Janitor Rebels!", "unlocked": False, "item_obtained": False},
    "Eastern School District": {"description": "Stronger monster that fights back.", "monster": "Rick The Door Technician", "unlocked": False, "item_obtained": False},
    "Western Military": {"description": "Requires weapons to defeat.", "monster": "Field Guard", "unlocked": False, "item_obtained": False},
    "Eastern Military": {"description": "Requires weapons to defeat.", "monster": "A juggernaut!(not from marvel, trust)", "unlocked": False, "item_obtained": False},
    "City Border": {"description": "Boss fight requiring specific items.", "monster": "The Undead City Border Police", "unlocked": False, "item_obtained": False},
    "State Line": {"description": "The final boss awaits you.", "monster": "Satan Himself!", "unlocked": False, "item_obtained": False},
}

# Monsters
monsters = {
    "A beast lies here, but he seems to be invisible!": {"health": 20, "damage": 5},
    "A monster with blades for hands!": {"health": 20, "damage": 5},
    "The undead has come back! He seems to own the house and pay the mortage too!": {"health": 20, "damage": 5},
    "The Janitor Rebels!": {"health": 50, "damage": 10},
    "Rick The Door Technician": {"health": 50, "damage": 10},
    "Field Guard": {"health": 75, "damage": 12},
    "A juggernaut!(not from marvel, trust)": {"health": 75, "damage": 12},
    "The Undead City Border Police": {"health": 100, "damage": 15},
    "Satan Himself!": {"health": 150, "damage": 20},
}

# Items
items = {
    "Weak Knife": {"type": "weapon", "boost": {"damage": 5}, "description": "Increases damage by 5."},
    "Weak Chest Plate": {"type": "chest_armor", "boost": {"max_health": 10}, "description": "Boosts max health by 10."},
    "Bandage": {"type": "healing", "boost": {"health": 20}, "description": "Heals 20 health. One-time use."},
    "Vaporub": {"type": "healing", "boost": {"health": 10}, "description": "Heals 10 health. One-time use."},
    "Weak Boots": {"type": "boots", "boost": {"dodge_chance": 0.1}, "description": "10% chance to avoid damage."},
    "Severed Hand": {"type": "special", "boost": {}, "description": "One-hit kill on any monster. One-time use."},
    "Rotten Teeth": {"type": "boots", "boost": {"steal_health": 20}, "description": "Steals 20 health from a monster."},
    "Military Helmet": {"type": "head_gear", "boost": {"damage": 10}, "description": "Increases damage by 10."},
    "Bulletproof Armor": {"type": "chest_armor", "boost": {"max_health": 25}, "description": "Increases health by 25."},
    "Field Officer Sword": {"type": "weapon", "boost": {"damage": 25}, "description": "Increases damage by 25."},
    "Blast Suit": {"type": "chest_armor", "boost": {"damage": 5, "max_health": 75}, "description": "Increases damage by 5 and max health by 75."},
    "Hand Grenades": {"type": "weapon", "boost": {"damage": 50}, "description": "Increases damage by 50."},
}

# Random Item Drop Function
def drop_random_item(location):
    if location == "Western School District" or location == "Eastern School District":
        item_type = random.choice(["boots", "chest_armor", "weapon"])
        if item_type == "boots":
            item_name = "Weak Boots"
            item = items[item_name]
        elif item_type == "chest_armor":
            item_name = "Weak Chest Plate"
            item = items[item_name]
        elif item_type == "weapon":
            item_name = "Weak Knife"
            item = items[item_name]
        
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    elif location == "Western Military":
        item_name = random.choice(["Military Helmet", "Field Officer Sword", "Bulletproof Armor"])
        item = items[item_name]
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    elif location == "Eastern Military":
        item_name = random.choice(["Military Helmet", "Field Officer Sword", "Bulletproof Armor"])
        item = items[item_name]
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    elif location == "City Border":
        item_name = random.choice(["Blast Suit", "Hand Grenades"])
        item = items[item_name]
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    else:
        # For other locations, just add random item
        item_name = random.choice(list(items.keys()))
        item = items[item_name]
        print(f"You found a {item_name}!")
        player["inventory"].append(item_name)

# Combat function
def combat(monster_name, current_location):
    monster = monsters[monster_name]
    print(f"A {monster_name} appears! It has {monster['health']} health and does {monster['damage']} damage.")
    
    while player["health"] > 0 and monster["health"] > 0:
        action = input("Do you want to (attack), (use item), or (equip/unequip item)? ").lower()
        
        if action == "attack":
            monster["health"] -= player["damage"]
            print(f"You hit the {monster_name}. It has {max(0, monster['health'])} health left.")
        
        elif action == "use item":
            if "Severed Hand" in player["inventory"]:
                print(f"You used the Severed Hand! The {monster_name} is defeated instantly.")
                player["inventory"].remove("Severed Hand")
                monster["health"] = 0
            else:
                print("You don't have any usable items.")
        
        elif action == "equip":
            item_name = input("Which item do you want to equip? ").strip()
            equip_item(item_name)
        
        elif action == "unequip":
            item_type = input("Which type of item do you want to unequip? (weapon, chest_armor, boots) ").strip()
            unequip_item(item_type)
        
        # Monster attacks after player's action
        if monster["health"] > 0:
            player["health"] -= monster["damage"]
            print(f"The {monster_name} hit you. You have {player['health']} health left.")
    
    # End of combat - check if player or monster won
    if player["health"] <= 0:
        print("You have been defeated. Game over!")
        exit()  # Ends the game if player is defeated
    else:
        print(f"You defeated the {monster_name}!")
        player["defeated_monsters"].append(monster_name)
        
        # Drop a random item based on the current location after defeating the monster
        drop_random_item(current_location)  # Pass current_location to drop_random_item

# Equip item function
def equip_item(item_name):
    if item_name in player["inventory"]:
        item = items[item_name]
        item_type = item["type"]
        if player["equipped"][item_type] is None:
            player["equipped"][item_type] = item_name
            print(f"You equipped the {item_name}.")
        else:
            print(f"You already have a {item_type} equipped. Unequip it first to equip the new one.")
    else:
        print("You don't have this item in your inventory.")

# Unequip item function
def unequip_item(item_type):
    if player["equipped"][item_type] is not None:
        item_name = player["equipped"][item_type]
        player["equipped"][item_type] = None
        print(f"You unequipped the {item_name}.")
    else:
        print(f"You don't have any {item_type} equipped.")

# Unlock new areas
def unlock_locations():
    if all(monster in player["defeated_monsters"] for monster in ["A beast lies here, but he seems to be invisible!", "A monster with blades for hands!", "The undead has come back! He seems to own the house and pay the mortage too!"]):
        locations["Western School District"]["unlocked"] = True
    if "Western School District" in player["defeated_monsters"]:
        locations["Eastern School District"]["unlocked"] = True
    if "Eastern School District" in player["defeated_monsters"]:
        locations["Western Military"]["unlocked"] = True
    if "Western Military" in player["defeated_monsters"]:
        locations["Eastern Military"]["unlocked"] = True
    if "Eastern Military" in player["defeated_monsters"]:
        locations["City Border"]["unlocked"] = True
    if "City Border" in player["defeated_monsters"]:
        locations["State Line"]["unlocked"] = True

# Main Game Loop
def main():
    current_location = "Center Plaza"
    
    while True:
        print(f"Current Location: {current_location}")
        print(f"Health: {player['health']}/{player['max_health']}")
        print("Inventory:", player["inventory"])
        print("Equipped:", player["equipped"])
        
        action = input("Do you want to (explore) a location, (view) your inventory, or (quit)? ").lower()
        
        if action == "explore":
            available_locations = [location for location, data in locations.items() if data["unlocked"] and location != current_location]
            print("Available locations:", available_locations)
            next_location = input("Where do you want to go? ").strip()
            
            if next_location in available_locations:
                print(f"You are traveling to {next_location}.")
                current_location = next_location
                combat(locations[current_location]["monster"], current_location)
            else:
                print("Invalid location.")
        
        elif action == "view":
            print("Inventory:", player["inventory"])
            print("Equipped items:", player["equipped"])
        
        elif action == "quit":
            print("Thanks for playing!")
            break

# Start the game
main()
