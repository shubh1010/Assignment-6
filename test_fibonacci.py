import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Fibonacci("string")
        with self.assertRaises(ValueError):
            Fibonacci(3.5)

    def test_fibonacci_zero(self):
        self.assertEqual(list(Fibonacci(0)), [0])

    def test_fibonacci_one(self):
        self.assertEqual(list(Fibonacci(1)), [0, 1])

    def test_fibonacci_two(self):
        self.assertEqual(list(Fibonacci(2)), [0, 1, 1])

    def test_fibonacci_four(self):
        self.assertEqual(list(Fibonacci(4)), [0, 1, 1, 2, 3])

    def test_fibonacci_ten(self):
        self.assertEqual(list(Fibonacci(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_negative_input(self):
        self.assertEqual(list(Fibonacci(-5)), [])

if __name__ == '__main__':
    unittest.main()