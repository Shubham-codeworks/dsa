class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            print("*" * i)

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern5(N)
    except ValueError as e:
        print(f"Error! {e}")
