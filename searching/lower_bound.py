class Solution:
    def lower_bound(self, nums, x):
        """
        Returns the first index where value is >= x
        """
        l, h = 0, len(nums) - 1
        ans = len(nums)

        while l <= h:
            m = l + (h - l) // 2
            if nums[m] >= x:
                ans = m
                h = m - 1
            else:
                l = m + 1

        return ans


obj = Solution()
print(obj.lower_bound([1, 2, 2, 3], 2))
print(obj.lower_bound([3, 5, 8, 15, 19], 9))
print(obj.lower_bound([3, 5, 8, 15, 19], 3))
print(obj.lower_bound([3, 5, 8, 15, 19], 19))
print(obj.lower_bound([3, 5, 8, 15, 19], 20))
print(obj.lower_bound([3], 2))
print(obj.lower_bound([3], 3))
print(obj.lower_bound([3], 4))
print(obj.lower_bound([3, 3, 3, 3, 3], 3))