class Solution:
    def pattern1(self, n):
        for i in range(n):
            print("*" * n)

if __name__  == "__main__":
    obj = Solution()
    N = int(input("Enter N: "))
    if not(1<= N <= 100):
        raise ValueError("Input N is out of range")
    else:
        obj.pattern1(N)

