class Solution:
  def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
      if num in seen and i - seen[num] <= k:
        return True
      seen[num] = i
    return False
    
obj = Solution()
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(obj.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))