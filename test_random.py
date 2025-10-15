# test_random.py
import unittest
import my_random as random  # import your module

class TestRandomModule(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(random.add_numbers(2, 3), 5)

    def test_multiply_numbers(self):
        self.assertEqual(random.multiply_numbers(2, 3), 6)

    def test_factorial(self):
        self.assertEqual(random.factorial(5), 120)

    def test_random_int(self):
        val = random.random_int(1, 10)
        self.assertTrue(1 <= val <= 10)

    def test_random_choice(self):
        seq = [1, 2, 3]
        val = random.random_choice(seq)
        self.assertIn(val, seq)

if __name__ == '__main__':
    unittest.main()
