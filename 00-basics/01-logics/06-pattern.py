class Solution:
    def pattern6(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end="")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern6(N)
    except ValueError as e:
        print(f"Error! {e}")
