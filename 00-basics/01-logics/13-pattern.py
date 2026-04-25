class Solution:
    def pattern13(self, n):
        count = 1
        for i in range(n):
            for j in range(i + 1):
                print(count, end=" ")
                count += 1
            print()
            
if __name__ == "__main__":
    obj = Solution()
    try:
        N = int(input("Enter N (1-100):"))
        if not(1 <= N <= 100):
            raise ValueError("Invalid Input! Enter a number between 1 and 100.")
        else:
            obj.pattern13(N)
    except ValueError as e:
        print(f"Error! {e}")