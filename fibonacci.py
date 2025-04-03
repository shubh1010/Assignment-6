class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        self.n = n
        self.sequence = [0] if n == 0 else []

    def __iter__(self):
        return iter(self.sequence)