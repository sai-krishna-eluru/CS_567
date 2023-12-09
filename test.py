import unittest
from unittest.mock import patch
from io import StringIO
from your_game_file import Player, Enemy, ItemShop, Game, battle

class TestRPGGame(unittest.TestCase):
    
    def setUp(self):
        self.player = Player(name="TestPlayer", health=50, attack=15, defense=8, level=2)
        self.enemy = Enemy(name="TestEnemy", health=30, attack=10, defense=5, experience=15)
        self.item_shop = ItemShop()
        self.game_instance = Game()

    def test_player_attack_enemy(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.player.attack_enemy(self.enemy)
            output = mock_stdout.getvalue().strip()
            self.assertIn("TestPlayer attacks TestEnemy", output)

    def test_enemy_attack_player(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.enemy.attack_player(self.player)
            output = mock_stdout.getvalue().strip()
            self.assertIn("TestEnemy attacks TestPlayer", output)

    def test_level_up(self):
        self.player.level_up()
        self.assertEqual(self.player.level, 3)
        self.assertEqual(self.player.attack, 20)
        self.assertEqual(self.player.defense, 10)
        self.assertEqual(self.player.health, 70)

    def test_use_health_potion(self):
        initial_health = self.player.health
        self.player.inventory.append("Health Potion")
        self.player.use_item("Health Potion")
        self.assertEqual(self.player.health, initial_health + 30)

    def test_visit_item_shop_buy_item(self):
        with patch("builtins.input", return_value="Health Potion"):
            self.game_instance.create_player()
            self.game_instance.visit_item_shop()
            self.assertIn("TestPlayer bought Health Potion", self.game_instance.player.inventory)

    def test_explore_encounter_enemy(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("random.choice", return_value=self.enemy):
                self.game_instance.create_player()
                self.game_instance.explore()
                output = mock_stdout.getvalue().strip()
                self.assertIn("A wild TestEnemy appears!", output)

    def test_game_loop_explore_option(self):
        with patch("builtins.input", return_value="1"), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.game_instance.create_player()
            self.game_instance.game_loop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("is exploring", output)

    def test_game_loop_visit_item_shop_option(self):
        with patch("builtins.input", return_value="2"), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.game_instance.create_player()
            self.game_instance.game_loop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Welcome to the Item Shop!", output)

    def test_game_loop_display_player_stats_option(self):
        with patch("builtins.input", return_value="3"), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.game_instance.create_player()
            self.game_instance.game_loop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Player Stats for TestPlayer", output)

    def test_game_loop_quit_option(self):
        with patch("builtins.input", return_value="4"), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.game_instance.create_player()
            self.game_instance.game_loop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Thanks for playing! Goodbye.", output)

if __name__ == "__main__":
    unittest.main()
