class Solution:
    def pattern9(self, n):
        for i in range(n):
            for _ in range(n-1-i):
                print(" ", end="")
            for _ in range(n-1-i, n+i):
                print("*", end="")
            print()
        for i in range(n,0,-1):
            for _ in range(n-i):
                print(" ", end="")
            for _ in range(n-i, n+i-1):
                print("*", end="")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern9(N)
    except ValueError as e:
        print(f"Error! {e}")

