import random

# Player stats
player_health = 100
player_attack = 5
inventory = []

# Function to display player's status
def display_status():
    print(f"Health: {player_health}")
    print(f"Attack: {player_attack}")
    print("Inventory:", inventory)

# Function to update player stats based on equipped items
def update_player_stats(item):
    global player_health, player_attack
    if item == "Weak Knife":
        player_attack += 30  # Weak Knife adds 30 attack damage
    elif item == "Specialized Mop":
        player_attack += 50  # Specialized Mop adds 50 attack damage
    elif item == "Weak Helmet":
        player_health += 30  # Weak Helmet adds 30 health
    elif item == "Trash Can Helmet":
        player_health += 50  # Trash Can Helmet adds 50 health
    elif item == "Field Officer Sword":
        player_attack += 60  # Field Officer Sword adds 60 attack damage
    elif item == "Bulletproof Armor":
        player_health += 100  # Bulletproof Armor adds 100 health
    elif item == "Blast Suit Armor":
        player_health += 150  # Blast Suit Armor adds 150 health
    elif item == "Hand Grenades":
        player_attack += 100  # Hand Grenades adds 100

# Function to handle combat
def combat(monster_health, monster_attack, monster_name, loot):
    global player_health, player_attack
    player_damage = player_attack
    while monster_health > 0 and player_health > 0:
        print(f"\n{monster_name} Health: {monster_health}")
        print(f"Your Health: {player_health}")
        action = input("Do you want to fight or heal? ").lower()
        if action == "fight":
            # Player attacks
            monster_health -= player_damage
            print(f"You dealt {player_damage} damage to the {monster_name}.")
        elif action == "heal":
            heal_item = get_heal_item()
            if heal_item:
                player_health += heal_item
                inventory.remove("Bandage")
                print(f"You healed for {heal_item} health.")
            else:
                print("No healing items in inventory.")
        else:
            print("Invalid action. Choose 'fight' or 'heal'.")

        # Monster attacks
        if monster_health > 0:
            player_health -= monster_attack
            print(f"{monster_name} dealt {monster_attack} damage to you.")

        if player_health <= 0:
            print("You have been defeated.")
            return False  # Player lost
    # Monster defeated, give loot
    print(f"You defeated the {monster_name}!")
    inventory.append(loot)
    update_player_stats(loot)  # Update stats based on loot received
    return True  # Player won

# Function to get heal item from inventory
def get_heal_item():
    if "Bandage" in inventory:
        return 20  # Bandage heals 20 health
    return 0

# Function for movement to locations
def move_to_location(location):
    global player_health
    if location == "Center Plaza":
        print("\nWelcome to the Center Plaza. You can go to the West House, East House, or North House.")
        print("There are no monsters here, but you can get ready for your journey.")
        display_status()
        return

    elif location == "West House":
        print("\nYou entered the West House and encountered a monster!")
        if combat(30, 5, "West House Monster", "Weak Knife"):
            print("You got a Weak Knife!")
        return

    elif location == "East House":
        print("\nYou entered the East House and encountered a monster!")
        if combat(30, 5, "East House Monster", "Weak Helmet"):
            print("You got a Weak Helmet!")
        return

    elif location == "North House":
        print("\nYou entered the North House and encountered a monster!")
        if combat(30, 5, "North House Monster", "Bandage"):
            print("You got a Bandage!")
        return

    elif location == "Western School District":
        print("\nYou entered the Western School District and encountered a stronger monster!")
        if combat(60, 15, "Western School District Monster", "Specialized Mop"):
            print("You got a Specialized Mop!")
        return

    elif location == "Eastern School District":
        print("\nYou entered the Eastern School District and encountered a stronger monster!")
        if combat(60, 15, "Eastern School District Monster", "Trash Can Helmet"):
            print("You got a Trash Can Helmet!")
        return

    elif location == "Western Military":
        print("\nYou entered the Western Military area and encountered a strong monster!")
        if combat(100, 25, "Western Military Monster", "Field Officer Sword"):
            print("You got a Field Officer Sword!")
        return

    elif location == "Eastern Military":
        print("\nYou entered the Eastern Military area and encountered a strong monster!")
        if combat(100, 25, "Eastern Military Monster", "Bulletproof Armor"):
            print("You got Bulletproof Armor!")
        return

    elif location == "City Border":
        print("\nYou entered the City Border and encountered a powerful boss!")
        if "Field Officer Sword" in inventory and "Bulletproof Armor" in inventory:
            if combat(150, 40, "City Border Boss", "Blast Suit Armor and Hand Grenades"):
                print("You got Blast Suit Armor and Hand Grenades!")
        else:
            print("You need the Field Officer Sword and Bulletproof Armor to fight this boss!")
        return

    elif location == "State Line":
        print("\nYou reached the State Line, the final boss!")
        if combat(200, 50, "State Line Boss", "Nothing (You won!)"):
            print("Congratulations, you have defeated the final boss and escaped the city!")

            return
            
            
        
# Main game loop
def main():
    global player_health
    print("Welcome to the Escape the Overrun Demonic Inhabitated Monsters Game!")
    print("You start in the Center Plaza. Your goal is to defeat all the monsters and escape the city.")
    print("Type 'inventory' to check your inventory and 'quit' to end the game.")
    location = "Center Plaza"
    while True:
        if player_health <= 0:
            print("You have died. Game Over.")
            break
        print(f"\nYou are currently in the {location}.")
        display_status()
        action = input("Where would you like to go? (West House, East House, North House, or quit)(These are your starting locations, after defeating them, you will have gained the items necessary to progress, you must then go to the western/eastern school district, then the western/eastern military, then the city border, then finally the state line): ").lower()
        if action == "quit":
            print("You quit the game.")
            break
        elif action == "west house":
            move_to_location("West House")
        elif action == "east house":
            move_to_location("East House")
        elif action == "north house":
            move_to_location("North House")
        elif action == "western school district":
            move_to_location("Western School District")
        elif action == "eastern school district":
            move_to_location("Eastern School District")
        elif action == "western military":
            move_to_location("Western Military")
        elif action == "eastern military":
            move_to_location("Eastern Military")
        elif action == "city border":
            move_to_location("City Border")
        elif action == "state line":
            move_to_location("State Line")
        else:
            print("Invalid location. Try again.")

# Start the game
if __name__ == "__main__":
    main()

#