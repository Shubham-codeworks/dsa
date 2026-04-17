class Solution:
    def pattern7(self, n):
        for i in range(n):
            for _ in range(n-i-1):
                print(" ", end="")
            for _ in range(n-i-1, n+i):
                print("*", end="")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern7(N)
    except ValueError as e:
        print(f"Error! {e}")
