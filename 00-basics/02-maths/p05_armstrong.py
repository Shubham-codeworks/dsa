from p01_digit_counter import DigitCount

class Armstrong:
<<<<<<< HEAD
    def is_armstrong(self, num:int) -> bool:
        num_digits = DigitCount().digit_count(num)
        total = 0
        n = num
        
        while n>0:
            last_digit = n % 10
            total += (last_digit) ** num_digits
            n = n // 10
        return num == total
=======
    def is_armstrong(self, n:int) -> bool:
        num_digits = DigitCount().digit_count(n)
        total = 0
        temp = n

        for _ in range(num_digits):
            last_digit = temp % 10
            total += (last_digit) ** num_digits
            temp = temp // 10
            
        return n == total
>>>>>>> a4cfc17f344cbe023ed277e56174aba7fc9b2781

if __name__ == "__main__":
    obj = Armstrong()
    n = int(input("Enter a number: "))
    res = obj.is_armstrong(n)
    print(f"Is {n} an armstrong number? {res}")
