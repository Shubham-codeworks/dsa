class Solution:
    """
    Returns the first index with value higher than x
    """
    def upper_bound(self, nums, x):
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


obj = Solution()
print(obj.upper_bound([1, 2, 2, 3], 2))
print(obj.upper_bound([3, 5, 8, 15, 19], 9))
print(obj.upper_bound([3, 5, 8, 15, 19], 3))
print(obj.upper_bound([3, 5, 8, 15, 19], 19))
print(obj.upper_bound([3, 5, 8, 15, 19], 20))
print(obj.upper_bound([3], 2))
print(obj.upper_bound([3], 3))
print(obj.upper_bound([3], 4))
print(obj.upper_bound([3, 3, 3, 3, 3], 3))