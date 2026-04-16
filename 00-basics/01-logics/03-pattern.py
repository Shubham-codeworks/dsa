class Solution:
    def pattern3(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()

if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N: "))
        if not (1<=N<=100):
            raise ValueError("Invalid Input! Enter N between 1 and 100.")
        else:
            obj.pattern3(N)
    except ValueError as e:
        print(f"Error: {e}")
