class ReverseNumber:
    def rev(self, n):
        ans = 0
        while n>0:
            last_digit = n%10
            ans = (ans * 10) + last_digit
            n = n//10
        return ans
    
if __name__ == "__main__":
    num = int(input("Enter an positive integer: "))
    obj = ReverseNumber()
    res = obj.rev(num)
    print(f"Your entered number is {num} and reveresed number is {res}.")