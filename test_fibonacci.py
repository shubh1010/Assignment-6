class TestFibonacci(unittest.TestCase):
    def test_fibonacci_ten(self):
        self.assertEqual(list(Fibonacci(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])