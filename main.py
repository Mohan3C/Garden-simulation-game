import time
import random

class GardenSimulator:
    def __init__(self):
        self.plants = {}
        self.money = 10  # Initial money to buy seeds
        self.weather = "sunny"
        self.day = 1

    def print_status(self):
        print(f"Day {self.day} | Money: ${self.money} | Weather: {self.weather}")
        print("Your garden:")
        for plant, info in self.plants.items():
            print(f"{plant.capitalize()}: {info['status']} - Days to harvest: {info['days_left']}")

    def check_weather(self):
        """Randomly changes the weather each day."""
        weather_options = ["sunny", "rainy", "cloudy", "stormy"]
        self.weather = random.choice(weather_options)
        print(f"Today's weather is: {self.weather}")

    def buy_seed(self):
        """Player buys a seed for $5."""
        if self.money >= 5:
            print("What seed would you like to buy? Options: carrot, tomato, lettuce")
            choice = input("Choose a seed: ").lower()
            if choice in ['carrot', 'tomato', 'lettuce']:
                self.money -= 5
                self.plants[choice] = {'status': 'planted', 'days_left': 5}
                print(f"You've planted {choice}s!")
            else:
                print("Invalid choice, try again.")
        else:
            print("You don't have enough money to buy seeds.")

    def water_plants(self):
        """Water the plants to increase growth."""
        print("You watered your plants.")
        for plant, info in self.plants.items():
            if info['status'] == 'planted':
                info['days_left'] -= 1  # Decrease days to harvest
        self.check_weather()

    def harvest(self):
        """Harvest ready crops."""
        for plant, info in self.plants.items():
            if info['days_left'] <= 0 and info['status'] != 'harvested':
                print(f"Your {plant} is ready to harvest!")
                self.money += 3  # Earn money for the harvest
                info['status'] = 'harvested'
        self.check_weather()

    def game_loop(self):
        """Main game loop."""
        while True:
            self.print_status()
            print("\nWhat would you like to do?")
            print("1. Buy seed ($5)")
            print("2. Water plants")
            print("3. Harvest crops")
            print("4. Quit game")

            choice = input("Enter a number: ")

            if choice == "1":
                self.buy_seed()
            elif choice == "2":
                self.water_plants()
            elif choice == "3":
                self.harvest()
            elif choice == "4":
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
            
            self.day += 1  # Move to the next day
            time.sleep(1)

# Start the game
game = GardenSimulator()
game.game_loop()
