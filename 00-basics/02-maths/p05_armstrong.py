from p01_digit_counter import DigitCount

class Armstrong:
    def is_armstrong(self, num:int) -> bool:
        num_digits = DigitCount().digit_count(num)
        total = 0
        n = num
        
        while n>0:
            last_digit = n % 10
            total += (last_digit) ** num_digits
            n = n // 10
        return num == total

if __name__ == "__main__":
    obj = Armstrong()
    n = int(input("Enter a number: "))
    res = obj.is_armstrong(n)
    print(f"Is {n} an armstrong number? {res}")
