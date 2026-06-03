from p02_reverse_num import ReverseNumber

class Palindrome:
    def is_palindrome(self, n):
        if n<0:
            return False
        return n == ReverseNumber().rev(n)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    obj = Palindrome()
    res = obj.is_palindrome(num)
    print(f"Is the entered number palindrme: {res}")