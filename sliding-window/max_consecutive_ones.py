class Solution:
    "https://leetcode.com/problems/max-consecutive-ones-iii/"
    def longest_ones(self, nums, k):
        left = 0
        max_size = 0
        zeros_count = 0
        n = len(nums)
        
        for right in range(n):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_size = max(right - left + 1, max_size)

        return max_size

if __name__ == "__main__":
    obj = Solution()
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Enter k: "))
    result = obj.longest_ones(nums, k)
    print(result)