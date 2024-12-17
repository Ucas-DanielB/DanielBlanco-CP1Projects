import random

# Player stats
player = {
    "health": 100,
    "max_health": 100,
    "damage": 100,
    "inventory": [],
    "equipped": {"weapon": None, "chest_armor": None, "boots": None},
    "defeated_monsters": [],
}

# Locations
locations = {
    "Center Plaza": {"description": "The starting point of your journey.", "unlocked": True, "item_obtained": True},
    "North House": {"description": "An easy monster to fight.", "monster": "Northern Beast", "unlocked": True, "item_obtained": False},
    "East House": {"description": "An easy monster with a 10% chance to drop the Severed Hand.", "monster": "Eastern Goblin", "unlocked": True, "item_obtained": False},
    "West House": {"description": "An easy monster with a 10% chance to drop Flip Flops.", "monster": "Western Wolf", "unlocked": True, "item_obtained": False},
    "Western School District": {"description": "Stronger monster that fights back.", "monster": "Western Teacher", "unlocked": False, "item_obtained": False},
    "Eastern School District": {"description": "Stronger monster that fights back.", "monster": "Eastern Professor", "unlocked": False, "item_obtained": False},
    "Western Military": {"description": "Requires weapons to defeat.", "monster": "Field Guard", "unlocked": False, "item_obtained": False},
    "Eastern Military": {"description": "Requires weapons to defeat.", "monster": "Armored Defender", "unlocked": False, "item_obtained": False},
    "City Border": {"description": "Boss fight requiring specific items.", "monster": "City Border Boss", "unlocked": False, "item_obtained": False},
    "State Line": {"description": "The final boss awaits you.", "monster": "Final Boss", "unlocked": False, "item_obtained": False},
}

# Monsters
monsters = {
    "Northern Beast": {"health": 20, "damage": 5},
    "Eastern Goblin": {"health": 20, "damage": 5},
    "Western Wolf": {"health": 20, "damage": 5},
    "Western Teacher": {"health": 50, "damage": 10},
    "Eastern Professor": {"health": 50, "damage": 10},
    "Field Guard": {"health": 75, "damage": 12},
    "Armored Defender": {"health": 75, "damage": 12},
    "City Border Boss": {"health": 100, "damage": 15},
    "Final Boss": {"health": 150, "damage": 20},
}

# Items
items = {
    "Weak Knife": {"type": "weapon", "boost": {"damage": 5}, "description": "Increases damage by 5."},
    "Weak Chest Plate": {"type": "chest_armor", "boost": {"max_health": 10}, "description": "Boosts max health by 10."},
    "Bandage": {"type": "healing", "boost": {"health": 20}, "description": "Heals 20 health. One-time use."},
    "Vaporub": {"type": "healing", "boost": {"health": 10}, "description": "Heals 10 health. One-time use."},
    "Weak Boots": {"type": "boots", "boost": {"dodge_chance": 0.1}, "description": "10% chance to avoid damage."},
    "Severed Hand": {"type": "special", "boost": {}, "description": "One-hit kill on any monster. One-time use."},
    "Flip Flops": {"type": "boots", "boost": {"steal_health": 5}, "description": "Steals 5 health from a monster. One-time use."},
}

# Display player stats
def print_stats():
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Damage: {player['damage']}")
    print(f"Inventory: {player['inventory']}")
    print(f"Equipped Items: {player['equipped']}")
    print(f"Defeated Monsters: {player['defeated_monsters']}")
    print()

# Equip item
def equip_item(item_name):
    if item_name not in player["inventory"]:
        print("You don't have this item.")
        return
    item = items[item_name]
    item_type = item["type"]

    if player["equipped"][item_type]:
        print(f"You already have {player['equipped'][item_type]} equipped. Unequip it first.")
        return

    # Equip the item and apply its boosts
    player["equipped"][item_type] = item_name
    for stat, boost in item["boost"].items():
        player[stat] = player.get(stat, 0) + boost
    print(f"You equipped {item_name}. {item['description']}")

# Unequip item
def unequip_item(item_type):
    if not player["equipped"][item_type]:
        print(f"You have no {item_type} equipped.")
        return

    # Unequip the item and remove its boosts
    item_name = player["equipped"][item_type]
    item = items[item_name]
    for stat, boost in item["boost"].items():
        player[stat] = player.get(stat, 0) - boost
    player["equipped"][item_type] = None
    print(f"You unequipped {item_name}.")

# Combat function
def combat(monster_name):
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
        if monster["health"] > 0:
            player["health"] -= monster["damage"]
            print(f"The {monster_name} hit you. You have {player['health']} health left.")
    if player["health"] <= 0:
        print("You have been defeated. Game over!")
        exit()
    else:
        print(f"You defeated the {monster_name}!")
        player["defeated_monsters"].append(monster_name)

# Unlock new areas
def unlock_locations():
    if all(monster in player["defeated_monsters"] for monster in ["Northern Beast", "Eastern Goblin", "Western Wolf"]):
        locations["Western School District"]["unlocked"] = True
        locations["Eastern School District"]["unlocked"] = True
        print("The school districts are now unlocked! Please type west or east school to progress!")

# Item drop function
def drop_item(location):
    if not locations[location]["item_obtained"]:
        if location == "East House" and random.random() < 0.1:
            print("You found the Severed Hand!")
            player["inventory"].append("Severed Hand")
        elif location == "West House" and random.random() < 0.1:
            print("You found Flip Flops!")
            player["inventory"].append("Flip Flops")
        else:
            item = random.choice(list(items.keys()))
            print(f"You found a {item}!")
            player["inventory"].append(item)
        locations[location]["item_obtained"] = True

# Main game loop
def play_game():
    print("Welcome to the game!")
    current_location = "Center Plaza"
    while True:
        unlock_locations()
        print(f"You are at {current_location}.")
        print_stats()
        command = input("Enter a command (north, east, west, equip, unequip, inventory, or quit): ").lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "equip":
            item_name = input("Which item do you want to equip? ").strip()
            equip_item(item_name)
        elif command == "unequip":
            item_type = input("Which type of item do you want to unequip? (weapon, chest_armor, boots) ").strip()
            unequip_item(item_type)
        elif command == "inventory":
            print("Your Inventory:")
            for item in player["inventory"]:
                print(f"- {item}: {items[item]['description']}")
        elif command == "north":
            current_location = "North House"
            combat("Northern Beast")
            drop_item(current_location)
        elif command == "east":
            current_location = "East House"
            combat("Eastern Goblin")
            drop_item(current_location)
        elif command == "west":
            current_location = "West House"
            combat("Western Wolf")
            drop_item(current_location)
        elif command == "west school" and locations["Western School District"]["unlocked"]:
            current_location = "Western School District"
            combat("Western Teacher")
        elif command == "east school" and locations["Eastern School District"]["unlocked"]:
            current_location = "Eastern School District"
            combat("Eastern Professor")
        else:
            print("Invalid command.")

play_game()
