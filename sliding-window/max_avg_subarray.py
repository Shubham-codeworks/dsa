class Solution:
    def find_max_average(self, nums: list[int], k: int) -> float:
        "https://leetcode.com/problems/maximum-average-subarray-i/description/"
        curr_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum / k

if __name__ == "__main__":
    obj = Solution()
    nums = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter k: "))
    res = obj.find_max_average(nums, k)
    print(f"{res}")