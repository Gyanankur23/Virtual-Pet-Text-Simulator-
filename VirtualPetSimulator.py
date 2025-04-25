import random

# Define the structure of a pet
def create_pet(name):
    return {
        'name': name,
        'happiness': 50,
        'hunger': 50,
        'health': 100
    }

# Feed the pet
def feed_pet(pet):
    pet['hunger'] = max(0, pet['hunger'] - 15)
    pet['happiness'] = max(0, pet['happiness'] - 5)
    print(f"\nYou fed {pet['name']}. Hunger decreased. Happiness slightly reduced.")

# Play with the pet
def play_with_pet(pet):
    pet['happiness'] = min(100, pet['happiness'] + 15)
    pet['hunger'] = min(100, pet['hunger'] + 5)
    print(f"\nYou played with {pet['name']}. Happiness increased. Hunger slightly increased.")

# Give toy to pet
def give_toy(pet):
    pet['happiness'] = min(100, pet['happiness'] + 10)
    print(f"\nYou gave a toy to {pet['name']}. Happiness increased.")

# Give medicine
def give_medicine(pet):
    pet['health'] = min(100, pet['health'] + 20)
    print(f"\nYou gave medicine to {pet['name']}. Health improved.")

# Show pet's status
def show_status(pet):
    print(f"\nStatus of {pet['name']}:")
    print(f"Happiness: {pet['happiness']}")
    print(f"Hunger: {pet['hunger']}")
    print(f"Health: {pet['health']}")

# Handle time passage
def time_passes(pet):
    pet['hunger'] = min(100, pet['hunger'] + 10)
    pet['happiness'] = max(0, pet['happiness'] - 5)
    pet['health'] = max(0, pet['health'] - 5)

# Check if the game is over
def check_game_over(pet):
    if pet['hunger'] >= 100:
        print(f"\n{pet['name']} is too hungry! Game Over.")
        return True
    if pet['happiness'] <= 0:
        print(f"\n{pet['name']} is too sad! Game Over.")
        return True
    if pet['health'] <= 0:
        print(f"\n{pet['name']} has fallen sick! Game Over.")
        return True
    return False

# Random events
def random_event(pet):
    event = random.choice(['snack', 'sick', 'none'])
    if event == 'snack':
        pet['hunger'] = max(0, pet['hunger'] - 10)
        print(f"\nRandom Event: {pet['name']} found a snack! Hunger decreased.")
    elif event == 'sick':
        pet['health'] = max(0, pet['health'] - 15)
        print(f"\nRandom Event: {pet['name']} caught a cold! Health decreased.")
    # else: No event

# Show menu
def show_menu():
    print("\nChoose an action:")
    print("1. Feed pet")
    print("2. Play with pet")
    print("3. Give toy")
    print("4. Give medicine")
    print("5. Check status")
    print("6. Switch pet")
    print("7. Quit")

# Main program
def main():
    print("Welcome to the Virtual Pet Simulator!")
    
    pets = {}
    num = int(input("How many pets would you like to create? "))
    for i in range(num):
        name = input(f"Enter name for pet #{i+1}: ")
        pets[name] = create_pet(name)

    current_pet = list(pets.values())[0]
    actions = 0

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            feed_pet(current_pet)
        elif choice == '2':
            play_with_pet(current_pet)
        elif choice == '3':
            give_toy(current_pet)
        elif choice == '4':
            give_medicine(current_pet)
        elif choice == '5':
            show_status(current_pet)
        elif choice == '6':
            print("\nAvailable pets:")
            for name in pets:
                print(f"- {name}")
            selected = input("Enter the name of the pet you want to switch to: ")
            if selected in pets:
                current_pet = pets[selected]
                print(f"You are now caring for {current_pet['name']}.")
            else:
                print("Pet not found.")
        elif choice == '7':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        actions += 1

        if actions % 3 == 0:
            time_passes(current_pet)
            random_event(current_pet)

        if check_game_over(current_pet):
            break

# Run the simulation
main()
