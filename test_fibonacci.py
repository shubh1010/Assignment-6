import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            Fibonacci("not an integer")

    def test_fibonacci_zero(self):
        self.assertEqual(list(Fibonacci(0)), [0])

    def test_fibonacci_one(self):
        self.assertEqual(list(Fibonacci(1)), [0, 1])

    def test_fibonacci_two(self):
        self.assertEqual(list(Fibonacci(2)), [0, 1, 1])

if __name__ == "__main__":
    unittest.main()