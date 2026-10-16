class Solution:
    def linear_search(self, nums, target):
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        
        return -1


if __name__ == "__main__":
    obj = Solution()
    numbers = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target: "))
    out = obj.linear_search(numbers, target)
    print(out)