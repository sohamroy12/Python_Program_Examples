import unittest
from unittest.mock import patch
from Random_Game import generate_random_number, is_valid_guess, play_guessing_game




class TestRandomGame(unittest.TestCase):

    def test_generate_random_number_mocked(self):
        with patch('Random_Game.randint', return_value=5):
            self.assertEqual(generate_random_number(1, 10), 5)  # add assertion here

    def test_is_valid_guess(self):
        self.assertTrue(is_valid_guess(5, 1, 10))
        self.assertFalse(is_valid_guess(0, 1, 10))
        self.assertTrue(is_valid_guess(10, 1, 10))
        self.assertTrue(is_valid_guess(1, 1, 10))

    def test_play_guessing_game(self):
        # Correct guess
        self.assertEqual(play_guessing_game(1, 10, 7, 7), "Correct! You are a winner!")

        # Incorrect guess
        self.assertEqual(play_guessing_game(1, 10, 5, 7), "Wrong guess. Try again!")

        # Invalid guess (too low)
        self.assertIn("Invalid guess", play_guessing_game(1, 10, 0, 7))

        # Invalid guess (too high)
        self.assertIn("Invalid guess", play_guessing_game(1, 10, 11, 7))

if __name__ == '__main__':
    unittest.main()
