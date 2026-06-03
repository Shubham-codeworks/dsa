class DigitCount:
    def digit_count(self, n):
        count = 0
        if n==0:
            count = 1
        n = abs(n)
        while n > 0:
            count += 1
            n = n//10
        return count

if __name__ == "__main__":
    obj = DigitCount()
    num = int(input("Enter a integer: "))
    res = obj.digit_count(num)
    print(f"Your entered integer is {num} and has {res} digits.")


