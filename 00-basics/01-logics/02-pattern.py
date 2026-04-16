class Solution:
    def pattern2(self, n):
        for i in range(1, n+1):
            print("*" * i)


if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N: "))
        if not (1 <= N <= 100):
            raise ValueError("Invalid Input! Enter N between 1 and 100.")
        else:
            obj.pattern2(N)
    except ValueError as e:
        print(f"Error: {e}")





