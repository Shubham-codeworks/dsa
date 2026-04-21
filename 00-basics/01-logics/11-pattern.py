class Solution:
    def pattern11(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                if ((i+j) % 2) == 0:
                    print("1", end="")
                else:
                    print("0", end="")
                if j < i:
                    print(" ", end="")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern11(N)
    except ValueError as e:
        print(f"Error! {e}")

