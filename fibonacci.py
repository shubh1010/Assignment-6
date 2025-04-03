class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        self.n = n
        self.sequence = [0] if n == 0 else [0, 1] if n == 1 else [0, 1]

        while len(self.sequence) <= n:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def __iter__(self):
        return iter(self.sequence)