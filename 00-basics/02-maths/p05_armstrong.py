from p01_digit_counter import DigitCount

class Armstrong:
    def is_armstrong(self, n:int) -> bool:
        num_digits = DigitCount().digit_count(n)
        total = 0
        num = n

        while num > 0:
            last_digit = num % 10
            total += (last_digit) ** num_digits
            num = num // 10
            
        return n == total

if __name__ == "__main__":
    obj = Armstrong()
    n = int(input("Enter a number: "))
    res = obj.is_armstrong(n)
    print(f"Is {n} an armstrong number? {res}")
