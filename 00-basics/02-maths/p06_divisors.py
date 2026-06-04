import math

class Divisors:
    def divisors(self, n: int) -> list[int]:
        factors = []

        for i in range(1, math.isqrt(n)+1):
            if n%i == 0:
                factors.append(i)
                if n//i != i:
                    factors.append(n//i)
        factors.sort()

        return factors

if __name__ == "__main__":
    obj = Divisors()
    n = int(input("Enter a number: "))
    res = obj.divisors(n)
    print(f"Divisors of {n} are {res}")