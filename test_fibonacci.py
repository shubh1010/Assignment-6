import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            Fibonacci("not an integer")

    def test_fibonacci_zero(self):
        self.assertEqual(list(Fibonacci(0)), [0])

if __name__ == "__main__":
    unittest.main()import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            Fibonacci("not an integer")

    def test_fibonacci_zero(self):
        self.assertEqual(list(Fibonacci(0)), [0])

if __name__ == "__main__":
    unittest.main()