#Ethan Blanco, Final Project

import random

# Player Stats and Inventory
player = {
    "level": 1,
    "strength": 5,
    "defense": 5,
    "health": 20,
    "gold": 0,
    "inventory": []
}

locations = {
    "Plains": {"visited": False, "items": ["Basic Sword", "Armor Piece"], "enemies": [{"name": "Wolf", "health": 15}]},
    "Desert": {"visited": False, "items": ["Key", "Potion"], "enemies": [{"name": "Bandit", "health": 50}]},
    "Caves": {"visited": False, "items": ["Shield"], "enemies": [{"name": "Spider", "health": 18}]},
    "Mountains": {"visited": False, "items": [], "enemies": [{"name": "Bear", "health": 30}]},
    "Port": {"visited": False, "items": ["Boat"], "enemies": []},
    "Wastelands": {"visited": False, "items": ["Flaming Sword"], "enemies": [{"name": "Fire Golem", "health": 50}]},
    "Hotlands": {"visited": False, "items": ["Fireproof Armor"], "enemies": [{"name": "Fire Elemental", "health": 40}]},
    "Ice Caps": {"visited": False, "items": ["Ice Pick"], "enemies": [{"name": "Ice Guardian", "health": 60}]},
    "Cyber City": {"visited": False, "items": ["Laser Gun"], "enemies": [{"name": "Cyber Computer", "health": 150}]}
}

# Helper Functions
def show_stats():
    print("\n=== Player Stats ===")
    for key, value in player.items():
        if key != "inventory":
            print(f"{key.capitalize()}: {value}")
    print("====================\n")

def explore_location(location_name):
    location = locations[location_name]
    print(f"\nExploring {location_name}...")
    if not location["visited"]:
        print(f"You find the following items: {', '.join(location['items'])}")
        player["inventory"].extend(location["items"])
        location["items"] = []
        location["visited"] = True
    else:
        print("You have already explored this area.")

    if location["enemies"]:
        print("You encounter an enemy!")
        fight_enemy(location["enemies"].pop(0))
    else:
        print("The area seems safe for now.\n")

def fight_enemy(enemy):
    print(f"A wild {enemy['name']} appears!")
    while enemy["health"] > 0 and player["health"] > 0:
        print(f"\nEnemy Health: {enemy['health']}")
        print(f"Your Health: {player['health']}")
        print("1. Attack\n2. Defend\n3. Use Item")
        action = input("Choose your action: ")

        if action == "1":
            damage = random.randint(1, 6) + player["strength"]
            enemy["health"] -= damage
            print(f"You deal {damage} damage to the {enemy['name']}!")
        elif action == "2":
            block = random.randint(1, 4) + player["defense"]
            print(f"You brace yourself, reducing incoming damage by {block}.")
        elif action == "3":
            use_item()
            continue
        else:
            print("Invalid choice! You lose your turn.")

        if enemy["health"] > 0:
            enemy_damage = max(0, random.randint(3, 8) - player["defense"])
            player["health"] -= enemy_damage
            print(f"The {enemy['name']} deals {enemy_damage} damage to you!")

        if player["health"] <= 0:
            print("You have been defeated! Game over.")
            quit()

    print(f"You defeated the {enemy['name']}!")
    player["level"] += 1
    player["gold"] += random.randint(5, 15)
    print("You gain a level and collect some gold!\n")

def use_item():
    print("\nYour Inventory:")
    for i, item in enumerate(player["inventory"], 1):
        print(f"{i}. {item}")
    choice = input("Enter the number of the item to use or 'cancel': ")
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(player["inventory"]):
            item = player["inventory"].pop(choice)
            if item == "Potion":
                player["health"] += 10
                print("You use a Potion and regain 10 health!")
            else:
                print(f"You can't use the {item} right now.")
        else:
            print("Invalid item choice.")
    elif choice.lower() == "cancel":
        print("You decided not to use an item.")
    else:
        print("Invalid input.")

def travel():
    print("\nAvailable Locations:")
    for i, location in enumerate(locations.keys(), 1):
        print(f"{i}. {location}")
    choice = input("Enter the number of the location to travel to: ")
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(locations):
            location_name = list(locations.keys())[choice]
            explore_location(location_name)
        else:
            print("Invalid location choice.")
    else:
        print("Invalid input.")

# Main Game Loop
def main():
    print("Welcome to the Text-Based Adventure Game!")
    while True:
        show_stats()
        print("1. Explore\n2. Travel\n3. View Stats\n4. Quit")
        choice = input("What would you like to do? ")

        if choice == "1":
            current_location = "Plains"  # Start at the Plains
            explore_location(current_location)
        elif choice == "2":
            travel()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the game
main()
