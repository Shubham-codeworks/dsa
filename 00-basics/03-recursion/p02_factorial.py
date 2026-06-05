class Factorial:
    def factorial(self, n: int) -> int:
        if n <= 1:
            return 1
        return n * self.factorial(n-1)


if __name__ == "__main__":
    obj = Factorial()
    num = int(input("Enter an integer: "))
    res = obj.factorial(num)
    print(f"{num}! = {res}")