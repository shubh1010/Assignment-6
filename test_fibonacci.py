import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_four(self):
        self.assertEqual(list(Fibonacci(4)), [0, 1, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_four(self):
        self.assertEqual(list(Fibonacci(4)), [0, 1, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()