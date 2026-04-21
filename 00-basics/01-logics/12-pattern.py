class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            for j in range(1, 2*n+1):
                if j <= i:
                    print(j, end="")
                elif j > 2*n - i:
                    print(2*n + 1 - j, end="")
                else:
                    print(" ", end="")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern12(N)
    except ValueError as e:
        print(f"Error! {e}")

