class Solution:
    def pattern10(self, n):
        for i in range(n):
            for _ in range(i+1):
                print("*", end="")
            print()
        for i in range(n-1, 0, -1):
            for _ in range(i):
                print("*", end="")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern10(N)
    except ValueError as e:
        print(f"Error! {e}")

