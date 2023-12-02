import random
class Player:
    def __init__(self, name, health=100, attack=10, defense=5, level=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.inventory = []
    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
    def level_up(self):
        self.level += 1
        self.attack += 5
        self.defense += 2
        self.health += 20
        print(f"{self.name} leveled up to level {self.level}!")
    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            if item == "Health Potion":
                self.health += 30
                print(f"{self.name} used a Health Potion and gained 30 health.")
            elif item == "Attack Boost":
                self.attack += 5
                print(f"{self.name} used an Attack Boost and gained 5 attack points.")
            elif item == "Defense Boost":
                self.defense += 3
                print(f"{self.name} used a Defense Boost and gained 3 defense points.")
        else:
            print(f"{self.name} doesn't have {item} in the inventory.")

class Enemy:
    def __init__(self, name, health=50, attack=8, defense=3, experience=20):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage.")

class ItemShop:
    def __init__(self):
        self.items = ["Health Potion", "Attack Boost", "Defense Boost"]
    def display_items(self):
        print("Items available in the shop:")
        for item in self.items:
            print(f"- {item}")
class Game:
    def __init__(self):
        self.player = None
        self.enemies = [Enemy(name="Goblin"), Enemy(name="Orc"), Enemy(name="Dragon")]
        self.item_shop = ItemShop()
        self.is_playing = True
    def create_player(self):
        player_name = input("Enter your character's name: ")
        self.player = Player(name=player_name)
    def explore(self):
        print(f"{self.player.name} is exploring...")
        encountered_enemy = random.choice(self.enemies)
        print(f"A wild {encountered_enemy.name} appears!")
        battle(self.player, encountered_enemy)
    def visit_item_shop(self):
        print("Welcome to the Item Shop!")
        self.item_shop.display_items()
        choice = input("What would you like to buy? (Type the item name or 'exit' to leave): ")
        if choice.lower() == 'exit':
            print("Leaving the Item Shop.")
        elif choice in self.item_shop.items:
            self.player.inventory.append(choice)
            print(f"{self.player.name} bought {choice}.")
        else:
            print("Invalid choice. Please select a valid item or type 'exit' to leave.")
    def game_loop(self):
        while self.is_playing and self.player.health > 0:
            print("\n1. Explore\n2. Visit Item Shop\n3. Check Player Stats\n4. Quit")
            action = input("Choose an action: ")
            if action == '1':
                self.explore()
            elif action == '2':
                self.visit_item_shop()
            elif action == '3':
                self.display_player_stats()
            elif action == '4':
                print("Thanks for playing! Goodbye.")
                self.is_playing = False
            else:
                print("Invalid choice. Please choose a valid action.")
    def display_player_stats(self):
        print(f"\nPlayer Stats for {self.player.name}:")
        print(f"Level: {self.player.level}")
        print(f"Health: {self.player.health}")
        print(f"Attack: {self.player.attack}")
        print(f"Defense: {self.player.defense}")
        print("Inventory:", self.player.inventory)
def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.health > 0 and enemy.health > 0:
        print(f"{player.name}'s Health: {player.health}, {enemy.name}'s Health: {enemy.health}")
        player.attack_enemy(enemy)
        if enemy.health <= 0:
            player.level_up()
            print(f"{player.name} defeated {enemy.name} and gained {enemy.experience} experience!")
            break
        enemy.attack_player(player)
        if player.health <= 0:
            print(f"{player.name} was defeated by {enemy.name}. Game over!")
            break
if __name__ == "__main__":
    game_instance = Game()
    game_instance.create_player()
    game_instance.game_loop()
