import unittest
from main.bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        """Helper function to roll multiple times."""
        for _ in range(rolls):
            self.game.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

if __name__ == "__main__":
    unittest.main()
