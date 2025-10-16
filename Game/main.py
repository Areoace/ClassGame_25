# Ultimate Casino Game
# Created: 10/14/2025
import random
import json
import os

DATA_FILE = "casino_data.json"

# Load or initialize player data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_player(name):
    if name not in data:
        data[name] = {
            "coins": 1000,
            "cars": [],
            "special_items": []
        }
    return data[name]

def slots(player):
    print("\n--- Slots ---")
    bet = int(input("Enter your bet: "))
    if bet > player["coins"]:
        print("Not enough coins!")
        return
    player["coins"] -= bet
    slot1 = random.randint(1, 9)
    slot2 = random.randint(1, 9)
    slot3 = random.randint(1, 9)
    slot4 = random.randint(1, 9)
    print(f"Slots: {slot1} {slot2} {slot3} {slot4}")
    if slot1 == slot2 == slot3 == slot4:
        winnings = bet * 10
        print(f"You won {winnings} coins!")
        player["coins"] += winnings
    else:
        print("You lost!")

def blackjack(player):
    print("\n--- Blackjack ---")
    bet = int(input("Enter your bet: "))
    if bet > player["coins"]:
        print("Not enough coins!")
        return
    player["coins"] -= bet

    def deal_card():
        return random.randint(1, 11)

    player_total = deal_card() + deal_card()
    dealer_total = deal_card() + deal_card()
    print(f"Your total: {player_total}, Dealer shows: {dealer_total}")

    while player_total < 21:
        choice = input("Hit or Stand? (H/S): ").lower()
        if choice == "h":
            card = deal_card()
            player_total += card
            print(f"You drew {card}. Total now {player_total}")
        else:
            break

    while dealer_total < 17:
        dealer_total += deal_card()

    print(f"Dealer total: {dealer_total}")
    if player_total > 21:
        print("Bust! You lose.")
    elif dealer_total > 21 or player_total > dealer_total:
        winnings = bet * 2
        print(f"You win {winnings} coins!")
        player["coins"] += winnings
    else:
        print("You lose!")

def poker(player):
    print("\n--- Poker ---")
    bet = int(input("Enter your bet: "))
    if bet > player["coins"]:
        print("Not enough coins!")
        return
    player["coins"] -= bet

    hand = [random.randint(1, 13) for _ in range(5)]
    print(f"Your hand: {hand}")
    # simple win condition: pair or higher
    counts = {x: hand.count(x) for x in hand}
    if max(counts.values()) >= 2:
        winnings = bet * 3
        print(f"You win {winnings} coins!")
        player["coins"] += winnings
    else:
        print("No pairs. You lose.")

def admin_panel():
    code = input("Enter admin code: ")
    if code != "BLADE":
        print("Invalid admin code!")
        return
    while True:
        print("\n--- Admin Panel ---")
        print("1. Give Coins")
        print("2. Give Car")
        print("3. Give Special Item")
        print("4. View Player Data")
        print("5. Exit Admin Panel")
        print ("6. Make sure to ban Sharan when you can....")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Player name: ")
            amount = int(input("Coins to give: "))
            player = get_player(name)
            player["coins"] += amount
            print(f"Gave {amount} coins to {name}")
        elif choice == "2":
            name = input("Player name: ")
            car = input("Car to give: ")
            player = get_player(name)
            player["cars"].append(car)
            print(f"Gave car {car} to {name}")
        elif choice == "3":
            name = input("Player name: ")
            item = input("Special item to give: ")
            player = get_player(name)
            player["special_items"].append(item)
            print(f"Gave {item} to {name}")
        elif choice == "4":
            print(json.dumps(data, indent=4))
        elif choice == "5":
            break
        save_data()

def main():
    print("Welcome to the All day all night 24/7  Casino Game!")
    name = input("Enter your player name: ")
    player = get_player(name)

    while True:
        print("\n--- Main Menu ---")
        print("1. Slots")
        print("2. Blackjack")
        print("3. Poker")
        print("4. View Inventory & Coins")
        print("5. Admin Panel")
        print("6. Exit")
        print ("© Made by Team-Blade and Viraj Agarwal Along with Samuel Phipps")
        choice = input("Choose an option: ")
        if choice == "1":
            slots(player)
        elif choice == "2":
            blackjack(player)
        elif choice == "3":
            poker(player)
        elif choice == "4":
            print(f"Coins: {player['coins']}")
            print(f"Cars: {player['cars']}")
            print(f"Special Items: {player['special_items']}")
        elif choice == "5":
            admin_panel()
        elif choice == "6":
            print("Goodbye!")
            save_data()
            break
        else:
            print("Invalid choice. Use numbers 1-6.")
        save_data()

main()
