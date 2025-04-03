class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        if n < 0:
            self.sequence = []
        else:
            self.sequence = [0, 1] if n > 0 else [0]

            while len(self.sequence) <= n:
                self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def __iter__(self):
        return iter(self.sequence)


if __name__ == "__main__":
    while True:
        user_input = input("Enter a non-negative integer: ")

        try:
            n = int(user_input)

            if n < 0:
                print(f"Fibonacci sequence for {n}:[]")
                continue

            fib = Fibonacci(n)
            print(f"Fibonacci sequence for {n}: {list(fib)}")
            break

        except ValueError:
            print("Invalid input. Please enter a **valid integer**.")