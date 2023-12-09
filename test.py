import unittest
from unittest.mock import patch
from io import StringIO
from game import Player, Enemy, ItemShop, Game, battle

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game_instance = Game()

    @patch('builtins.input', side_effect=['TestPlayer'])
    def test_create_player(self, mock_input):
        self.game_instance.create_player()
        self.assertEqual(self.game_instance.player.name, 'TestPlayer')

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'exit'])
    def test_explore_and_visit_item_shop(self, mock_input, mock_stdout):
        self.game_instance.create_player()
        self.game_instance.explore()
        self.assertIn("is exploring...", mock_stdout.getvalue())
        self.game_instance.visit_item_shop()
        self.assertIn("Welcome to the Item Shop!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['2', 'Health Potion', 'exit'])
    def test_visit_item_shop_and_buy_item(self, mock_input, mock_stdout):
        self.game_instance.create_player()
        self.game_instance.visit_item_shop()
        self.assertIn("Welcome to the Item Shop!", mock_stdout.getvalue())
        self.game_instance.visit_item_shop()
        self.assertIn("What would you like to buy?", mock_stdout.getvalue())
        self.game_instance.visit_item_shop()
        self.assertIn("Leaving the Item Shop.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_display_player_stats(self, mock_input, mock_stdout):
        self.game_instance.create_player()
        self.game_instance.display_player_stats()
        self.assertIn("Player Stats for TestPlayer:", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'exit'])
    def test_game_loop(self, mock_input, mock_stdout):
        self.game_instance.create_player()
        self.game_instance.game_loop()
        self.assertIn("Explore", mock_stdout.getvalue())
        self.assertIn("Leaving the Item Shop.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'exit'])
    def test_battle_and_level_up(self, mock_input, mock_stdout):
        player = Player(name="TestPlayer", health=50, attack=20, defense=10, level=1)
        enemy = Enemy(name="TestEnemy", health=30, attack=15, defense=5, experience=20)
        battle(player, enemy)
        self.assertIn("attacks TestEnemy for", mock_stdout.getvalue())
        self.assertIn("defeated TestEnemy and gained", mock_stdout.getvalue())
        self.assertEqual(player.level, 2)

if __name__ == '__main__':
    unittest.main()
