import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            Fibonacci("not an integer")

if __name__ == "__main__":
    unittest.main()